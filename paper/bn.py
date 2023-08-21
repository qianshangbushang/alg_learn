# batch normalization
# 处于全连接和激励函数之间
"""
算法步骤
 1. 先求数据均值
 2. 再求数据方差
 3. 归一化/标准化
 前三者称为标准化工序，后者称为反标准化
 4. 放大和偏移
"""
import torch


def batch_norm(is_training, X: torch.Tensor, gamma, beta, moving_mean, moving_var, eps, momentum):
    if not is_training:
        X_hat = (X - moving_mean) / torch.sqrt(moving_var + eps)
    else:
        assert len(X.shape) in (2, 4)

        if len(X.shape) == 2:
            mean = X.mean(dim=0)
            var = ((X - mean) ** 2).mean(dim=0)
        else:
            mean = X.mean(dim=0, keepdim=True).mean(dim=2, keepdim=True).mean(dim=3, keepdim=True)
            var = ((X - mean) ** 2).mean(dim=0, keepdim=True).mean(dim=2, keepdim=True).mean(dim=3, keepdim=True)

        X_hat = (X - mean) / torch.sqrt(var + eps)

        moving_mean = momentum * moving_mean + (1 - momentum) * mean
        moving_var = momentum * moving_var + (1 - momentum) * var

    Y = gamma * X_hat + beta
    return Y, moving_mean, moving_var


class BatchNorm(torch.nn.Module):
    def __init__(self, num_features, num_dims) -> None:
        super().__init__()
        if num_dims == 2:
            shape = (1, num_features)
        else:
            shape = (1, num_features, 1, 1)

        self.gamma = torch.nn.parameter.Parameter(torch.ones(shape))
        self.beta = torch.nn.parameter.Parameter(torch.zeros(shape))

        self.moving_mean = torch.zeros(shape)
        self.moving_var = torch.zeros(shape)
        return

    def forward(self, X: torch.Tensor):
        if self.moving_mean.device != X.device:
            self.moving_mean.to(X.device)
            self.moving_var.to(X.device)

        Y, self.moving_mean, self.moving_var = batch_norm(self.training, X, self.gamma, self.beta,
                                                          self.moving_mean, self.moving_var, eps=1e-05, momentum=0.9)
        return Y
