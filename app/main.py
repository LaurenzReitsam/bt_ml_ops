from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Request(BaseModel):
    filename: str


class Response(BaseModel):
    content: str


if __name__ == "__main__":
    app = FastAPI()

    @app.get("/ping")
    async def healthy():
        return {"Healthy"}

    @app.post("/")
    async def predict(request: Request) -> Response:
        try:
            file = Path("./files").resolve() / request.filename
            return Response(content=file.read_text())
        except FileNotFoundError:
            files = [x.name for x in file.parent.iterdir()]
            msg = f"{file=} not found. Possible options are:\n{', '.join(files)}"
            raise HTTPException(404, msg)

    uvicorn.run(app, host="0.0.0.0", port=8080)
