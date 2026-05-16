# ============================================================
# tools/content_writer_tool.py
# ============================================================

from typing import Literal, List

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


from tools.schemas import ContentWriterOutput

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

# ============================================================
# CONTENT TYPE CONFIG
# ============================================================

CONTENT_TYPE_CONFIG = {

    "seo_blog": {

        "target_words": "1800-2500",

        "style": "Long-form SEO article",
    },

    "linkedin_post": {

        "target_words": "200-500",

        "style": "Short-form viral LinkedIn content",
    },

    "newsletter": {

        "target_words": "800-1500",

        "style": "Digestible email newsletter",
    },

    "marketing_copy": {

        "target_words": "300-800",

        "style": "High-converting marketing copy",
    },

    "research_report": {

        "target_words": "2500-4000",

        "style": "Deep analytical report",
    },
}


# ============================================================
# SYSTEM PROMPTS
# ============================================================

BLOG_SYSTEM_PROMPT = """
You are an elite SEO blog writer working inside StudioAI.

You create:
- long-form premium blog articles
- deeply researched SEO content
- publication-quality educational content

Your writing style:
- authoritative
- insightful
- polished
- professional
- engaging

You NEVER write shallow summaries.
"""


LINKEDIN_SYSTEM_PROMPT = """
You are an elite LinkedIn ghostwriter.

You specialize in:
- viral professional content
- engagement-focused writing
- authority-building storytelling

Your writing feels:
- human
- emotional
- modern
- concise
"""


NEWSLETTER_SYSTEM_PROMPT = """
You are a premium newsletter writer.

You create:
- insightful newsletters
- digestible updates
- curated industry insights

Your writing feels:
- conversational
- valuable
- readable
- modern
"""


MARKETING_COPY_SYSTEM_PROMPT = """
You are an elite conversion-focused copywriter.

You specialize in:
- persuasive messaging
- SaaS positioning
- emotional marketing
- conversion optimization

Your writing should:
- drive action
- increase conversions
- communicate value clearly
"""


RESEARCH_REPORT_SYSTEM_PROMPT = """
You are a professional research analyst.

You create:
- analytical reports
- structured research
- evidence-based documentation

Your writing should:
- be deeply analytical
- remain factual
- include trends and insights
"""


# ============================================================
# PROMPT MAP
# ============================================================

PROMPTS = {

    "seo_blog": BLOG_SYSTEM_PROMPT,

    "linkedin_post": LINKEDIN_SYSTEM_PROMPT,

    "newsletter": NEWSLETTER_SYSTEM_PROMPT,

    "marketing_copy": MARKETING_COPY_SYSTEM_PROMPT,

    "research_report": RESEARCH_REPORT_SYSTEM_PROMPT,
}


# ============================================================
# TOOL
# ============================================================

def generate_content(

    topic: str,

    content_type: Literal[
        "seo_blog",
        "linkedin_post",
        "newsletter",
        "marketing_copy",
        "research_report",
    ] = "seo_blog",

    tone: str = "professional",

    target_audience: str = "General audience",

    evidence: List[dict] = [],
):

    # ========================================================
    # SELECT SYSTEM PROMPT
    # ========================================================

    system_prompt = PROMPTS.get(
        content_type,
        BLOG_SYSTEM_PROMPT,
    )


    # ========================================================
    # CONFIG
    # ========================================================

    config = CONTENT_TYPE_CONFIG.get(
        content_type,
        CONTENT_TYPE_CONFIG["seo_blog"]
    )

    target_words = config["target_words"]

    style_description = config["style"]


    # ========================================================
    # CONTENT TYPE RULES
    # ========================================================

    content_rules = ""

    # --------------------------------------------------------
    # LINKEDIN
    # --------------------------------------------------------

    if content_type == "linkedin_post":

        content_rules = """

LINKEDIN POST RULES:

- DO NOT write a blog article
- Write like a top LinkedIn creator
- Start with a strong hook
- Use short paragraphs
- Use whitespace heavily
- Keep sentences concise
- Focus on engagement
- Include emotional storytelling
- Add curiosity
- Include a strong CTA
- Avoid H1/H2 markdown headings
- Optimize for shares and comments
"""


    # --------------------------------------------------------
    # NEWSLETTER
    # --------------------------------------------------------

    elif content_type == "newsletter":

        content_rules = """

NEWSLETTER RULES:

- DO NOT write a blog article
- Write like a premium newsletter
- Use conversational writing
- Focus on digestible insights
- Include practical takeaways
- Keep formatting lightweight
- Avoid academic structure
- Use short sections
- Feel curated and editorial
- Make it enjoyable to read
"""


    # --------------------------------------------------------
    # MARKETING COPY
    # --------------------------------------------------------

    elif content_type == "marketing_copy":

        content_rules = """

MARKETING COPY RULES:

- DO NOT write a blog article
- Focus on persuasion
- Focus on benefits over features
- Use emotional triggers
- Use compelling language
- Optimize for conversions
- Include strong CTAs
- Keep writing concise
- Avoid long educational explanations
- Make readers want action immediately
"""


    # --------------------------------------------------------
    # RESEARCH REPORT
    # --------------------------------------------------------

    elif content_type == "research_report":

        content_rules = """

RESEARCH REPORT RULES:

- Write analytical content
- Use structured sections
- Include trends and insights
- Maintain formal tone
- Use evidence heavily
- Include findings
- Include implications
- Feel like professional industry research
- Keep writing factual and data-driven
"""


    # --------------------------------------------------------
    # SEO BLOG
    # --------------------------------------------------------

    else:

        content_rules = """

SEO BLOG RULES:

- Write long-form SEO content
- Use H1/H2/H3 headings
- Expand concepts deeply
- Include examples
- Include practical applications
- Optimize readability
- Make content educational
- Make content comprehensive
- Use strong markdown formatting
"""


    # ========================================================
    # FORMAT EVIDENCE
    # ========================================================

    evidence_text = ""

    for item in evidence:

        title = item.get("title", "")

        snippet = item.get("snippet", "")

        source = item.get("source", "")

        url = item.get("url", "")

        evidence_text += f"""

TITLE:
{title}

SNIPPET:
{snippet}

SOURCE:
{source}

URL:
{url}

==================================================
"""


    # ========================================================
    # STRUCTURED OUTPUT
    # ========================================================




    # ========================================================
    # GENERATE CONTENT
    # ========================================================

    response = llm.invoke(

        [

            SystemMessage(
                content=system_prompt
            ),

            HumanMessage(
                content=f"""

TOPIC:
{topic}

CONTENT TYPE:
{content_type}

STYLE:
{style_description}

TARGET LENGTH:
{target_words} words

TONE:
{tone}

TARGET AUDIENCE:
{target_audience}

==================================================
CONTENT TYPE RULES
==================================================

{content_rules}

==================================================
RESEARCH EVIDENCE
==================================================

{evidence_text}

==================================================
WRITING INSTRUCTIONS
==================================================

1. First internally plan:
   - introduction
   - key sections
   - flow
   - conclusion

2. Maintain high readability

3. Use evidence naturally

4. Keep writing factual

5. Avoid hallucinations

6. Write polished premium-quality content

7. Match EXACTLY the requested content type

8. Maintain modern formatting

9. Make content engaging and valuable

10. Suggest visuals naturally where useful

==================================================
VERY IMPORTANT
==================================================

DO NOT default to blog article style.

Strictly follow the requested content type.

The output should feel like professionally
published premium content.
"""
            ),
        ]
    )


    # ========================================================
    # RETURN
    # ========================================================

    return {
        "content": response.content
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    sample_evidence = [

        {
            "title": "AI Agents in Enterprise",

            "snippet": """
AI agents are transforming enterprise workflows
through automation and reasoning.
""",

            "source": "TechCrunch",

            "url": "https://example.com",
        }
    ]


    # ========================================================
    # TEST NEWSLETTER
    # ========================================================

    result = generate_content(

        topic="""
The Rise of Multimodal AI:
Text, Images, and Autonomous Workflows
""",

        content_type="newsletter",

        tone="professional",

        target_audience="""
AI founders, creators, and tech professionals
""",

        evidence=sample_evidence,
    )

    print(result)