import torch

### Lab02 Problem 1
### Linear Regression - single variable
### For given x_train(x) and label(y), perform linear regression.
### Assume y = wx + b

def train(x_train, label):
    ### Implement from here ###
    w = torch.tensor([0.], requires_grad = True)
    b = torch.tensor([1.], requires_grad = True)
    return w, b

if __name__=="__main__":
    x_train = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0])
    label = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])
    x_test = torch.tensor([5.0, 10.0, 8.0])
    
    w, b = train(x_train, label)
    print("weight : " + str(w) + ", bias : " + str(b))
    
    y = w * x_test + b
    print("Predicted value : " + str(y))

    answer = torch.tensor([12, 22, 18])
    print("Actual value : " + str(answer))
