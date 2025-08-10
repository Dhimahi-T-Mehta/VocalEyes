"""
vision_agent.py
----------------
Agent 1: Vision & Understanding Agent

Responsibilities:
- Detect uploaded file type
- Extract text from documents
- Analyze images
- Return clean textual output using Gemini
"""

import os
import io
import base64
import mimetypes
import pdfplumber

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


class VisionAgent:

    def __init__(self, api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash-latest",
            temperature=0.8,
            google_api_key=api_key
        )

    def analyze_file(self, filename: str, file_bytes: bytes) -> str:

        mime_type, _ = mimetypes.guess_type(filename)

        if mime_type is None:
            mime_type = "application/octet-stream"

        # -----------------------------
        # PDF Documents
        # -----------------------------
        if "pdf" in mime_type:

            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                extracted_text = "\n".join(
                    page.extract_text() or ""
                    for page in pdf.pages
                )

            prompt = f"""
            Here is the extracted text from the document '{filename}'.

            Simply return the complete text without changing its meaning.

            {extracted_text}
            """

            response = self.llm.invoke([
                HumanMessage(content=prompt)
            ])

            return response.content

        # -----------------------------
        # Other Documents
        # -----------------------------
        elif (
            mime_type.startswith("text/")
            or "word" in mime_type
        ):

            prompt = f"Extract the complete raw text from '{filename}'."

            response = self.llm.invoke([
                HumanMessage(content=prompt),
                HumanMessage(content=[
                    {
                        "mime_type": mime_type,
                        "data": file_bytes
                    }
                ])
            ])

            return response.content

        # -----------------------------
        # Images
        # -----------------------------
        elif mime_type.startswith("image/"):

            image = base64.b64encode(file_bytes).decode("utf-8")

            prompt = f"Analyze the image '{filename}'."

            response = self.llm.invoke([
                HumanMessage(content=prompt),
                HumanMessage(content=[
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{image}"
                        }
                    }
                ])
            ])

            return response.content

        else:
            raise ValueError(f"Unsupported file type: {mime_type}")