# Gen AI CV vs Job Description Matcher with Local LLM (Ollama)

This Streamlit app lets you:
- Upload a resume (.pdf or .docx)
- Paste a job description
- Compare them using a local LLM (e.g., LLaMA3 via Ollama)
- Get match percentage and detailed feedback

## 🔧 Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed locally with `llama3` or `mistral` model

```bash
ollama run llama3
