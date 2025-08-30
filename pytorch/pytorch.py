# 1404-05-28
# Mohammad Kadkhodaei
# PyTorch in One Hour, by Sebastian Raschka, https://sebastianraschka.com/teaching/pytorch-1h
# ---

import torch
torch.__version__

torch.cuda.is_available()

# create a 0D tensor (scalar) from a Python integer
tensor0d = torch.tensor(1)

# create a 1D tensor (vector) from a Python list
tensor1d = torch.tensor([1, 2, 3])

# create a 2D tensor from a nested Python list
tensor2d = torch.tensor([[1, 2], [3, 4]])

# create a 3D tensor from a nested Python list
tensor3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# device, 1404-06-08
# ---
device = torch.device("cuda")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ---

