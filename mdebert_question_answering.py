from transformers import pipeline

qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
question = "Why is model conversion important?"
context = "The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks."
print(qa_model(question=question, context=context))
