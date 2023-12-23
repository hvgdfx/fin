
import hanlp


data = {
  "text": "张三和李四是好朋友，一起在同一家公司工作。",
  "entities": [
    {"entity": "张三", "start": 0, "end": 2, "label": "Person"},
    {"entity": "李四", "start": 3, "end": 5, "label": "Person"},
    {"entity": "公司", "start": 19, "end": 21, "label": "Organization"}
  ],
  "relations": [
    {"head": "张三", "tail": "李四", "relation": "朋友"},
    {"head": "张三", "tail": "公司", "relation": "工作"},
    {"head": "李四", "tail": "公司", "relation": "工作"}
  ]
}


import torch 
from torch.utils.data import DataLoader, Dataset 

class REDataset(Dataset):
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        sample = self.data[idx]
        text_embedding = encode_text(sample["text"])
        entity_labels = encode_entity_labels(sample["entities"])
        relation_labels = encode_relation_labels(sample["relations"])
        return {
            "text_embedding": text_embedding,
            "entity_labels": entity_labels,
            "relation_labels": relation_labels,
        }
    
datas = [data, data]
redataset = REDataset(datas)
redataloader = DataLoader(redataset, batch_size=1, shuffle=True)

