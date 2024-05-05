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
* TestAcc  TestLoss
  * 1       0.623     1.354
  * 2       0.652     1.305
  * 3       0.618     1.412
  * 4       0.672     1.273
  * 5       0.665     1.386
  * mean    0.646     1.346
  * std     0.025     0.057
terminal.pt          best_val_loss.pt         
         TestAcc TestLoss          TestAcc TestLoss
1          0.623    1.354            0.630    1.367
2          0.652    1.305            0.660    1.292
3          0.618    1.412            0.610    1.395
4          0.672    1.273            0.680    1.271
5          0.665    1.386            0.672    1.361
mean       0.646    1.346            0.650    1.337
std        0.025    0.057            0.030    0.053
