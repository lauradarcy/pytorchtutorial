from __future__ import print_function
import torch

print('torch.empty')
x = torch.empty(5,3)
print(x)

print('\ntorch.rand')
x = torch.rand(5,3)
print(x)

print('\ntorch.zeros')
x = torch.zeros(5,3, dtype=torch.long)
print(x)

print('\ntorch.tensor')
x = torch.tensor([5.5,3])
print(x)

print('\nx.new_ones')
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

print('\nx=torch.rand_like')
x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)                                      # result has the same size

print('\nx.size()')
print(x.size())

print('\ny=torch.rand')
y = torch.rand(5, 3)
print(x + y)

print('\ntorch.add(x,y)')
print(torch.add(x, y))

print('\nresult=torch.empty(5,3)\ntorch.add(x, y, out=result)')
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

print('\ny.add_(x)')
# adds x to y
y.add_(x)
print(y)

print('\n print x')
print(x)
print('\nprint(x[:,1])')
print(x[:,1])