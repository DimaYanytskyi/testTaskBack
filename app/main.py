from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from app.db import get_all_ids, get_record_by_id
app = FastAPI(title="Records API")

@app.get("/records", response_model=List[int])
def read_records():
    ids = get_all_ids()
    return ids


@app.get("/record/{record_id}")
def read_record(record_id: int) -> Dict[str, Any]:
    rec = get_record_by_id(record_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Record not found")

    rtype = rec.get("type")
    out = {"type": rtype}
    if rtype == "webview":
        out["url"] = rec.get("url")
    elif rtype == "image":
        out["picture"] = rec.get("picture")
    elif rtype == "text":
        out["text"] = rec.get("text")
    else:
        raise HTTPException(status_code=500, detail="Invalid record type in DB")

    return out