import streamlit as st
from backend.cortex_search import query_cortex_search
from backend.mistral_integration import generate_answer

st.title("AskDocs AI: Intelligent Knowledge Assistant")

# Upload documents
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv"])
if uploaded_file:
    st.success("File uploaded successfully!")

# Query input
query = st.text_input("Ask a question:")
if query:
    with st.spinner("Searching..."):
        # Step 1: Retrieve relevant content
        results = query_cortex_search(query)
        st.subheader("Retrieved Content")
        for result in results:
            st.write(result[0])

        # Step 2: Generate an answer
        if results:
            context = " ".join([r[0] for r in results])
            answer = generate_answer(f"Context: {context}\nQuestion: {query}")
            st.subheader("Generated Answer")
            st.write(answer)
