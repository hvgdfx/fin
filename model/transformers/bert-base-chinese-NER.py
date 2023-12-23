
from transformers import (
  BertTokenizerFast,
  AutoModel,
  pipeline,
)

model_path = "/data1/llama/models/bert-base-chinese-ner/"

tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)



nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)