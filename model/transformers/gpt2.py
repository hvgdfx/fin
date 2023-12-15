from transformers import AutoTokenizer, AutoModel, TFAutoModel

model_path = "/data1/llama/models/gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = TFAutoModel.from_pretrained(model_path)



text = 'This is an example sentence for classification.'

def load_torch():
    from transformers import GPT2Tokenizer, GPT2Model
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2Model.from_pretrained(model_path)
    encoded_input = tokenizer(text, return_tensors="pt")
    output = model(**encoded_input)

def load_tf():
    from transformers import GPT2Tokenizer, TFGPT2Model
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = TFGPT2Model.from_pretrained(model_path)
    text = "Replace me by any text you'd like."
    encoded_input = tokenizer(text, return_tensors='tf')
    output = model(encoded_input)

def load_model():
    from transformers import AutoTokenizer, AutoModel
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModel.from_pretrained(model_path, return_tensors="tf")
    text = "Replace me by any text you'd like."
    encoded_input = tokenizer(text, return_tensors='tf')
    output = model(encoded_input)


import numpy as np

# 现在要做一件事：提取内容的事件，包括不限于事件的时间、地点、人物等

# 提取知识图谱，新闻中的主体(人物、组织等)





