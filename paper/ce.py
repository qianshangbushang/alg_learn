import torch

def cross_entropy(y_pred:torch.Tensor, y_label:torch.Tensor):
    return -torch.log(y_pred.gather(1, y_label.view(-1, 1)))



if __name__ == "__main__":
    y_pred = torch.rand([8, 5])
    y_label = torch.randint(0, 5, [8, 1])
    print(y_pred)
    print(y_label)
    print(cross_entropy(y_pred, y_label))