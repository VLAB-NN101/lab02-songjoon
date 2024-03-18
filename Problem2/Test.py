import Problem2.Problem as Problem
import torch
import csv
import sys

PATH = "~/Testcase/Lab02/Problem2/"
def getAddress():
    return PATH + "Student_Performance.csv"

if __name__=="__main__":
    ## need to implement grading code
    ## test run example : ./Test.py 1
    with open(getAddress(), "r") as f:
        rdr = csv.reader(f)
        arr = [line for line in rdr][1:]

        train_data = arr[:-3]
        test_data = arr[-3:]

        ## process torch.Tensor and make comparsion
        ## Answer should be < 1% relative error.