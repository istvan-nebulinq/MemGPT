import torch

print(torch.cuda.is_available())  # Should print True if your setup is correct
print(torch.cuda.current_device())  # Should print 0 if your GPU is detected
print(torch.cuda.get_device_name(0))  # Should print the name of your GPU
