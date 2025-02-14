import os
import cv2
import pydicom
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Preprocessing function
def prepro(image):
    x, y, w, h = 195, 150, 890, 680
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    
    # Crop the region of interest
    cropped_image = image[y:y+h, x:x+w]
    
    # Scale to 8-bit if necessary
    if cropped_image.dtype != np.uint8:
        cropped_image = cv2.normalize(cropped_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # CLAHE expects a single-channel grayscale image
    if len(cropped_image.shape) != 2:  # Ensure the image is single-channel
        cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    filtered_image = cv2.GaussianBlur(cropped_image, (5, 5), 0)
    
    # Apply CLAHE
    clahe_image = clahe.apply(filtered_image)
    return clahe_image

# File selection dialog
def select_file():
    Tk().withdraw()  # Hide main Tkinter window
    file_path = askopenfilename(
        title="Select a DICOM file",
        filetypes=[("DICOM Files", "*.dcm"), ("All Files", "*.*")]
    )
    return file_path

# Main function
def process_dicom_to_video():
    # Select DICOM file
    path = select_file()
    if not path:
        print("No file selected.")
        return
    
    # Load DICOM file
    dcm = pydicom.dcmread(path)
    
    # Extract the number of frames
    if hasattr(dcm, 'NumberOfFrames'):
        frame_count = int(dcm.NumberOfFrames)
        print(f"This file contains {frame_count} frames.")
    else:
        frame_count = 1
        print("This is a static image file.")
    
    # Get pixel data
    pixel_data = dcm.pixel_array
    
    # Get FPS
    fps = 30  # Default FPS
    if hasattr(dcm, 'FrameTime'):  # If frame time is available
        frame_time = float(dcm.FrameTime)  # FrameTime in milliseconds
        fps = int(1000 / frame_time)
    print(f"FPS is {fps}")
    
    # Set output file name
    base_name = os.path.basename(path)
    name, ext = os.path.splitext(base_name)
    output_filename = f"{name}_processed.mp4"
    
    # Define video export settings
    height, width = 680, 890  # Cropped dimensions
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Use mp4v codec
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height), isColor=True)
    
    # Process each frame
    for i in range(frame_count):
        frame = pixel_data[i] if frame_count > 1 else pixel_data
        
        # Scale pixel data to 8-bit if necessary
        if frame.dtype != np.uint8:
            frame = (frame / frame.max() * 255).astype(np.uint8)
        
        # Apply preprocessing
        processed_frame = prepro(frame)
        
        # Convert grayscale to BGR for color video
        color_frame = cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2BGR)
        
        # Write to video
        out.write(color_frame)
    
    # Release resources
    out.release()
    print(f"Video saved as {output_filename}")

# Execute the main function
if __name__ == "__main__":
    process_dicom_to_video()
