import torch

class MyTensor(list):
    pass

print(torch.Tensor([1, 2, 3]) + torch.Tensor([4, 5, 6]))
print(MyTensor([1, 2, 3]) + MyTensor([4, 5, 6]))
