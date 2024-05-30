Model training / testing results will be saved  in this folder.

## sample-run ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes)
terminal.pt         
          TestAcc TestLoss
1          0.685    1.155
2          0.665    1.173
3          0.688    1.166
4          0.790    0.814
5          0.688    1.169
mean       0.703    1.095
std        0.050    0.157
* 
## 2024-05-01-16-09 ResNet(block=ResidualBlock, layers=[3, 4, 6, 3], num_classes=config.n_classes)
* num_workers = 4 
* optimizer = torch.optim.SGD(model.parameters(), lr=config.lr, momentum=0.9, weight_decay=config.weight_decay)
* Early stopping (20)
  * 33%|##6     | 66/200 [1:03:06<2:08:07, 57.37s/ep]
  * 24%|##4       | 48/200 [46:06<2:25:59, 57.63s/ep]
  * 24%|##4       | 48/200 [45:48<2:25:02, 57.25s/ep]
  * 29%|##9       | 58/200 [55:30<2:15:52, 57.42s/ep]
  * 28%|##8       | 56/200 [55:22<2:22:23, 59.33s/ep]
terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.623    1.354            0.630    1.367
2          0.652    1.305            0.660    1.292
3          0.618    1.412            0.610    1.395
4          0.672    1.273            0.680    1.271
5          0.665    1.386            0.672    1.361
mean       0.646    1.346            0.650    1.337
std        0.025    0.057            0.030    0.053

## 2024-05-05-13-16 CNN()
* num_workers = 2
* optimizer = torch.optim.Adam(model.parameters(), lr=3e-4)
* Early stopping (20)
  * 27%|##7       | 54/200 [53:05<2:23:32, 58.99s/ep] TrnAcc=0.045 ValAcc=0.034 TrnLoss=3.901 ValLoss=3.912 
  * 10%|#         | 21/200 [20:31<2:54:56, 58.64s/ep] TrnAcc=0.034 ValAcc=0.031 TrnLoss=3.911 ValLoss=3.915
  * 14%|#3        | 27/200 [26:54<2:56:47, 61.31s/ep] TrnAcc=0.016 ValAcc=0.016 TrnLoss=3.929 ValLoss=3.930 
  * 11%|#1        | 22/200 [21:37<2:55:00, 58.99s/ep] TrnAcc=0.037 ValAcc=0.013 TrnLoss=3.908 ValLoss=3.933 
  * 10%|#         | 21/200 [20:37<2:55:44, 58.91s/ep] TrnAcc=0.037 ValAcc=0.034 TrnLoss=3.909 ValLoss=3.911
    TestAcc  TestLoss
1       0.060     3.886
2       0.030     3.917
3       0.013     3.933
4       0.040     3.905
5       0.045     3.898
mean    0.037     3.908
std     0.018     0.018

## 2024-05-05-17-27 ResNet50()
* num_workers = 2
* dropout_rate = 0.5
* gamma = 0.8
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 20%|##        | 41/200 [42:15<2:43:51, 61.83s/ep] TrnAcc=0.742 ValAcc=0.244 TrnLoss=0.830 ValLoss=3.889
  * 12%|#1        | 23/200 [24:12<3:09:29, 64.23s/ep] TrnAcc=0.329 ValAcc=0.041 TrnLoss=2.161 ValLoss=7.965
  * 12%|#2        | 24/200 [24:55<3:02:48, 62.32s/ep] TrnAcc=0.534 ValAcc=0.062 TrnLoss=1.504 ValLoss=9.457
  * 18%|#7        | 35/200 [35:21<2:46:39, 60.60s/ep] TrnAcc=0.578 ValAcc=0.131 TrnLoss=1.351 ValLoss=5.212 
  * 12%|#1        | 23/200 [23:23<2:59:57, 61.00s/ep] TrnAcc=0.540 ValAcc=0.084 TrnLoss=1.522 ValLoss=6.788
        terminal.pt          best_val_loss.pt         
        TestAcc TestLoss          TestAcc TestLoss
1          0.190    4.171            0.105    3.977
2          0.040    8.060            0.020    4.122
3          0.020   10.118            0.020    3.918
4          0.092    5.393            0.138    3.367
5          0.083    6.929            0.020    4.001
mean       0.085    6.934            0.060    3.877
std        0.066    2.314            0.057    0.295

## not saved ResNet50()
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 16%|#6        | 32/200 [32:04<2:43:08, 58.26s/ep] TrnAcc=0.592 ValAcc=0.259 TrnLoss=1.351 ValLoss=2.928
  * 19%|#9        | 38/200 [38:06<2:42:54, 60.34s/ep] TrnAcc=0.620 ValAcc=0.284 TrnLoss=1.289 ValLoss=2.825 
  * 15%|#5        | 30/200 [31:15<2:56:52, 62.43s/ep] TrnAcc=0.573 ValAcc=0.184 TrnLoss=1.473 ValLoss=3.881
  * 16%|#5        | 31/200 [31:29<2:48:42, 59.89s/ep] TrnAcc=0.585 ValAcc=0.278 TrnLoss=1.404 ValLoss=3.084
  * 14%|#4        | 28/200 [28:10<2:45:31, 57.74s/ep] TrnAcc=0.574 ValAcc=0.163 TrnLoss=1.423 ValLoss=4.026
      TestAcc  TestLoss
1       0.253     3.247
2       0.302     2.907
3       0.168     3.897
4       0.242     3.208
5       0.140     4.307
mean    0.221     3.513
std     0.066     0.572

## 2024-05-06-06-15 ResNet18()
* num_workers = 2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 27%|##7       | 54/200 [52:13<2:15:27, 55.66s/ep] TrnAcc=0.866 ValAcc=0.700 TrnLoss=0.610 ValLoss=1.143
  * 28%|##8       | 57/200 [54:43<2:16:03, 57.09s/ep] TrnAcc=0.903 ValAcc=0.716 TrnLoss=0.493 ValLoss=1.033
  * 20%|##        | 40/200 [39:17<2:37:27, 59.05s/ep] TrnAcc=0.929 ValAcc=0.716 TrnLoss=0.390 ValLoss=1.114 
  * 26%|##6       | 53/200 [53:12<2:22:58, 58.36s/ep] TrnAcc=0.852 ValAcc=0.709 TrnLoss=0.605 ValLoss=1.085
  * 22%|##1       | 43/200 [40:37<2:17:42, 52.63s/ep] TrnAcc=0.890 ValAcc=0.716 TrnLoss=0.537 ValLoss=1.032  
          terminal.pt          best_val_loss.pt         
          TestAcc TestLoss          TestAcc TestLoss
1          0.598    1.461            0.595    1.458
2          0.603    1.410            0.600    1.413
3          0.608    1.394            0.603    1.389
4          0.700    1.025            0.693    1.022
5          0.618    1.417            0.615    1.415
mean       0.625    1.342            0.621    1.339
std        0.043    0.179            0.041    0.179
    
## 2024-05-06-09-38 ResNet18() with RandomScale, RandomNoise, FrequencyMask, TimeMask
* num_workers = 2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 30%|##4     | 60/200 [1:16:05<2:58:57, 76.69s/ep] TrnAcc=0.587 ValAcc=0.600 TrnLoss=1.404 ValLoss=1.527
  * 24%|#9      | 48/200 [1:00:28<2:59:48, 70.98s/ep] TrnAcc=0.670 ValAcc=0.641 TrnLoss=1.192 ValLoss=1.270 
  * 21%|##1     | 42/200 [52:06<3:17:07, 74.86s/ep] TrnAcc=0.708 ValAcc=0.622 TrnLoss=1.087 ValLoss=1.351
  * 24%|#9      | 49/200 [1:00:06<3:04:41, 73.39s/ep] TrnAcc=0.682 ValAcc=0.641 TrnLoss=1.144 ValLoss=1.378
  * 20%|##      | 41/200 [52:09<3:24:03, 77.00s/ep] TrnAcc=0.691 ValAcc=0.628 TrnLoss=1.115 ValLoss=1.331
         terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.525    1.788            0.525    1.774
2          0.570    1.511            0.568    1.506
3          0.560    1.555            0.568    1.547
4          0.618    1.308            0.618    1.301
5          0.575    1.579            0.580    1.548
mean       0.570    1.548            0.572    1.535
std        0.033    0.171            0.033    0.168 

## 2024-05-06-10-47 ResNet() with RandomScale, RandomNoise, FrequencyMask, TimeMask
* num_workers = 2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 24%|#9      | 49/200 [1:01:21<3:07:51, 74.65s/ep] TrnAcc=0.616 ValAcc=0.613 TrnLoss=1.368 ValLoss=1.464 
  * 22%|##2     | 44/200 [53:00<3:10:17, 73.19s/ep] TrnAcc=0.600 ValAcc=0.600 TrnLoss=1.390 ValLoss=1.521 
  * 26%|##1     | 53/200 [1:04:00<2:57:42, 72.53s/ep] TrnAcc=0.670 ValAcc=0.575 TrnLoss=1.213 ValLoss=1.592 
  * 26%|##      | 51/200 [1:04:22<3:04:06, 74.13s/ep] TrnAcc=0.623 ValAcc=0.588 TrnLoss=1.309 ValLoss=1.444
  * 32%|##6     | 65/200 [1:22:40<2:53:01, 76.90s/ep] TrnAcc=0.673 ValAcc=0.637 TrnLoss=1.142 ValLoss=1.340
           terminal.pt          best_val_loss.pt         
           TestAcc TestLoss          TestAcc TestLoss
1          0.522    1.857            0.527    1.854
2          0.502    1.832            0.505    1.839
3          0.477    1.826            0.490    1.782
4          0.590    1.360            0.600    1.364
5          0.542    1.634            0.555    1.622
mean       0.527    1.702            0.536    1.692
std        0.043    0.211            0.044    0.205

## 2024-05-06-15-04 ResNet18() with reduced parameters for RandomNoise, FrequencyMask, TimeMask 
* num_workers = 2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 30%|##3     | 59/200 [1:13:48<2:50:46, 72.67s/ep] TrnAcc=0.715 ValAcc=0.662 TrnLoss=1.035 ValLoss=1.238
  * 26%|##1     | 53/200 [1:05:52<3:02:06, 74.33s/ep] TrnAcc=0.696 ValAcc=0.628 TrnLoss=1.128 ValLoss=1.348
  * 23%|##3       | 46/200 [56:57<3:10:34, 74.25s/ep] TrnAcc=0.752 ValAcc=0.641 TrnLoss=0.919 ValLoss=1.167
  * 22%|##2       | 45/200 [55:19<3:18:08, 76.70s/ep] TrnAcc=0.698 ValAcc=0.628 TrnLoss=1.095 ValLoss=1.320 
  * 24%|##3       | 47/200 [57:03<2:58:17, 69.92s/ep] TrnAcc=0.725 ValAcc=0.669 TrnLoss=0.964 ValLoss=1.198
           terminal.pt               best_val_loss.pt         
           TestAcc TestLoss          TestAcc TestLoss
1          0.568    1.547            0.562    1.538
2          0.588    1.528            0.593    1.528
3          0.593    1.406            0.605    1.370
4          0.642    1.198            0.652    1.198
5          0.603    1.539            0.603    1.531
mean       0.599    1.444            0.603    1.433
std        0.028    0.149            0.032    0.149

## 2024-05-06-16-33 ResNetDropout(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.2
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (20)
  * 28%|##2     | 55/200 [1:11:11<3:07:30, 77.59s/ep] TrnAcc=0.568 ValAcc=0.625 TrnLoss=1.463 ValLoss=1.449
  * 25%|##      | 50/200 [1:05:33<3:17:04, 78.83s/ep] TrnAcc=0.601 ValAcc=0.653 TrnLoss=1.286 ValLoss=1.233
  * 23%|##3       | 46/200 [57:00<3:09:48, 73.95s/ep] TrnAcc=0.558 ValAcc=0.550 TrnLoss=1.486 ValLoss=1.645
  * 23%|##3       | 46/200 [55:55<3:10:52, 74.37s/ep] TrnAcc=0.548 ValAcc=0.597 TrnLoss=1.532 ValLoss=1.523
  * 22%|##2       | 45/200 [56:07<3:07:06, 72.43s/ep] TrnAcc=0.616 ValAcc=0.641 TrnLoss=1.340 ValLoss=1.364
           terminal.pt               best_val_loss.pt
           TestAcc TestLoss          TestAcc TestLoss
1          0.520    1.791            0.525    1.792
2          0.570    1.475            0.583    1.476
3          0.482    1.746            0.485    1.759
4          0.575    1.456            0.575    1.460
5          0.555    1.569            0.570    1.556
mean       0.540    1.608            0.547    1.609
std        0.039    0.154            0.042    0.157

## 2024-05-08-08-27 ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask
* num_workers = 2
* gamma = 0.9
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (30)
  * 77%|######9  | 154/200 [3:11:09<55:46, 72.76s/ep] TrnAcc=0.999 ValAcc=0.887 TrnLoss=0.005 ValLoss=0.477
  * 58%|####   | 117/200 [2:28:48<1:48:42, 78.58s/ep] TrnAcc=1.000 ValAcc=0.834 TrnLoss=0.005 ValLoss=0.738
  * 50%|###5   | 101/200 [2:10:27<2:01:50, 73.85s/ep] TrnAcc=1.000 ValAcc=0.812 TrnLoss=0.006 ValLoss=0.773
  * 48%|###8    | 96/200 [1:58:08<2:09:57, 74.98s/ep] TrnAcc=0.997 ValAcc=0.806 TrnLoss=0.016 ValLoss=0.878
  * 53%|###7   | 106/200 [2:11:32<1:58:17, 75.51s/ep] TrnAcc=0.998 ValAcc=0.869 TrnLoss=0.011 ValLoss=0.625 
           terminal.pt               best_val_loss.pt         
           TestAcc TestLoss          TestAcc TestLoss
1          0.823    0.848            0.802    0.817
2          0.772    1.075            0.760    1.105
3          0.752    1.084            0.745    1.115
4          0.828    0.727            0.818    0.711
5          0.745    1.042            0.750    0.973
mean       0.784    0.955            0.775    0.944
std        0.039    0.160            0.033    0.178

## 2024-05-09-07-58 ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask & Dropout
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.9
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (30)
  * 53%|###7   | 106/200 [2:09:53<1:53:54, 72.71s/ep] TrnAcc=0.998 ValAcc=0.853 TrnLoss=0.013 ValLoss=0.573
  * 64%|####4  | 127/200 [2:37:25<1:27:57, 72.30s/ep] TrnAcc=0.998 ValAcc=0.825 TrnLoss=0.010 ValLoss=0.758
  * 45%|###6    | 90/200 [1:49:35<2:19:47, 76.25s/ep] TrnAcc=0.996 ValAcc=0.819 TrnLoss=0.021 ValLoss=0.724
  * 84%|#######5 | 167/200 [3:24:57<38:28, 69.96s/ep] TrnAcc=1.000 ValAcc=0.822 TrnLoss=0.006 ValLoss=0.704
  * 57%|###9   | 114/200 [2:21:06<1:49:26, 76.36s/ep] TrnAcc=0.999 ValAcc=0.856 TrnLoss=0.007 ValLoss=0.627 
           terminal.pt               best_val_loss.pt         
           TestAcc TestLoss          TestAcc TestLoss
1          0.772    1.010            0.740    1.010
2          0.780    1.019            0.790    0.939
3          0.777    1.072            0.740    1.143
4          0.873    0.513            0.845    0.595
5          0.772    1.085            0.770    1.027
mean       0.795    0.940            0.777    0.943
std        0.043    0.241            0.044    0.208

## 2024-05-27-22-39 ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask & Dropout
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.9
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (30)
  * 78%|#####4 | 155/200 [3:26:53<1:01:44, 82.33s/ep] TrnAcc=1.000 ValAcc=0.856 TrnLoss=0.005 ValLoss=0.597
  * 50%|###5   | 101/200 [2:16:02<2:11:52, 79.93s/ep] TrnAcc=0.998 ValAcc=0.809 TrnLoss=0.017 ValLoss=0.775 
  * 46%|###6    | 91/200 [2:04:07<2:28:45, 81.89s/ep] TrnAcc=0.997 ValAcc=0.831 TrnLoss=0.018 ValLoss=0.677 
  * 66%|####5  | 131/200 [2:51:36<1:29:11, 77.55s/ep] TrnAcc=1.000 ValAcc=0.806 TrnLoss=0.006 ValLoss=0.751
  * 60%|####2  | 121/200 [2:29:04<1:34:25, 71.71s/ep] TrnAcc=0.999 ValAcc=0.828 TrnLoss=0.007 ValLoss=0.699 
     terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.785    0.943            0.802    0.923
2          0.770    1.048            0.760    1.039
3          0.740    1.119            0.750    1.118
4          0.835    0.608            0.830    0.634
5          0.733    1.081            0.760    1.019
mean       0.772    0.960            0.780    0.947
std        0.041    0.207            0.034    0.188

## 2024-05-28-12-58 ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask & Dropout
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.9
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* Early stopping (30)
  * 52%|###6   | 105/200 [2:11:11<1:56:29, 73.58s/ep] TrnAcc=0.998 ValAcc=0.841 TrnLoss=0.016 ValLoss=0.724 
  * 44%|###5    | 89/200 [1:54:28<2:20:58, 76.20s/ep] TrnAcc=0.994 ValAcc=0.831 TrnLoss=0.028 ValLoss=0.725 
  * 48%|###8    | 95/200 [1:59:57<2:16:45, 78.15s/ep] TrnAcc=0.998 ValAcc=0.803 TrnLoss=0.015 ValLoss=0.751
  * 52%|###6   | 105/200 [2:11:51<2:01:50, 76.95s/ep] TrnAcc=0.999 ValAcc=0.803 TrnLoss=0.010 ValLoss=0.759 
  * 55%|###8   | 110/200 [2:17:37<1:52:05, 74.73s/ep] TrnAcc=0.999 ValAcc=0.869 TrnLoss=0.010 ValLoss=0.660
     terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.752    1.146            0.807    0.837
2          0.780    0.949            0.785    0.872
3          0.760    1.044            0.765    1.022
4          0.853    0.631            0.825    0.645
5          0.772    1.086            0.752    1.053
mean       0.783    0.971            0.787    0.886
std        0.040    0.203            0.030    0.164

## 2024-05-29-18-47 ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes) with reduced parameters for RandomNoise, FrequencyMask, TimeMask & Dropout
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.9
* optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)
* val size = 0.1
* Early stopping (40)
  * 44%|###5    | 88/200 [1:48:35<2:16:35, 73.17s/ep] TrnAcc=0.994 ValAcc=0.831 TrnLoss=0.029 ValLoss=0.766 
  * 72%|#####  | 143/200 [3:05:20<1:16:08, 80.16s/ep] TrnAcc=0.999 ValAcc=0.850 TrnLoss=0.007 ValLoss=0.596
  * 72%|#####  | 144/200 [3:12:25<1:09:48, 74.79s/ep] TrnAcc=1.000 ValAcc=0.844 TrnLoss=0.006 ValLoss=0.512 
  * 86%|#######7 | 173/200 [3:43:31<36:35, 81.32s/ep] TrnAcc=1.000 ValAcc=0.856 TrnLoss=0.003 ValLoss=0.512
  * 
terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.795    0.908            0.785    0.887
2          0.790    0.848            0.790    0.838
3          0.787    0.960            0.815    0.876
4          0.870    0.537            0.850    0.575
5          0.782    1.040            0.772    1.035
mean       0.805    0.859            0.802    0.842
std        0.037    0.193            0.031    0.167
