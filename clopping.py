import cv2
import numpy as np
import os

x, y, w, h = 250, 140, 780, 690

# Input and output folders
input_dir = "image_files"
output_dir = "cropped_images"
os.makedirs(output_dir, exist_ok=True)

for video_folder in os.listdir(input_dir):
    video_folder_path = os.path.join(input_dir, video_folder)
    
    output_folder = os.path.join(output_dir, video_folder)
    os.makedirs(output_folder, exist_ok=True)
    
    for img_file in os.listdir(video_folder_path):
        if img_file.endswith(".png"):
            img_path = os.path.join(video_folder_path, img_file)
            
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            cropped_image = img[y:y+h, x:x+w]
            
            output_path = os.path.join(output_folder, img_file)
            cv2.imwrite(output_path, cropped_image)

        
print("Finish processing")