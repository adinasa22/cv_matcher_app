response = {'model': 'mistral', 'created_at': '2025-05-21T08:07:47.747347Z', 'message': {'role': 'assistant', 'content': ' {\n "percentage": 80,\n "match": [\n "Experience in developing machine learning models",\n "Knowledge of programming languages such as Python",\n "Experience in analyzing large datasets",\n "Proficiency in SQL"\n ],\n "mismatch": [\n "Lack of experience with large language models (LLMs) for NLP",\n "No experience in designing and developing retrieval-augmented generation (RAG) systems",\n "No specific background or familiarity with the banking sector or financial products",\n "No formal education in Computer Science, Data Science, Statistics"\n ]\n }'}, 'done_reason': 'stop', 'done': True, 'total_duration': 862173168345, 'load_duration': 12874218504, 'prompt_eval_count': 1771, 'prompt_eval_duration': 682762319440, 'eval_count': 152, 'eval_duration': 166483841474}

import json

content = json.loads(response['message']['content'])
print(content['percentage'])
print(content['match'])
print(content['mismatch'])