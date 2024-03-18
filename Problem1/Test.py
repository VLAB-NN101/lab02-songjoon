import Problem1.Problem as Problem
import torch

if __name__=="__main__":
    error = 1e-2
    answer = torch.tensor([12,22,18])
    assert(all(abs(answer - Problem.main()) < error))        
