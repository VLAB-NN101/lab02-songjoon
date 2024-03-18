import torch
import pandas as pd

### Lab02 Problem 2
### Multiple Linear Regression - multiple variable
### For given x_train(Hours, PrevStudy, Sleep, Sample) and label(Perf), perform linear regression.
### Assume y = wx + b

def train(Hours,PrevStudy,Sleep,Sample,Perf):
    ### 2) Implement here ###

    w = torch.tensor([0.])
    b = torch.tensor([0.])
    return w,b 

def main():
    PATH = "~/Testcase/Lab02/Problem2/"
    data = pd.read_csv(PATH+'Student_Performance.csv')

    ### 1) Implement here ###
    Hours = None
    PrevStudy = None
    Sleep = None
    Sample = None
    Perf = None      # label
    x_test = torch.FloatTensor([7,99,9,1])
    
    w,b = train(Hours,PrevStudy,Sleep,Sample,Perf) 
    print("weight : " + str(w) + ", bias : " + str(b))
    
    y = torch.dot(w,x_test) + b
    print("Predicted value : " + str(y))
    
    answer = torch.tensor([91])
    print("Actual value : " + str(answer))
    
    return y

main()
