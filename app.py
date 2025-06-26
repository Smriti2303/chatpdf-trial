import os
import time
import pickle
import streamlit as st
from dotenv import load_dotenv
from htmltemplates import css, bot_template, user_template
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseRetriever
from langchain.schema.document import Document
from typing import List, Any
from pydantic import Field

# --- Load environment variables ---
load_dotenv()
api_key = os.getenv("GITHUB_TOKEN")

# --- Auto-build FAISS index if not present ---
if not os.path.exists("faiss_index/index.pkl"):
    from preprocess_pdfs import main as build_index
    build_index()

# --- Load FAISS vectorstore ---
with open("faiss_index/index.pkl", "rb") as f:
    vectorstore_data = pickle.load(f)

if isinstance(vectorstore_data, tuple) and hasattr(vectorstore_data[0], "similarity_search"):
    vectorstore, tender_data = vectorstore_data
else:
    st.error("Invalid FAISS vectorstore loaded. Please regenerate the index.")
    st.stop()

# --- Initialize session state ---
for key, default in {
    "chat_history": [],
    "chat_history_display": [],
    "smart_mode": True,
    "selected_pdf": "All PDFs"
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --- Extract available PDFs ---
try:
    all_docs = vectorstore.similarity_search("dummy", k=1000)
except Exception:
    all_docs = []

all_pdfs = sorted({
    doc.metadata.get("source", "").split("/")[-1]
    for doc in all_docs if "source" in doc.metadata
})

# --- Setup LLM ---
llm = ChatOpenAI(
    model="openai/gpt-4o",
    api_key=api_key,
    base_url="https://models.github.ai/inference"
)

# --- Setup memory ---
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# --- Custom Retriever ---
class CustomRetriever(BaseRetriever):
    vectorstore: Any = Field()
    selected_pdf: str = Field()

    def _get_relevant_documents(self, query: str) -> List[Document]:
        all_results = self.vectorstore.similarity_search(query, k=20)
        if self.selected_pdf == "All PDFs":
            return all_results[:5]
        return [
            doc for doc in all_results
            if doc.metadata.get("source", "").endswith(self.selected_pdf)
        ][:5]

retriever = CustomRetriever(vectorstore=vectorstore, selected_pdf=st.session_state.selected_pdf)

# --- Build chain ---
chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

# --- Display chat messages ---
def display_chat(user_msg, bot_msg, response_time=None):
    st.markdown(user_template.replace("{{MSG}}", user_msg), unsafe_allow_html=True)
    msg = bot_msg
    if response_time is not None:
        msg += f"\n\n⏱️ _Responded in {response_time}s_"
    st.markdown(bot_template.replace("{{MSG}}", msg), unsafe_allow_html=True)

# --- Handle user input ---
def handle_userinput(query: str):
    with st.spinner("🔍 Thinking..."):
        start = time.time()
        result = chain({"question": query, "chat_history": st.session_state.chat_history})
        end = time.time()
        response_time = round(end - start, 2)

        st.session_state.chat_history.append((query, result["answer"]))
        st.session_state.chat_history_display.insert(0, (query, result["answer"], response_time))
        display_chat(query, result["answer"], response_time)
        st.session_state.question = ""  # Reset input box

# --- Main layout ---
def main():
    st.set_page_config(page_title="📘 Chat with Tender PDFs", layout="wide")
    st.markdown(css, unsafe_allow_html=True)
    st.title("🤖 Chat with Tender PDFs")

    col1, col2 = st.columns([1, 4])

    with col1:
        with st.sidebar:
            st.markdown("### 📂 Filter Tenders")
            st.session_state.selected_pdf = st.selectbox("Choose PDF", ["All PDFs"] + all_pdfs)

            st.markdown("### 💡 Sample Prompts")
            st.button("📋 List all tenders", on_click=lambda: st.session_state.update({"question": "List all tenders"}))
            st.button("🧾 Summarize this tender", on_click=lambda: st.session_state.update({"question": "Summarize this tender document"}))
            st.button("📌 Eligibility Criteria", on_click=lambda: st.session_state.update({"question": "What is the eligibility criteria?"}))

            st.markdown("### 🕘 Chat History")
            for i, (q, a, t) in enumerate(st.session_state.chat_history_display):
                with st.expander(f"🔹 {q}", expanded=False):
                    st.markdown(f"{a}\n\n_🕓 Responded in {t}s_")

    with col2:
        st.markdown("#### 💬 Ask your question")
        question = st.text_input("Type here and press Enter", key="question")
        if question:
            handle_userinput(question)

        if st.session_state.chat_history_display:
            st.markdown("### 🧠 Conversation")
            for q, a, t in st.session_state.chat_history_display:
                display_chat(q, a, t)

if __name__ == "__main__":
    main()
