import torch
import pandas as pd


def train(Hours,PrevStudy,Sleep,Sample,Perf):
    ### 2) Implement here ###


    return w,b 

def main():
    data = pd.read_csv('./Student_Performance.csv')

    ### 1) Implement here ###
    Hours = None
    PrevStudy = None
    Sleep = None
    Sample = None
    Perf = None
    x_test = torch.FloatTensor([7,99,9,1])
    
    w,b = train(Hours,PrevStudy,Sleep,Sample,Perf) 
    
    y = torch.dot(w,x_test) + b
    return y

main()
