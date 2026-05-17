# ============================================================
# backend.py
# ============================================================

from tools.query_generator_tool import (
    query_generator_tool,
)

from tools.search_tool import (
    search_tool,
)

from tools.content_writer_tool import (
    generate_content,
)

from tools.seo_optimizer_tool import (
    optimize_seo,
)

from tools.image_planner_tool import (
    plan_images,
)

from tools.image_generator_tool import (
    generate_images,
)

from tools.article_composer import (
    compose_multimodal_article,
)

from tools.export_tool import (
    export_article,
)


# ============================================================
# PIPELINE
# ============================================================

def run_pipeline(

    topic: str,

    content_type: str = "seo_blog",

    tone: str = "professional",

    enable_image_generation: bool = True
):

    # ========================================================
    # STEP 1 — QUERY GENERATION
    # ========================================================

    print("\n")
    print("=" * 60)
    print("STUDIO AI PIPELINE STARTED")
    print("=" * 60)

    print("\n[1] GENERATING SEARCH QUERIES...")

    query_result = query_generator_tool(

        topic=topic,

        content_type=content_type,
    )

    queries = query_result["queries"]

    print(f"Generated {len(queries)} queries")


    # ========================================================
    # STEP 2 — WEB RESEARCH
    # ========================================================

    print("\n[2] RESEARCHING WEB SOURCES...")

    research_result = search_tool(
        {
            "queries": queries
        }
    )

    evidence = research_result["evidence"]

    print(
        f"Collected {len(evidence)} evidence items"
    )


    # ========================================================
    # STEP 3 — CONTENT GENERATION
    # ========================================================

    print("\n[3] GENERATING CONTENT...")

    article_result = generate_content(

        topic=topic,

        content_type=content_type,

        tone=tone,

        target_audience="AI professionals",

        evidence=evidence,
    )

    # ========================================================
    # CONTENT
    # ========================================================

    article_markdown = article_result["content"]

    print("Content generated successfully")


    # ========================================================
    # STEP 4 — SEO OPTIMIZATION
    # ========================================================

    print("\n[4] OPTIMIZING SEO...")

    seo_result = optimize_seo(

        article=article_markdown,

        topic=topic,

        target_audience="AI professionals",
    )

    optimized_article = seo_result[
        "optimized_content"
    ]

    print("SEO optimization completed")


    # ========================================================
    # IMAGE SECTION
    # ========================================================

    
    generated_images = []

    final_article = optimized_article


    # ========================================================
    # STEP 5 — IMAGE PLANNING
    # ========================================================


    if enable_image_generation:

        print("\n[5] PLANNING IMAGES...")

        image_plan_result = plan_images(

            article=optimized_article,

            topic=topic,

            content_type=content_type,
        )

        image_plans = image_plan_result[
            "images"
        ]

        print(
            f"Planned {len(image_plans)} images"
        )


        # ====================================================
        # STEP 6 — IMAGE GENERATION
        # ====================================================

        print("\n[6] GENERATING IMAGES...")

        image_result = generate_images(
            image_plans=image_plans
        )

        generated_images = image_result[
            "images"
        ]

        print(
            f"Generated {len(generated_images)} images"
        )


        # ====================================================
        # STEP 7 — MULTIMODAL COMPOSITION
        # ====================================================

        print(
            "\n[7] COMPOSING FINAL ARTICLE..."
        )

        final_article = optimized_article

# ====================================================
# APPEND IMAGES TO ARTICLE
# ====================================================

        if generated_images:

            final_article += "\n\n---\n\n"
            final_article += "# Visual Gallery\n\n"

        for image in generated_images:

                local_image_path = (
                f"generated_images/{image['image_path'].split('/')[-1]}"
            )

        final_article += f"""

        ![{image['caption']}]({local_image_path})

        *{image['caption']}*

        """

        print(
            "Multimodal article composed"
        )

    else:

        print(
            "\n[5] IMAGE GENERATION DISABLED"
        )


    # ========================================================
    # STEP 8 — EXPORT
    # ========================================================
    
    print("\n[8] EXPORTING PDF...")

# ========================================================
# SAFE FILENAME
# ========================================================

    import re

# ========================================================
# SAFE FILENAME
# ========================================================

    safe_filename = topic.lower()

# remove invalid filesystem chars

    safe_filename = re.sub(

        r'[<>:"/\\\\|?*“”‘’]',

        '',

        safe_filename
    )

# replace spaces with underscore

    safe_filename = safe_filename.replace(
        " ",
        "_"
    )

# remove commas/dots/newlines

    safe_filename = re.sub(
        r"[,.\n\r]+",
        "",
        safe_filename
    )

# keep filename short

    safe_filename = safe_filename[:60]

# fallback

    if not safe_filename:

        safe_filename = "studio_ai_article"

# ========================================================
# EXPORT
# ========================================================

    export_result = export_article(

        article_markdown=final_article,

        filename=safe_filename,
    )

    print("PDF exported successfully")

    # ========================================================
    # PIPELINE COMPLETE
    # ========================================================

    print("\n")
    print("=" * 60)
    print("STUDIO AI PIPELINE COMPLETED")
    print("=" * 60)


    # ========================================================
    # FINAL OUTPUT
    # ========================================================

    return {

        "topic": topic,

        "queries": queries,

        "final_article": final_article,

        "images": generated_images,

        "pdf_path": export_result[
            "pdf_path"
        ],

        "markdown_path": export_result[
            "markdown_path"
        ],
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    result = run_pipeline(

        topic="""
The Rise of Multimodal AI:
Text, Images, and Autonomous Workflows
""",

        content_type="newsletter",

        tone="professional",

        enable_image_generation=True,
    )

    print("\n")
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(result["pdf_path"])