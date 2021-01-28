import torch
import torch.nn as nn

class CustomCNN(nn.Module):
    """ Simple Custom CNN for classification which explains how to write model files 

    Args:
        num_classes (int): Number of output classes in your dataset.
    """
    def __init__(self ,num_classes=10):
        super(CustomCNN, self).__init__()
        self.conv_1 = nn.Conv2d(1, 3, kernel_size=(3, 3))
        self.relu_1 = nn.ReLU()
        self.pool_1 = nn.MaxPool2d(kernel_size=2, ceil_mode=False)
        self.conv_2 = nn.Conv2d(3, 5, kernel_size=(3, 3))
        self.relu_2 = nn.ReLU()
        self.pool_2 = nn.MaxPool2d(kernel_size=2, ceil_mode=False)
        self.flatten = nn.Flatten()
        self.linear_1 = nn.Linear(125,20)
        self.relu_3 = nn.ReLU()
        self.linear_2 = nn.Linear(20,num_classes)
        self.relu_4 = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
    def forward(self, x):
        x = self.conv_1(x)
        x = self.relu_1(x)
        x = self.pool_1(x)
        x = self.conv_2(x)
        x = self.relu_2(x)
        x = self.pool_2(x)
        x = self.flatten(x)
        x = self.linear_1(x)
        x = self.relu_3(x)
        x = self.linear_2(x)
        x = self.relu_4(x)
        x = self.softmax(x)

        return x
