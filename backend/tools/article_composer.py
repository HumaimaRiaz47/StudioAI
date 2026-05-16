# tools/article_composer.py

from typing import List

from pydantic import BaseModel


# ============================================================
# SCHEMA
# ============================================================

class ArticleComposerOutput(BaseModel):

    final_article: str


# ============================================================
# TOOL
# ============================================================

def compose_multimodal_article(
    article: str,
    generated_images: List[dict],
):

    # ========================================================
    # SPLIT ARTICLE INTO LINES
    # ========================================================

    lines = article.split("\n")

    composed_lines = []

    image_index = 0

    total_images = len(generated_images)

    # ========================================================
    # INSERT IMAGES AFTER MAJOR HEADINGS
    # ========================================================

    for line in lines:

        composed_lines.append(line)

        # ----------------------------------------------------
        # Detect section headings
        # ----------------------------------------------------

        if (
            line.startswith("## ")
            and image_index < total_images
        ):

            image = generated_images[image_index]

            image_path = image.get(
                "image_path",
                ""
            )

            caption = image.get(
                "caption",
                ""
            )

            image_type = image.get(
                "image_type",
                "illustration"
            )

            prompt = image.get(
                "prompt",
                ""
            )

            # ------------------------------------------------
            # CREATE IMAGE MARKDOWN
            # ------------------------------------------------

            image_markdown = f"""

![{caption}]({image_path})

*{caption}*

<!-- IMAGE TYPE: {image_type} -->

"""

            composed_lines.append(
                image_markdown
            )

            image_index += 1

    # ========================================================
    # APPEND REMAINING IMAGES
    # ========================================================

    while image_index < total_images:

        image = generated_images[image_index]

        image_path = image.get(
            "image_path",
            ""
        )

        caption = image.get(
            "caption",
            ""
        )

        image_markdown = f"""

![{caption}]({image_path})

*{caption}*

"""

        composed_lines.append(
            image_markdown
        )

        image_index += 1

    # ========================================================
    # FINAL ARTICLE
    # ========================================================

    final_article = "\n".join(
        composed_lines
    )

    # ========================================================
    # RETURN
    # ========================================================

    return ArticleComposerOutput(
        final_article=final_article
    ).model_dump()


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    sample_article = """
# AI Agents in Enterprise

Introduction content here.

## Automation

AI automation section.

## AI Workflows

Workflow explanation.

## Future of AI

Future section.
"""

    sample_images = [
        {
            "image_path": "generated_images/workflow.png",

            "caption": "AI Workflow Diagram",

            "image_type": "diagram",

            "prompt": "AI workflow architecture",
        },

        {
            "image_path": "generated_images/dashboard.png",

            "caption": "AI Dashboard",

            "image_type": "ui_mockup",

            "prompt": "AI dashboard UI",
        }
    ]

    result = compose_multimodal_article(
        article=sample_article,
        generated_images=sample_images,
    )

    print(result["final_article"])