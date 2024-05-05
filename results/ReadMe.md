Model training / testing results will be saved  in this folder.

## sample-run
* ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes)
* TestAcc=0.703

## 2024-05-01-16-09
* ResNet(block=ResidualBlock, layers=[3, 4, 6, 3], num_classes=config.n_classes)
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

## 2024-05-05-13-16
* CNN()
* num_workers = 2
* Early stopping 
  * 27%|##7       | 54/200 [53:05<2:23:32, 58.99s/ep] TrnAcc=0.045 ValAcc=0.034 TrnLoss=3.901 ValLoss=3.912 
  * 10%|#         | 21/200 [20:31<2:54:56, 58.64s/ep] TrnAcc=0.034 ValAcc=0.031 TrnLoss=3.911 ValLoss=3.915
  * 14%|#3        | 27/200 [26:54<2:56:47, 61.31s/ep] TrnAcc=0.016 ValAcc=0.016 TrnLoss=3.929 ValLoss=3.930 
  * 11%|#1        | 22/200 [21:37<2:55:00, 58.99s/ep] TrnAcc=0.037 ValAcc=0.013 TrnLoss=3.908 ValLoss=3.933 
  * 10%|#         | 21/200 [20:37<2:55:44, 58.91s/ep] TrnAcc=0.037 ValAcc=0.034 TrnLoss=3.909 ValLoss=3.911 
terminal.pt
    TestAcc  TestLoss
1       0.060     3.886
2       0.030     3.917
3       0.013     3.933
4       0.040     3.905
5       0.045     3.898
mean    0.037     3.908
std     0.018     0.018