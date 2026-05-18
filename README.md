# StudioAI

StudioAI is an AI-powered multimodal publishing platform that generates high-quality blogs, newsletters, LinkedIn posts, marketing content, SEO-optimized articles, AI-generated visuals, and exportable PDFs.

Built with:
- FastAPI
- React
- Groq LLMs
- Tavily Search
- Pollinations AI
- WeasyPrint

---

# Features

- AI blog generation
- Newsletter generation
- LinkedIn content generation
- SEO optimization
- AI-powered research workflow
- Image generation
- PDF export
- Markdown export
- Real-time dashboard UI
- Streaming-style pipeline updates
- Multimodal article composition

---

# Tech Stack

## Backend
- FastAPI
- Python
- Groq API
- Tavily Search
- WeasyPrint

## Frontend
- React
- TailwindCSS

---

# Pipeline

1. Query Generation
2. Web Research
3. Content Writing
4. SEO Optimization
5. Image Planning
6. Image Generation
7. PDF Export

---

# Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Environment Variables

Create a `.env` file inside backend:

```env
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

---

# API Endpoint

```http
POST /generate
```

Example request:

```json
{
  "topic": "Future of AI Agents",
  "content_type": "seo_blog",
  "tone": "professional",
  "generate_images": true
}
```

---

# Supported Content Types

- SEO Blog
- Newsletter
- LinkedIn Post
- Marketing Copy
- Research Report

---

# 🎥 Demo Video

https://drive.google.com/file/d/1qGkyFXWRSGaYZg0_O74voIAmRk4XfOR-/view?usp=sharing

---

# Future Improvements

- Streaming generation
- Multi-model support
- Team workspaces
- AI editing assistant
- Cloud deployment
- Authentication
- CMS integration

---

# License

MIT License
