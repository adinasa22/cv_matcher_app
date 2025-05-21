import streamlit as st
from utils import extract_text_from_file
from llm_runner import get_match_feedback

st.set_page_config(page_title="Gen AI CV vs Job Description Matcher", layout="wide")
st.title("📄 Gen AI CV vs Job Description Matcher using Local LLM")

# Upload CV
cv_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])

# Paste Job Description
job_description = st.text_area("Paste the Job Description here", height=300)

#Temperature Slider
st.markdown("### Temperature")
st.markdown("Adjust the temperature to control the randomness of the model's output.")
temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.5, step=0.1)


# Match Button
if st.button("🔍 Analyze Match"):
    if not cv_file or not job_description:
        st.warning("Please upload a CV and paste a job description.")
    else:
        with st.spinner("Reading CV and querying local LLM..."):
            cv_text = extract_text_from_file(cv_file)
            percentage, match, mismatch = get_match_feedback(cv_text, job_description, temperature=temperature)

        st.success(f"✅ Match Score: {percentage}%")
        if percentage > 50:
            st.balloons()
        st.markdown("### Feedback:")

        st.markdown("### Reasons to select candidate:")
        st.markdown(match)

        st.markdown("### Reasons to reject candidate:")
        st.markdown(mismatch)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Ollama by Aditya")
