# 1404-05-28
# Mohammad Kadkhodaei
# PyTorch in One Hour, by Sebastian Raschka, https://sebastianraschka.com/teaching/pytorch-1h
# ---

import torch
torch.__version__
torch.cuda.is_available()

# Scalars, vectors, matrices, and tensors

# create a 0D tensor (scalar) from a Python integer
tensor0d = torch.tensor(1)

# create a 1D tensor (vector) from a Python list
tensor1d = torch.tensor([1, 2, 3])

# create a 2D tensor from a nested Python list
tensor2d = torch.tensor([[1, 2], [3, 4]])

# create a 3D tensor from a nested Python list
tensor3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Tensor data types, dtype, https://docs.pytorch.org/docs/stable/tensors.html
tensor1d = torch.tensor([1, 2, 3])
print(tensor1d.dtype)
floatvec = tensor1d.to(torch.float32)

# device, 1404-06-08
# ---
device = torch.device("cuda")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ---

# A typical training loop
# ---
import torch.nn.functional as F

torch.manual_seed(123)
model = NeuralNetwork(num_inputs=2, num_outputs=2)
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

num_epochs = 3

for epoch in range(num_epochs):

    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):

        logits = model(features)

        loss = F.cross_entropy(logits, labels) # Loss function

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        ### LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d} "f" | Batch {batch_idx:03d}/{len(train_loader):03d} "f" | Train/Val Loss: {loss:.2f}")

    model.eval()
    # Optional model evaluation
# ---


# Saving and loading models, 1404-06-26
torch.save(model.state_dict(), "model.pth")
model.load_state_dict(torch.load("model.pth", weights_only=True))

