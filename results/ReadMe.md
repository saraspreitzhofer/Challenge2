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
* Early stopping
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
* Early stopping 
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
* Early stopping 
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
* Early stopping 
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
* dropout_rate = 0.2
* gamma = 0.2
* Early stopping 
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
* dropout_rate = 0.2
* gamma = 0.2
* Early stopping
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
* dropout_rate = 0.2
* gamma = 0.2
* Early stopping 
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