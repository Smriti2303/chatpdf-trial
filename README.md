
# 🤖Tender Chatbot

An intelligent chatbot interface that helps you interact with government tender PDF files. It uses local LLMs and embeddings to answer questions, extract clauses, summarize content, and filter by document — all within an elegant and fast web UI.

---

## 🌟 Features

- 💬 **Conversational AI** for tender documents
- 🧾 **Tender Summary** and Clause Extraction
- 📋 **List all tenders** and extract tender numbers
- 🔍 **Filter by specific PDF**
- 📚 **Chat History** preserved per session
- 🎨 **Attractive UI** with avatars, templates, and styled layout
- 🧠 **Offline Embeddings** using HuggingFace
- ⚡ **Fast responses** (under 10 seconds)

---

## 📂 Project Structure

```

chatpdf-trial/
│
├── app.py                   # Main Streamlit app
├── preprocess\_pdfs.py       # Preprocessing & FAISS index creation
├── htmltemplates.py         # Styled avatars and CSS for chatbot UI
├── requirements.txt         # Python dependencies
├── uploads/                 # Place your PDFs here
├── faiss\_index/             # Stores embeddings and hash file
└── README.md

````

---

## 🛠️ Setup Instructions

### 1. ✅ Clone the Repository

```bash
git clone https://github.com/Smriti2303/chatpdf-trial.git
cd chatpdf-trial
````

### 2. 📦 Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📁 Upload Tender PDFs

Put your tender documents inside the `uploads/` folder.

---

## 🔍 Preprocess PDFs

```bash
python preprocess_pdfs.py
```

This extracts, chunks, embeds, and stores your PDF content into a FAISS index.

---

## 🚀 Run the Chatbot

```bash
streamlit run app.py
```

This launches a beautiful chatbot interface in your browser.

---

## 🧠 Try These Example Questions

* “📋 List all tenders”
* “🧾 Summarize this tender”
* “📌 What is the eligibility criteria?”
* “⚖️ Compare the scope of two tenders”
* “📅 What’s the last submission date?”

---

## 🌐 Deploy for Free (Streamlit Cloud)

1. Push your project to GitHub.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **New app**, select your repo and branch.
4. Set `app.py` as the main file.
5. Click **Deploy** and you’re live! 🌍

> ⚠️ Avoid committing large `.gguf` model files — use `.gitignore` or Git LFS if needed.

---

## 🔐 Environment Setup (Optional)

If you're using an OpenRouter or proxy:

Create a `.env` file with:

```env
GITHUB_TOKEN=your_optional_proxy_key
```

---

## 🧠 Tech Stack

* **Streamlit** — Chat UI
* **LangChain** — LLM Orchestration
* **FAISS** — Vector similarity search
* **HuggingFace Embeddings** — Local sentence embedding
* **PyPDF2** — PDF parsing
* **Ollama / Mistral / LLaMA** — Optional local LLMs

---


---

## 👩‍💻 Author

**Smriti Mahajan**

Built with ❤️ to make government tenders more accessible using AI.

[![GitHub](https://img.shields.io/badge/GitHub-Smriti2303-blue?logo=github)](https://github.com/Smriti2303)

---

## 📄 License

MIT License. Use freely, credit appreciated.

---

```

---

✅ *You can now save this as `README.md` in your project root.*

Would you like me to also generate a sample `requirements.txt` or `.gitignore` file to go with it?
```
