"""Pull the obs table ONLY from a remote 92.8 GB h5ad via HTTP range reads.

Reads only the byte ranges backing /obs (h5py over an fsspec HTTPS file); the
expression matrix, layers, obsm etc. are never downloaded (~a few hundred MB
transferred vs 92.8 GB). Requires the server to honour range requests
(cellgeni-share COG does: accept-ranges: bytes).

NETWORK: the cellgeni-share.cog.sanger.ac.uk host is Sanger-internal. If the
download stalls or returns connection/403 errors from off-site, connect to the
Sanger VPN first. Run took ~6-7 min on-VPN for 2.24M cells x 65 obs columns.
Deps: h5py, fsspec, aiohttp, pandas, pyarrow.
"""
import fsspec, h5py, numpy as np, pandas as pd, time, os
URL="https://cellgeni-share.cog.sanger.ac.uk/REQ-69024/integrated_scvi_all_tissues_cellxgene_filtered.h5ad"
t0=time.time()
fs=fsspec.filesystem("https", block_size=8*1024*1024)
h=h5py.File(fs.open(URL,"rb"),"r")
obs=h["obs"]
order=[c if isinstance(c,str) else c.decode() for c in obs.attrs["column-order"]]
def dec(a):
    if a.dtype.kind in ("S","O"):
        return np.array([x.decode() if isinstance(x,bytes) else x for x in a])
    return a
cols={}
idx=dec(obs["_index"][:])
for name in order:
    item=obs[name]
    if isinstance(item,h5py.Group):
        keys=set(item.keys())
        if {"categories","codes"} <= keys:
            cols[name]=pd.Categorical.from_codes(item["codes"][:], categories=list(dec(item["categories"][:])))
        elif {"values","mask"} <= keys:
            vals=item["values"][:].astype("object"); vals[item["mask"][:]]=None; cols[name]=vals
    else:
        cols[name]=dec(item[:])
h.close()
df=pd.DataFrame(cols, index=pd.Index(idx,name="cell_id"))
df.to_parquet("h5ad_obs/obs.parquet")
print("OK obs shape:", df.shape, "%.1f MB parquet, %.0fs"%(os.path.getsize("h5ad_obs/obs.parquet")/1e6, time.time()-t0))
