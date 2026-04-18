import streamlit as st
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2:3b")

# 🔹 Page config
st.set_page_config(layout="wide")

# 🔹 Sidebar
with st.sidebar:
    st.title("📄 Upload PDFs")
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

    st.title("📝 Notes")

# 🔹 Chat title
st.title("💬 Chat with Documents")

# 🔹 Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 🔹 User input
user_input = st.chat_input("Ask something...")

# 🔹 MAIN LOGIC (PUT YOUR CODE HERE)
if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # 🔹 LLM Response
    docs = []  # (RAG later)
    response = llm.invoke(user_input)

    # Show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

    # 🔹 Save Note Button (INSIDE THIS BLOCK)
    if st.button("Save Note"):
        with open("storage/notes/note.md", "a") as f:
            f.write(response + "\n\n")