import cv2
import numpy as np
import os

# Input and output folders
input_dir = "cropped_images"
output_dir = "clahe_images"
os.makedirs(output_dir, exist_ok=True)

def apply_clahe(image):
    # Create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    
    # Apply the CLAHE algorithm to the image
    clahe_image = clahe.apply(image)
    
    return clahe_image

for video_folder in os.listdir(input_dir):
    video_folder_path = os.path.join(input_dir, video_folder)
    
    output_folder = os.path.join(output_dir, video_folder)
    os.makedirs(output_folder, exist_ok=True)
    
    for img_file in os.listdir(video_folder_path):
        if img_file.endswith(".png"):
            img_path = os.path.join(video_folder_path, img_file)
            
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            clahe_img = apply_clahe(img)
            
            output_path = os.path.join(output_folder, img_file)
            cv2.imwrite(output_path, clahe_img)
            
print("Finish processing")         



