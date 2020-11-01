import torch
t1 = torch.tensor(4.)
print(t1)

print(t1.dtype)

t2 = torch.tensor(4.5)
print(t2.dtype)

t3= torch.tensor([1, 2,3 ,4])
print(t3)

t4 = torch.tensor([[1,3,3],
                  [1,2,3]])
print(t4)

t5 = torch.tensor([
    [[11, 12, 13],
     [13, 14, 15]],
    [[15, 16, 17],
     [17, 18, 19.]]])
print(t5.size())



#############################################################################
# hear we have create a three variable with two computed derivatives#


x = torch.tensor(3.)
w = torch.tensor(4. , requires_grad= True)
b = torch.tensor(5. , requires_grad= True)
y= w * x +b

# print(y.backward)

#  displaying gradients #

print( x.grad)
print( w.grad)
print( x.grad)


import numpy as np

g = np.array([[1, 2 ],
              [2, 3]])

t6 = torch.from_numpy(g)
print(t6.dtype)
print(g.dtype)

z= t6.numpy()
print(z)


print(torch.__version__)