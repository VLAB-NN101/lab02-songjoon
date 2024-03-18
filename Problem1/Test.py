import Problem1.Problem as Problem
import torch
import csv
import sys

PATH = "~/Testcase/Lab02/Problem1/"
def getAddress(x):
    return PATH + "ex" + str(x) + ".csv"

if __name__=="__main__":
    ## need to implement grading code
    ## test run example : ./Test.py 1
    with open(getAddress(sys.argv[1]), "r") as f:
        rdr = csv.reader(f)
        arr = [line for line in rdr][1:]

        train_data = arr[:-3]
        test_data = arr[-3:]

        ## process torch.Tensor and make comparsion
        ## Answer should be < 1% relative error.