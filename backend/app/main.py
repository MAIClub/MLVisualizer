from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"MAI": "ML - Web study project !!"}