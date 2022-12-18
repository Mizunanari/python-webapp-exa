from pathlib import Path
from typing import Any

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/hello")
def read_root() -> dict[str, Any]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}


@app.get("/html", response_class=HTMLResponse)
def return_html() -> str:
    with open(Path("public/example.html"), "r") as f:
        return f.read()


@app.get("/html2", response_class=HTMLResponse)
def return_html2() -> str:
    with open(Path("public/example2.html"), "r") as f:
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


@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon() -> FileResponse:
    return FileResponse("public/favicon.ico")


@app.get("/", include_in_schema=False)
async def redirect_docs() -> RedirectResponse:
    return RedirectResponse("http://localhost:8000/docs")
