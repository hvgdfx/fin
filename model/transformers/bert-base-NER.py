
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

model_path = "/data1/llama/models/bert-base-NER/"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForTokenClassification.from_pretrained(model_path)

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)