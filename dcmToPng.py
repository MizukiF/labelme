import os
import pydicom
import numpy as np
import cv2

# Directory of video files
dicom_dir = "video_files"

# Directory of output images
output_dir = "image_files"

# Create an output folder
os.makedirs(output_dir, exist_ok=True)

# Process the DICOM files transfering to png
for dicom_file in os.listdir(dicom_dir):
    if dicom_file.endswith(".dcm"):
        dicom_path = os.path.join(dicom_dir, dicom_file)
        dicom_name = os.path.splitext(dicom_file)[0] # "No1.dcm" -> "No1"
        
        # Create folders for each sample (No1, No2 .... NoX)
        output_folder = os.path.join(output_dir, dicom_name)
        os.makedirs(output_folder, exist_ok=True)
        
        # Load DICOM files
        dicom_data = pydicom.dcmread(dicom_path)
        
        # Get frames
        frames = dicom_data.pixel_array # [num_frames, hight, width]
        
        # Save frames as images
        for i, frame in enumerate(frames):
            frame_filename = f"frame_{i+1:03d}.png"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)
            
print("Finish the processing")