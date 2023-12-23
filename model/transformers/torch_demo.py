
import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的神经网络
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建示例数据
input_size = 3 * 64 * 64  # 图像大小为3x64x64
hidden_size = 128
output_size = 10  # 假设有10个类别

# 生成随机图像数据和对应标签
num_samples = 100
random_images = torch.randn(num_samples, 3, 64, 64)
random_labels = torch.randint(0, output_size, (num_samples,))

# 初始化模型、损失函数和优化器
model = SimpleModel(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 10
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(random_images.view(-1, input_size))
    
    # 计算损失
    loss = criterion(outputs, random_labels)
    
    # 反向传播和优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 输出训练信息
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

# 保存模型的权重和架构
model_path = "/data1/llama/models/demo/simple_model.pth"
torch.save(model.state_dict(), model_path)

# 加载模型
loaded_model = SimpleModel(input_size, hidden_size, output_size)
loaded_model.load_state_dict(torch.load(model_path))

# 模型处于评估模式
loaded_model.eval()

# 使用加载的模型进行推理
test_input = torch.randn(5, 3, 64, 64)
output = loaded_model(test_input.view(-1, input_size))
print("Model Output:", output)
