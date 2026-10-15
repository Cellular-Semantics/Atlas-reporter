"""Reference-list parsing across JATS dialects (#35).

Springer/Nature supplies structured ``<element-citation>`` children. AAAS
(Science) supplies one unstructured citation string plus ``<ext-link>``
identifiers — that dialect used to yield a ``ResolvedRef`` with every field
``None``, for every reference, silently.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from textwrap import dedent

import pytest
from atlas_chat.services._jats_parser import (
    _clean_xml,
    _parse_citation_string,
    _parse_ref_list,
    _strip_namespace_from_tree,
)

AAAS_REFS = dedent("""\
    <?xml version="1.0"?>
    <article xmlns:xlink="http://www.w3.org/1999/xlink">
      <back>
        <ref-list>
          <ref id="R1"><label>1.</label><mixed-citation>
            <named-content content-type="citation-string">Park J-E, Jardine L,
              Gottgens B, Haniffa M. Prenatal development of human immunity.
              Science. 2020;368:600-603. doi: 10.1126/science.aaz9330.</named-content>
            <ext-link ext-link-type="doi" xlink:href="10.1126/science.aaz9330"/>
            <ext-link ext-link-type="pmcid" xlink:href="PMC7612900"/>
            <ext-link ext-link-type="pmid" xlink:href="32381715"/>
            <ext-link ext-link-type="google-scholar" xlink:href="journal=Science"/>
          </mixed-citation></ref>
          <ref id="R2"><label>2.</label><mixed-citation>
            <named-content content-type="citation-string">Popescu D-M, et al.
              Decoding human fetal liver haematopoiesis. Nature.
              2019;574:365-371. doi: 10.1038/s41586-019-1652-y.</named-content>
            <ext-link ext-link-type="doi" xlink:href="10.1038/s41586-019-1652-y"/>
          </mixed-citation></ref>
        </ref-list>
      </back>
    </article>
""")

NATURE_REFS = dedent("""\
    <?xml version="1.0"?>
    <article>
      <back>
        <ref-list>
          <ref id="CR1"><element-citation publication-type="journal">
            <person-group><name><surname>Lee</surname><given-names>J</given-names></name></person-group>
            <article-title>Hair-bearing human skin from pluripotent stem cells</article-title>
            <year>2020</year>
            <pub-id pub-id-type="doi">10.1038/s41586-020-2352-3</pub-id>
            <pub-id pub-id-type="pmid">32494013</pub-id>
          </element-citation></ref>
        </ref-list>
      </back>
    </article>
""")


def _refs(xml: str) -> dict:
    root = ET.fromstring(_clean_xml(xml))
    _strip_namespace_from_tree(root)
    return _parse_ref_list(root)


@pytest.mark.unit
def test_aaas_mixed_citation_yields_identifiers_and_metadata() -> None:
    refs = _refs(AAAS_REFS)
    assert set(refs) == {"R1", "R2"}
    r1 = refs["R1"]
    assert r1.doi == "10.1126/science.aaz9330"
    assert r1.pmid == "32381715"
    assert r1.pmcid == "PMC7612900"
    assert r1.year == 2020
    assert r1.first_author == "Park"
    assert r1.title == "Prenatal development of human immunity"
    # "et al." author lists still resolve a surname and a title.
    r2 = refs["R2"]
    assert r2.first_author == "Popescu"
    assert r2.title == "Decoding human fetal liver haematopoiesis"
    assert r2.doi == "10.1038/s41586-019-1652-y"


@pytest.mark.unit
def test_google_scholar_ext_links_are_not_mistaken_for_identifiers() -> None:
    r1 = _refs(AAAS_REFS)["R1"]
    assert "journal=Science" not in (r1.doi, r1.pmid, r1.pmcid)


@pytest.mark.unit
def test_structured_element_citation_still_preferred() -> None:
    r1 = _refs(NATURE_REFS)["CR1"]
    assert r1.doi == "10.1038/s41586-020-2352-3"
    assert r1.pmid == "32494013"
    assert r1.first_author == "Lee"
    assert r1.title == "Hair-bearing human skin from pluripotent stem cells"
    assert r1.year == 2020


@pytest.mark.unit
@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        # Volume-only, no page range.
        (
            "Cao J, et al. A human cell atlas of fetal gene expression. "
            "Science. 2020;370 doi: 10.1126/science.aba7721.",
            {"first_author": "Cao", "year": 2020, "doi": "10.1126/science.aba7721"},
        ),
        # Hyphenated surname, full author list.
        (
            "Jagannathan-Bogdan M, Zon LI. Hematopoiesis. Dev Camb Engl. "
            "2013;140:2463-2467. doi: 10.1242/dev.083147.",
            {"first_author": "Jagannathan-Bogdan", "year": 2013},
        ),
        # Year immediately followed by a colon rather than a semicolon.
        (
            "Jardine L, et al. Blood and immune development in fetal bone marrow. "
            "Nature. 2021:1-5. doi: 10.1038/s41586-021-03929-x.",
            {"year": 2021, "title": "Blood and immune development in fetal bone marrow"},
        ),
    ],
)
def test_citation_string_variants(raw: str, expected: dict) -> None:
    parsed = _parse_citation_string(raw)
    for key, val in expected.items():
        assert parsed[key] == val


@pytest.mark.unit
def test_citation_string_claims_nothing_it_cannot_place() -> None:
    # No year, no recognisable field layout — must not invent a title.
    assert "title" not in _parse_citation_string("Some unstructured note.")
    assert _parse_citation_string("") == {}
