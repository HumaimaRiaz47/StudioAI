from typing import TypedDict, List, Optional, Literal, Annotated
from pydantic import BaseModel, Field
import operator

# -----------------------------
# 1) Schemas
# -----------------------------
class Task(BaseModel):
    id: int
    title: str

    goal: str = Field(
        ...,
        description="One sentence describing what the reader should be able to do/understand after this section.",
    )
    bullets: List[str] = Field(
        ...,
        min_length=3,
        max_length=6,
        description="3–6 concrete, non-overlapping subpoints to cover in this section.",
    )
    target_words: int = Field(..., description="Target word count for this section (120–550).")

    tags: List[str] = Field(default_factory=list)
    requires_research: bool = False
    requires_citations: bool = False
    requires_code: bool = False


class Plan(BaseModel):
    blog_title: str
    audience: str
    tone: str
    blog_kind: Literal["explainer", "tutorial", "news_roundup", "comparison", "system_design"] = "explainer"
    constraints: List[str] = Field(default_factory=list)
    tasks: List[Task]


class EvidenceItem(BaseModel):
    title: str
    url: str
    published_at: Optional[str] = None  # keep if Tavily provides; DO NOT rely on it
    snippet: Optional[str] = None
    source: Optional[str] = None


class RouterDecision(BaseModel):
    needs_research: bool
    mode: Literal["closed_book", "hybrid", "open_book"]
    queries: List[str] = Field(default_factory=list)


class EvidencePack(BaseModel):
    evidence: List[EvidenceItem] = Field(default_factory=list)

class State(TypedDict):
    topic: str

    # routing / research
    mode: str
    needs_research: bool
    queries: List[str]
    evidence: List[EvidenceItem]
    plan: Optional[Plan]

    # workers
    sections: Annotated[List[tuple[int, str]], operator.add]  # (task_id, section_md)
    final: str

class QueryGeneratorOutput(BaseModel):

    content_type: Literal[
        "seo_blog",
        "linkedin_post",
        "newsletter",
        "marketing_copy",
        "research_report",
    ]

    tone: str

    target_audience: str

    search_strategy: str

    queries: List[str] = Field(
        default_factory=list
    )


class ContentWriterOutput(BaseModel):

    title: str

    content: str

    summary: str

    suggested_image_prompts: List[str] = Field(
        default_factory=list
    )

class SEOOptimizerOutput(BaseModel):

    seo_title: str

    meta_description: str

    focus_keywords: List[str] = Field(
        default_factory=list
    )

    optimized_content: str


class ImagePlan(BaseModel):

    position: str

    image_type: Literal[
        "diagram",
        "illustration",
        "infographic",
        "workflow_visual",
        "ui_mockup",
        "comparison_chart",
    ]

    title: str

    caption: str

    prompt: str

class ImagePlannerOutput(BaseModel):

    images: List[ImagePlan] = Field(
        default_factory=list
    )



class GeneratedImage(BaseModel):

    image_path: str

    caption: str

    prompt: str


class ImageGeneratorOutput(BaseModel):

    images: List[GeneratedImage] = Field(
        default_factory=list
    )

class GeneratedImage(BaseModel):

    image_path: str

    caption: str

    prompt: str

    image_type: str


class MultimodalComposerOutput(BaseModel):

    final_article: str
