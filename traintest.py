import torch
import numpy as np
import numpy as np
import cv2
from torch.utils.data import Dataset
import random

print(torch.__version__)  # PyTorchのバージョン
print(torch.version.cuda) # CUDAのバージョン
print(torch.backends.cudnn.version())  # cuDNNのバージョン

class ultrasoundDataset(Dataset):
    def __init__(self, image_paths, mask_paths, transform=True):
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.transform = transform
        
    def __len__(self):
        return len(self)
    
    def speckle_noise(self, img, gamma_shape=1.5, gamma_scale=0.5):
        noise = np.random.gamma()