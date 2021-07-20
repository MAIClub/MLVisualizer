from typing import Optional

from fastapi import FastAPI

app = FastAPI()
# foo


@app.get("/")
def read_root():
    return {"MAI": "ML - Web study project !!"}
