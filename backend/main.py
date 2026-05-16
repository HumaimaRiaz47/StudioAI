# ============================================================
# main.py
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from backend import run_pipeline

# ============================================================
# APP
# ============================================================

app = FastAPI()


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# STATIC FILES
# ============================================================

app.mount(
    "/generated_images",
    StaticFiles(directory="generated_images"),
    name="generated_images",
)

app.mount(
    "/exports",
    StaticFiles(directory="exports"),
    name="exports",
)


# ============================================================
# REQUEST SCHEMA
# ============================================================

class GenerateRequest(BaseModel):

    topic: str

    content_type: str = "seo_blog"

    tone: str = "professional"

    generate_images: bool = True


# ============================================================
# ROUTES
# ============================================================

@app.get("/")
def home():

    return {
        "message": "StudioAI Backend Running"
    }


@app.post("/generate")
def generate_article(data: GenerateRequest):

    result = run_pipeline(

        topic=data.topic,

        content_type=data.content_type,

        tone=data.tone,

        enable_image_generation=data.generate_images,
    )

    return {

        "success": True,

        "topic": result["topic"],

        "queries": result["queries"],

        "article": result["final_article"],

        "images": result["images"],

        "pdf_path": result["pdf_path"],

        "markdown_path": result["markdown_path"],
    }