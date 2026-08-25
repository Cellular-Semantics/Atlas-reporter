# incoming/

Drop supplementary files here by hand (any format). Everything in this folder is
git-ignored except this README.

The indexer treats a file dropped here exactly like one it fetched itself — the
manifest records `retrieval.route: "manual"` instead of a URL. This is the only
route available for closed-access papers, which are out of scope for automated
retrieval.

Layout: one subdirectory per paper, named with the paper's DOI slug
(DOI lowercased, `/` → `_`), e.g.

    incoming/10.1038_s41586-024-08002-x/41586_2024_8002_MOESM4_ESM.zip
