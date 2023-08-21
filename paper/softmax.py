from doctest import REPORT_UDIFF
import torch

def softmax(x:torch.Tensor):
    return torch.exp(x) / torch.sum(torch.exp(x), dim=-1, keepdim=True)


if __name__ == "__main__":
    print(softmax(torch.rand([4, 2])))