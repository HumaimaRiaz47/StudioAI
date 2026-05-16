
from typing import List

from pydantic import BaseModel, Field

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

from tools.schemas import SEOOptimizerOutput


from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

# SYSTEM PROMPT

SEO_OPTIMIZER_SYSTEM_PROMPT = """
You are an SEO editor.

Your task is NOT to rewrite the article.

ONLY:
- improve formatting slightly
- improve readability
- improve heading consistency
- improve keyword placement naturally
- preserve original markdown
- preserve structure
- preserve spacing

IMPORTANT:
- DO NOT duplicate sections
- DO NOT regenerate the article
- DO NOT repeat headings
- DO NOT append extra summaries
- DO NOT add keyword lists
- DO NOT add 'Optimized Content'
- DO NOT add SEO reports

Return ONLY the cleaned markdown article.
"""


def optimize_seo(
    article: str,
    topic: str,
    target_audience: str = "general audience",
):
  

    # ========================================================
# GENERATE SEO OPTIMIZED CONTENT
# ========================================================

    response = llm.invoke(

    [

        SystemMessage(
            content=SEO_OPTIMIZER_SYSTEM_PROMPT 
        ),

        HumanMessage(
            content=f"""

TOPIC:
{topic}

TARGET AUDIENCE:
{target_audience}

ARTICLE:
{article}

==================================================
SEO INSTRUCTIONS
==================================================

1. Improve SEO naturally

2. Improve readability

3. Keep markdown formatting clean

4. Add better headings if needed

5. Improve keyword usage naturally

6. Keep article engaging

7. Do NOT hallucinate facts

8. Return ONLY optimized markdown content
"""
        ),
    ]
)

# ========================================================
# RETURN
# ========================================================

    return {

    "seo_title": topic,

    "meta_description": (
        f"Learn about {topic}."
    ),

    "focus_keywords": [
        topic
    ],

    "optimized_content": response.content
}