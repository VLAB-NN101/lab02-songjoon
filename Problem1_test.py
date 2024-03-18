import Problem1_answer
import torch

def test_Problem1():
    error = 1e-2
    answer = torch.tensor([12,22,18])
    assert(all(abs(answer - Problem1_answer.main()) < error))        
