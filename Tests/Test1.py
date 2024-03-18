import Problem1
import torch

if __name__=="__main__":
    error = 1e-2
    answer = torch.tensor([12,22,18])
    assert(all(abs(answer - Problem1.main()) < error))        
