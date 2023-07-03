from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def index():
    return {"message": "Hello World"}
