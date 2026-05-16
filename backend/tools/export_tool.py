# tools/export_tool.py

import os
import uuid

import markdown2

from weasyprint import HTML

from pydantic import BaseModel


# ============================================================
# OUTPUT DIRECTORY
# ============================================================

OUTPUT_DIR = "exports"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# ============================================================
# SCHEMA
# ============================================================

class ExportOutput(BaseModel):

    markdown_path: str

    pdf_path: str

    markdown_filename: str

    pdf_filename: str


# ============================================================
# TOOL
# ============================================================

def export_article(
    article_markdown: str,
    filename: str = "studio_ai_article",
):

    # ========================================================
    # UNIQUE FILENAMES
    # ========================================================

    unique_id = str(uuid.uuid4())[:8]

    markdown_filename = (
        f"{filename}_{unique_id}.md"
    )

    pdf_filename = (
        f"{filename}_{unique_id}.pdf"
    )

    markdown_path = os.path.join(
        OUTPUT_DIR,
        markdown_filename
    )

    pdf_path = os.path.join(
        OUTPUT_DIR,
        pdf_filename
    )

    # ========================================================
    # SAVE MARKDOWN
    # ========================================================

    with open(
        markdown_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(article_markdown)

    print(f"Markdown saved: {markdown_path}")

    # ========================================================
    # MARKDOWN → HTML
    # ========================================================

    html_content = markdown2.markdown(

        article_markdown,

        extras=[
            "fenced-code-blocks",
            "tables",
            "strike",
            "task_list",
        ]
    )

    # ========================================================
    # STYLED HTML
    # ========================================================

    styled_html = f"""
<html>

<head>

<style>

body {{
    font-family: Arial, sans-serif;
    padding: 32px;
    line-height: 1.6;
    color: #222;
    background-color: white;
    max-width: 900px;
    margin: auto;
}}

h1 {{
    font-size: 34px;
    margin-top: 30px;
    margin-bottom: 16px;
    color: #111;
}}

h2 {{
    font-size: 26px;
    margin-top: 28px;
    margin-bottom: 12px;
    color: #222;
}}

h3 {{
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
}}

p {{
    margin-bottom: 14px;
    font-size: 16px;
}}

img {{
    width: 100%;
    max-width: 700px;
    border-radius: 12px;
    margin: 20px auto;
    display: block;
}}

em {{
    display: block;
    text-align: center;
    color: #666;
    margin-bottom: 20px;
}}

code {{
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 4px;
}}

pre {{
    background: #f4f4f4;
    padding: 16px;
    border-radius: 10px;
    overflow-x: auto;
}}

blockquote {{
    border-left: 4px solid #ddd;
    padding-left: 16px;
    color: #555;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}}

table, th, td {{
    border: 1px solid #ddd;
}}

th, td {{
    padding: 12px;
    text-align: left;
}}

</style>

</head>

<body>

{html_content}

</body>

</html>
"""

    # ========================================================
    # EXPORT PDF
    # ========================================================

    HTML(

        string=styled_html,

        base_url=os.getcwd()

    ).write_pdf(pdf_path)

    print(f"PDF generated: {pdf_path}")

    # ========================================================
    # RETURN
    # ========================================================

    return ExportOutput(

        markdown_path=markdown_path,

        pdf_path=pdf_path,

        markdown_filename=markdown_filename,

        pdf_filename=pdf_filename,

    ).model_dump()