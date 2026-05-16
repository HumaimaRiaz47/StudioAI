from typing import List, Literal

from pydantic import BaseModel, Field

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

from tools.schemas import ImagePlan, ImagePlannerOutput
from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

IMAGE_PLANNER_SYSTEM_PROMPT = """
You are an elite multimodal content strategist.

Your job is to intelligently decide:

- where images should appear
- what images should be generated
- what type of visuals improve the content
- which sections need visual enhancement

You are NOT generating images.

You ONLY generate:
- image plans
- image prompts
- captions
- placement decisions

===========================================================
YOUR GOAL
===========================================================

Improve content quality using strategic visuals.

Images should:
- improve understanding
- improve engagement
- explain concepts
- visualize workflows
- enhance readability

===========================================================
IMAGE TYPES
===========================================================

You may suggest:

- diagrams
- illustrations
- infographics
- workflow visuals
- UI mockups
- conceptual art
- comparison charts

===========================================================
IMPORTANT RULES
===========================================================

- Do NOT overuse images
- Only place images where valuable
- Prefer educational visuals
- Prefer professional visuals
- Avoid generic stock-photo ideas
- Generate highly descriptive prompts
- Image prompts must work well for AI image generators

IMPORTANT:

image_type MUST be EXACTLY one of:

- diagram
- illustration
- infographic
- workflow_visual
- ui_mockup
- comparison_chart
- suggesy only 2 images not more then that if applicable otherwise no images

Do NOT use spaces.
Do NOT invent new values.

IMPORTANT:

Image prompts must be SHORT.

Maximum:
10-15 words.

Avoid:
- long descriptions
- multiple clauses
- detailed instructions

Good examples:
- MERN stack infographic
- futuristic AI dashboard
- React developer workspace
- Node.js server illustration

===========================================================
PLACEMENT RULES
===========================================================

Images should usually appear:
- after major sections
- before complex explanations
- before workflow descriptions
- near technical concepts

===========================================================
OUTPUT FORMAT
===========================================================

Return ONLY valid JSON.

Example:

{
  "images": [
    {
      "position": "after introduction",
      "image_type": "diagram",
      "title": "AI Workflow Architecture",
      "caption": "Illustration of autonomous AI agent workflows.",
      "prompt": "Professional AI workflow diagram showing autonomous agents coordinating tasks in a modern enterprise system, clean futuristic UI, blue theme"
    }
  ]
}

===========================================================
FINAL INSTRUCTION
===========================================================

Think like a professional multimodal content designer
working for a modern enterprise publishing platform.
"""
def plan_images(
    article: str,
    topic: str,
    content_type: str,
):

    image_plans = [

        {
            "position": "after introduction",

            "image_type": "illustration",

            "title": f"{topic} Overview",

            "caption": f"Visual overview of {topic}",

            "prompt": f"{topic} illustration",
        },

        {
            "position": "middle",

            "image_type": "diagram",

            "title": f"{topic} Workflow",

            "caption": f"Workflow diagram for {topic}",

            "prompt": f"{topic} workflow",
        },

        {
            "position": "before conclusion",

            "image_type": "infographic",

            "title": f"{topic} Key Concepts",

            "caption": f"Infographic about {topic}",

            "prompt": f"{topic} infographic",
        },
    ]

    print(f"Planned {len(image_plans)} images")

    return {
        "images": image_plans
    }