import json


def get_match_feedback(cv_text, jd_text, temperature=0.5):
    prompt = f"""
You are a professional resume screening assistant.

Your task is to compare a candidate's CV against a job description and provide a structured JSON output.

Instructions:
- Evaluate how well the CV matches the job description.
- Return a match percentage (0-100).
- List matched skills or experiences in bullet points.
- List missing or mismatched skills or requirements in bullet points.

Return only a valid JSON object in the following format:
{{
  "percentage": <match_percentage>,
  "match": [<list_of_matching_skills_or_experiences>],
  "mismatch": [<list_of_missing_or_mismatched_skills_or_requirements>]
}}

CV:
\"\"\"
{cv_text}
\"\"\"

Job Description:
\"\"\"
{jd_text}
\"\"\"

Try to return the output in a structured JSON format without any additional text or explanation.
Make sure to include all relevant details in the JSON output.
Do not include any other text or explanation outside the JSON object.
Make sure to return a valid JSON object.
Try to return the percentage and feedback using match and mismatch.
"""
    try:
        import ollama
        response = ollama.chat(model='mistral',
                               messages=[{"role": "user", "content": prompt}],
                               options={"temperature": temperature})

        content = json.loads(response['message']['content'])
        percentage = content['percentage']
        match = content['match']
        mismatch = content['mismatch']

        return percentage, match, mismatch

    except Exception as e:
        print(f"Error: {e}")
        return 0, [], []
