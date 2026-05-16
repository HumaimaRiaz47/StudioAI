from typing import List

from dotenv import load_dotenv

from langchain_community.tools.tavily_search import (
    TavilySearchResults
)

load_dotenv()

# ============================================================
# TAVILY SEARCH
# ============================================================

def tavily_search(
    query: str,
    max_results: int = 5
) -> List[dict]:

    tool = TavilySearchResults(
        max_results=max_results
    )

    results = tool.invoke(
        {"query": query}
    )

    normalized: List[dict] = []

    for r in results or []:

        normalized.append(
            {
                "title": r.get("title") or "",

                "url": r.get("url") or "",

                "snippet": (
                    r.get("content")
                    or r.get("snippet")
                    or ""
                )[:500],

                "published_at": (
                    r.get("published_date")
                    or r.get("published_at")
                ),

                "source": r.get("source"),
            }
        )

    return normalized


# ============================================================
# TOOL
# ============================================================

def search_tool(
    queries: List[str]
):

    raw_results: List[dict] = []

    # ========================================================
    # SEARCH ALL QUERIES
    # ========================================================

    for q in queries:

        print(f"Searching: {q}")

        raw_results.extend(
            tavily_search(
                q,
                max_results=5
            )
        )

    if not raw_results:

        return {
            "evidence": []
        }

    # ========================================================
    # DEDUPLICATE
    # ========================================================

    dedup = {}

    for r in raw_results:

        url = r.get("url")

        if url and url not in dedup:

            dedup[url] = {

                "title": r.get("title", ""),

                "url": url,

                "snippet": r.get(
                    "snippet",
                    ""
                )[:500],

                "published_at": r.get(
                    "published_at"
                ),

                "source": r.get(
                    "source"
                ),
            }

    # ========================================================
    # RETURN
    # ========================================================

    evidence = list(dedup.values())

    print(f"Collected {len(evidence)} evidence items")

    return {
        "evidence": evidence
    }