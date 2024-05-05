import torch.nn as nn


# https://www.kaggle.com/code/salimhammadi07/esc-50-environmental-sound-classification#4.-Model
class CNN(nn.Module):

    def __init__(self):
        super().__init__()
        # 5 conv blocks / flatten / linear / softmax
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=24, kernel_size=(6, 6), stride=1),
            nn.ReLU(),
            nn.BatchNorm2d(24)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=24, out_channels=24, kernel_size=(6, 6), stride=1),
            nn.LeakyReLU(0.2),
            nn.BatchNorm2d(24)
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(in_channels=24, out_channels=48, kernel_size=(5, 5), stride=(2, 2)),
            nn.LeakyReLU(0.2),
            nn.BatchNorm2d(48)
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(in_channels=48, out_channels=48, kernel_size=(5, 5), stride=(2, 2)),
            nn.LeakyReLU(0.2),
            nn.BatchNorm2d(48)
        )
        self.conv5 = nn.Sequential(
            nn.Conv2d(in_channels=48, out_channels=64, kernel_size=(4, 4), stride=1),
            nn.LeakyReLU(0.2),
            nn.BatchNorm2d(64)
        )
        self.conv6 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(4, 4), stride=1),
            nn.LeakyReLU(0.2),
            nn.BatchNorm2d(64)
        )
        self.connected_layer = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 21 * 97, 200),
            nn.Dropout(0.25),
            nn.Linear(200, 50),  # 200 unit
            nn.Softmax(dim=1)
        )

    def forward(self, input_data):
        input_data = input_data.to('cuda')
        x = self.conv1(input_data)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        x = self.connected_layer(x)
        return x
