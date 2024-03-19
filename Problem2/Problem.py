import torch

### Lab02 Problem 2
### Multiple Linear Regression - multiple variable
### For given x_train(x1,x2,...) and label(y), perform linear regression.
### Assume y = wx + b

def train(x_train, label):
    ### Implement from here ###
    w = torch.tensor([0.,0.])
    b = torch.tensor([0.])
    return w,b 

if __name__=="__main__":
    x_train = torch.tensor([[0., 1.], [1., 0.], [2., 2.], [3., 1.], [4., 3.]])
    label = torch.tensor([3., 2., 7., 6., 11.]) 
    
    # y = x_0 + 2*x_1 + 1 # Note that not all test cases give clear line.
    x_test = torch.tensor([[5., 3.], [10., 6.], [8., 9.]])
    
    w,b = train(x_train, label) 
    print("weight : " + str(w) + ", bias : " + str(b))
    
    y = torch.matmul(x_test,w) + b
    print("Predicted value : " + str(y))
    
    answer = torch.tensor([12, 23, 27])
    print("Actual value : " + str(answer))