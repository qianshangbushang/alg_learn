import torch


def accuracy(y_pred:torch.Tensor, y_true:torch.Tensor):
    return torch.mean((y_pred.argmax(dim=1) == y_true).float()).item()


if __name__ == "__main__":
    y_pred = torch.rand([5, 4])
    y_true = torch.randint(0, 4, [5,])
    print(y_pred)
    print(y_true)
    print(accuracy(y_pred, y_true))