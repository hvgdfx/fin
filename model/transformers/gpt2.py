from transformers import AutoTokenizer, AutoModel, TFAutoModel

model_path = "/data1/llama/models/gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = TFAutoModel.from_pretrained(model_path)

text = 'This is an example sentence for classification.'


def load_torch():
    from transformers import GPT2Tokenizer, GPT2Model
    tokenizer = GPT2Tokenizer.from_pretrained(model_path + "/torch")
    model = GPT2Model.from_pretrained(model_path + "/torch")
    encoded_input = tokenizer(text, return_tensors="pt")
    output = model(**encoded_input)
    model.generate()


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

def main():
    from transformers import GPT2Tokenizer, GPT2Model
    tokenizer = GPT2Tokenizer.from_pretrained(model_path + "/torch")
    model = GPT2Model.from_pretrained(model_path + "/torch")

    encoded_prompt = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

    output_sequences = model.generate(
        input_ids=encoded_prompt,
        max_length=len(encoded_prompt[0]),
        # temperature=args.temperature,
        # top_k=args.k,
        # top_p=args.p,
        # repetition_penalty=args.repetition_penalty,
        do_sample=True,
        # num_return_sequences=args.num_return_sequences,
    )


if __name__ == '__main__':
    main()
