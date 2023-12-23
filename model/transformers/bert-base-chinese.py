
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
from torch.utils.data import DataLoader, TensorDataset
import time

def load_model():
    model_name = "/data1/llama/models/bert-base-chinese"
    num_classes = 25
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_classes)
    model.classifier = nn.Linear(model.config.hidden_size, num_classes)
    return model, tokenizer

def get_dataloader(texts, labels1, tokenizer):
    train_texts = texts[0: 1000] 
    train_labels = labels1[0: 1000]
    inputs = tokenizer(train_texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    labels = torch.tensor(train_labels)
    dataset = TensorDataset(inputs.input_ids, inputs.attention_mask, inputs.token_type_ids, labels)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
    return dataloader

def train(model, dataloader):
    t1 = time.time()
    criterion = nn.CrossEntropyLoss()
    optimizer = AdamW(model.parameters(), lr=2e-5)
    num_epochs = 3
    for epoch in range(num_epochs):
        t2 = time.time()
        for batch in dataloader:
            input_ids, attention_mask, token_type_ids, labels = batch
            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
        print(f"epoch: {str(epoch)}, rt: {str(time.time()-t2)}")
    t3 = time.time()
    print(f"train model time cost: {str(t3 -t1)}")
    return model


def save_model(model):
    model.save_pretrained("fine_tuned_model")

def predict_by_text(model, tokenizer, text):
    test_inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        logits = model(**test_inputs).logits
    predictions = torch.argmax(logits, dim=1)
    print("预测结果:", predictions)
    print("预测结果:", predictions.tolist())
    print("预测结果:", list(map(lambda x: index_to_label[x], predictions.tolist())))


model, tokenizer = load_model()

dataloader = get_dataloader(texts, labels1, tokenizer)

train(model, dataloader)

predict_by_text(model, tokenizer, 
                ["靳东，被誉为剧痴的演员，在电视剧《我的前半生》和《伪装者》中的出色表现一举成名。尽管他出道多年，演艺事业一直平稳发展，但正是这两部作品使他站稳了娱乐圈的脚跟，成为备受瞩目的表演派演员。",
                "红星资本局12月20日消息，日本东芝公司（以下简称“东芝”）将于今日正式退市，结束自1949年以来74年的上市企业历史。据央视新闻援引《朝日新闻》报道，日本东芝公司将于20日从东京证券交易所退市。11月22日，东芝便发布公告宣布了该退市时间。",
                "神舟十六号成功返回，承载着无数人的期待。景海鹏、朱杨柱和桂海潮三位航天员顺利安全地完成了神舟十六号任务，他们成功出舱。景海鹏这次已经进行了4次太空飞行，累计超过200天，成为中国航天员中执行飞行任务次数最多的人。而首位航天飞行工程师朱杨柱和首位载荷专家桂海潮也圆满完成了他们的首次飞行之旅。",
                "在职业世界，地位无所谓高低贵贱，但无可否认的是，无论在学业还是生活中，我们总是面临各种“层级”。就算是在大学这个阶层里，也存在着类似“等级分明”的情况。不同学校的教学质量和整体水平各有千秋。然而，学生们努力提升成绩，唯一目的就是为了进入更优秀的大学，为自己的毕业后职业和个人发展打下更坚实的基础。",
                "新华社北京12月20日电 中央农村工作会议19日至20日在北京召开。会议以习近平新时代中国特色社会主义思想为指导，全面贯彻落实党的二十大和二十届二中全会精神，深入贯彻落实习近平总书记关于“三农”工作的重要论述，贯彻落实中央经济工作会议精神，分析当前“三农”工作面临的形势和挑战，部署2024年“三农”工作。",
                  ])






