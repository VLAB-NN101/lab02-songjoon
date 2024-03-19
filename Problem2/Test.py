import Problem 
import torch
import csv
import sys
import numpy as np

PATH = "/home/runner/Testcase/Lab02/Problem2/"

def getAddress(x):
    return PATH + "ex" + str(x) + ".csv"

if __name__ == "__main__":
    ## need to implement grading code
    ## test run example : ./Test.py 1
    num = sys.argv[1]
    with open(getAddress(num), "r") as f:
        rdr = csv.reader(f)
        arr = [line for line in rdr][1:]

        train_data = arr[:-3]
        test_data = arr[-3:]
            
        ## process torch.Tensor and make comparsion
        ## Answer should be < 1% relative error.
        datalen = len(arr[0])- 1
        train_tensor = torch.FloatTensor(np.float_(train_data))
        x_train = train_tensor[:,0:datalen]
        train_label = train_tensor[:,datalen]
        w, b = Problem.train(x_train,train_label)
            
        test_tensor = torch.FloatTensor(np.float_(test_data))
        x_test = test_tensor[:,0:datalen]
        test_label = test_tensor[:,datalen]
        
        y = torch.matmul(x_test,w)+b
        
        error = 1e-1 * test_label

        assert(all(abs(test_label - y) < error)) 