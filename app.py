import streamlit as st

st.set_page_config(page_title="AI Document Review Agent", page_icon="📄", layout="centered")

st.title("📄 AI Document Review Agent")
st.write(
    "Upload a document below. The agent will extract its contents and "
    "validate it against a business rule (expected invoice amount: **$2500**)."
)

uploaded_file = st.file_uploader("Upload a document (.txt)", type=["txt"])

if uploaded_file is not None:
    # --- Text Extraction Step ---
    text = uploaded_file.read().decode("utf-8")

    st.subheader("1. Document Loaded")
    st.text_area("Extracted Text", text, height=180)

    # --- Validation Agent Step ---
    st.subheader("2. Validation Result")

    if "$2500" in text:
        st.success("✅ Validation Passed — Amount matches expected value ($2500).")
    else:
        st.error("❌ Validation Failed — Amount does not match expected value ($2500).")
        st.warning("⚠️ Flagged for Human Review — please verify this document manually.")

else:
    st.info("Please upload a document to begin review.")
