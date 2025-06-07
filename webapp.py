from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uuid

from fine_tune_openai import generate_completion

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATA_DIR = os.path.join("data", "user_inputs")
os.makedirs(DATA_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, user_text: str = Form(...)):
    filename = os.path.join(DATA_DIR, f"{uuid.uuid4().hex}.txt")
    with open(filename, "w") as f:
        f.write(user_text)

    prompt = (
        "Write a romantic love letter in the style of the following text:\n"
        f"{user_text}\n---\nLetter:"
    )
    generated = generate_completion(prompt)
    return templates.TemplateResponse(
        "index.html", {"request": request, "generated": generated}
    )
