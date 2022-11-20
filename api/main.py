from pathlib import Path
from typing import Any

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()


@app.get("/hello")
def read_root() -> dict[str, Any]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}


@app.get("/html", response_class=HTMLResponse)
def return_html() -> str:
    with open(Path("api/index.html"), "r") as f:
        return f.read()


@app.post("/html")
async def post_data(
    calender: str = Form("none"),
    checkbox: str = Form("off"),
    textbox: str = Form("blank"),
    number: str = Form("null"),
    select: str = Form("none"),
) -> dict[str, Any]:
    return {
        "calender": calender,
        "checkbox": checkbox,
        "textbox": textbox,
        "number": number,
        "select": select,
    }


@app.get("/")
async def redirect_docs() -> RedirectResponse:
    return RedirectResponse("http://localhost:8000/docs")
