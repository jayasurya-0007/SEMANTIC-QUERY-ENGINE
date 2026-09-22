from io import BytesIO
from typing import Literal

import docx
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader


def extract_text_from_pdf(data: bytes) -> str:
    reader = PdfReader(BytesIO(data))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages).strip()


def extract_text_from_docx(data: bytes) -> str:
    document = docx.Document(BytesIO(data))
    paragraphs = [p.text for p in document.paragraphs if p.text]
    return "\n".join(paragraphs).strip()


def extract_text_from_txt(data: bytes) -> str:
    return data.decode("utf-8", errors="ignore").strip()


def extract_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = " ".join(s.strip() for s in soup.stripped_strings)
    return text.strip()


def parse_uploaded_file(filename: str, data: bytes) -> tuple[str, Literal["pdf", "docx", "txt"]]:
    lower_name = filename.lower()
    if lower_name.endswith(".pdf"):
        return extract_text_from_pdf(data), "pdf"
    if lower_name.endswith(".docx"):
        return extract_text_from_docx(data), "docx"
    if lower_name.endswith(".txt"):
        return extract_text_from_txt(data), "txt"
    raise ValueError("Unsupported file type. Use PDF, DOCX, or TXT.")
