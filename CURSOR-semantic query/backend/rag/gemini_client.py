import os

import google.generativeai as genai


class GeminiClient:
    def __init__(self) -> None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.model = None
            return
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.model = genai.GenerativeModel(model_name)

    def generate_answer(self, question: str, context: str) -> str:
        if not self.model:
            raise RuntimeError("Missing GEMINI_API_KEY in environment.")

        prompt = f"""
You are a strict retrieval QA assistant.
Rules:
1) Answer ONLY using the context.
2) If context is insufficient, reply: "I don't have enough information in the provided sources."
3) Be concise and factual.
4) Cite which source chunks are relevant using [source:<id>] markers when available in context.

Context:
{context}

Question:
{question}
"""
        response = self.model.generate_content(prompt)
        return (response.text or "").strip()
