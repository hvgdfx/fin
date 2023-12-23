
import torch
from transformers import BertTokenizer, BertModel, pipeline

model_path = "/data1/llama/models/bert-base-uncased"

tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertModel.from_pretrained(model_path)
text = "Hi, my name is Rambo, nice to meet you."
text = "你好，我爱北京天安门"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

with torch.no_grad():
    output = model(**encoded_input)

predicted_token_ids = torch.argmax(output.last_hidden_state, dim=-1)
predicted_tokens = tokenizer.batch_decode(predicted_token_ids.squeeze().tolist())
predicted_text = " ".join(predicted_tokens)

print("Original Text:", text)
print("Predicted Text:", predicted_text)

unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)

