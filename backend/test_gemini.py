from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()


# ============================================================
# MODEL
# ============================================================

llm = ChatGroq(

    model="llama-3.3-70b-versatile",

    temperature=0.7,
)


# ============================================================
# TEST
# ============================================================

response = llm.invoke("""

Write a short LinkedIn post about:
AI agents transforming businesses.

Keep it engaging.

""")

print("\n")
print("=" * 60)
print("GROQ RESPONSE")
print("=" * 60)

print(response.content)