"""Probe the remote h5ad /uns (and /varm) for precomputed DE / marker results.
Same obs-only range-read approach; needs Sanger VPN. Reads only the /uns group metadata."""
import fsspec, h5py
URL = "https://cellgeni-share.cog.sanger.ac.uk/REQ-69024/integrated_scvi_all_tissues_cellxgene_filtered.h5ad"
fs = fsspec.filesystem("https", block_size=2*1024*1024)
h = h5py.File(fs.open(URL, "rb"), "r")

def walk(g, prefix="", depth=0):
    if depth > 3: return
    for k in g.keys():
        it = g[k]
        if isinstance(it, h5py.Group):
            print(f"{prefix}[grp] {k}  attrs={dict(it.attrs)}")
            walk(it, prefix + "    ", depth + 1)
        else:
            print(f"{prefix}[ds]  {k}: shape={getattr(it,'shape',None)} dtype={getattr(it,'dtype',None)}")

print("=== /uns ===")
walk(h["uns"])
print("\n=== /varm keys ===", list(h["varm"].keys()) if "varm" in h else "none")
print("=== /var keys ===", list(h["var"].keys()))
h.close()
print("PROBE_DONE")
