Model training / testing results will be saved  in this folder.

### final_submission: ResNet(block=ResidualBlock, layers=[2, 2, 2, 2], num_classes=config.n_classes)
* num_workers = 2
* dropout_rate = 0.2
* gamma = 0.95
* optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
* val_size = 0.02


               terminal.pt               best_val_loss.pt         
               TestAcc TestLoss          TestAcc TestLoss
    1          0.815    1.022            0.718    1.292
    2          0.810    1.126            0.750    1.398
    3          0.815    1.094            0.787    1.159
    4          0.848    0.640            0.845    0.676
    5          0.797    1.066            0.780    1.036
    mean       0.817    0.990            0.776    1.112
    std        0.018    0.199            0.047    0.280