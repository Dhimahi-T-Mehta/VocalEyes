# 🎙️ VocalEyes

> **Hear the World, See the Possibilities.**

VocalEyes is an AI-powered **Multi-Agent Accessibility System** designed to help visually impaired individuals independently access and understand visual information. By combining document and image understanding with natural-sounding speech synthesis, the system transforms uploaded content into clear, spoken audio.

Developed as part of IBM's **"From Learner to Beginner: Become an AI Agent Architect"** certification program, VocalEyes demonstrates how multiple AI agents can collaborate to solve real-world accessibility challenges.

---

## 🌍 Sustainable Development Goals

* **SDG 10 – Reduced Inequalities** *(Primary)*
* **SDG 4 – Quality Education**
* **SDG 3 – Good Health and Well-being**

---

## ✨ Features

* Upload documents and images
* Extract text from PDFs and documents
* Analyze visual content using AI
* Generate contextual descriptions
* Convert extracted information into natural speech
* Simple interface for accessibility-focused interaction

---

## 🤖 Multi-Agent Architecture

### Agent 1 — Vision & Understanding

Responsible for understanding uploaded content.

**Technologies**

* Google Gemini 1.5 Flash
* LangChain

**Responsibilities**

* Detect file type
* Extract document text
* Analyze images
* Understand content
* Generate structured text

---

### Agent 2 — Speech Generation

Responsible for converting text into speech.

**Technology**

* Murf AI API

**Responsibilities**

* Receive processed text
* Generate high-quality speech
* Produce downloadable MP3 audio

---

## 🔄 Workflow

```text
User Upload
      │
      ▼
Vision & Understanding Agent
      │
      ▼
Extracted Text
      │
      ▼
Speech Generation Agent
      │
      ▼
Natural Audio Output
```

---

## 🛠️ Tech Stack

| Category  | Technologies             |
| --------- | ------------------------ |
| Language  | Python                   |
| AI        | Google Gemini 1.5 Flash  |
| Framework | LangChain                |
| Speech    | Murf AI                  |
| Interface | Google Colab, ipywidgets |

---

## 📁 Supported File Types

* PDF
* TXT
* DOC / DOCX
* JPG
* JPEG
* PNG
* GIF

---

## 🚀 Future Enhancements

* Regional language support
* Real-time camera input
* Offline OCR
* Voice commands
* Additional specialized AI agents
* Cloud deployment

---

## 👨‍💻 Author

**Dhimahi T. Mehta**

Final Year B.E. Computer Engineering Student

---

## 📜 License

This project is released under the MIT License.
