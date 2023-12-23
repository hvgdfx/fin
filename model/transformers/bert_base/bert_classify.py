
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
from bs4 import BeautifulSoup
import re
from torch.utils.data import Dataset, DataLoader

def load_model_tokenizer():
    model_path = "/data1/llama/models/bert-base-chinese"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForMaskedLM.from_pretrained(model_path)
    return model, tokenizer

def load_data():
    p = "/data1/llama/models/classify/data.csv"
    texts = []
    labels = []
    with open(p, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "").replace("\r", "")
            matches = re.match(r'"(.*?)","(.*?)","(.*?)"', line)
            category = matches.group(1)
            content = matches.group(2)
            soup = BeautifulSoup(content, 'html.parser')
            extracted_text = soup.get_text()
            texts.append(extracted_text)
            labels.append(category)
            date = matches.group(3)
            print(f"{category} {content} {date}")
    label_to_index = {}
    index_to_label = {}
    for label in labels:
        if label not in label_to_index:
            index_to_label[len(label_to_index)] = label
            label_to_index[label] = len(label_to_index)
    encoded_labels = [label_to_index[label] for label in labels]
    return texts, encoded_labels, label_to_index, index_to_label

def get_train_y(labels):
    label_to_index = {}
    for label in labels:
        if label not in label_to_index:
            label_to_index[label] = len(label_to_index)
    encoded_labels = [label_to_index[label] for label in labels]
    print(f"label_to_index size: {len(label_to_index)}")
    return torch.tensor(encoded_labels), label_to_index

def get_train_x(texts, model, tokenizer):
    tokens = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=100)
    return model(**tokens)
    


class TextClassificationDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    def __len__(self):
        return len(self.texts)
    def __getitem__(self, index):
        text = self.texts[index]
        label = self.labels[index]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt",
        )
        input_ids = encoding["input_ids"].squeeze()
        attention_mask = encoding["attention_mask"].squeeze()
        label = torch.tensor(label)
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "label": label,
        }

def get_labels_classes(labels):
    return len(set(labels))

model, tokenizer = load_model_tokenizer()
texts, labels1, label_to_index, index_to_label = load_data()
num_classes = get_labels_classes(labels=labels1)

text_classify_dataset = TextClassificationDataset(texts=texts, labels=labels, tokenizer=tokenizer, max_length=512)
text_classify_dataloader = DataLoader(text_classify_dataset, batch_size=1, shuffle=True)

import torch.optim as optim
from torch.nn import Linear, Sequential, CrossEntropyLoss

def train():
    num_epochs = 5
    num_classes = 25
    classification_head = Linear(model.config.hidden_size, num_classes)
    model_with_classification_head = Sequential(model, classification_head)
    print(model_with_classification_head)
    optimizer = torch.optim.AdamW(model_with_classification_head.parameters(), lr=2e-5)
    criterion = CrossEntropyLoss()
    for epoch in range(num_epochs):
        model_with_classification_head.train()
        for batch in text_classify_dataloader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['label']
            optimizer.zero_grad()
            outputs = model_with_classification_head(input_ids)
            cls_representation = outputs.last_hidden_state[:, 0, :]
            logits = classification_head(cls_representation)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

train()






