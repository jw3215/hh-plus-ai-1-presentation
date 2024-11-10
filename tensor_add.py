import torch

class MyTensor(list):
    def __add__(self, other):
        return MyTensor([a + b for a, b in zip(self, other)])

print(torch.Tensor([1, 2, 3]) + torch.Tensor([4, 5, 6]))
print(MyTensor([1, 2, 3]) + MyTensor([4, 5, 6]))
