import json
import numpy as np
import cv2
import os

# Set directory
video_No = 17
annotation_dir = f"C:/Users/mizuk/Desktop/Study/labelme/clahe_images/No{video_No}/anno"
mask_dir = f"C:/Users/mizuk/Desktop/Study/labelme/clahe_images/No{video_No}/mask"
os.makedirs(mask_dir, exist_ok=True)

# Get json information
json_files = [f for f in os.listdir(annotation_dir) if f.endswith(".json")]

for json_file in json_files:
    json_path = os.path.join(annotation_dir, json_file)
    
    # open json file
    with open(json_path, "r") as f:
        data = json.load(f)
        
    # get image size
    img_height = data["imageHeight"]
    img_width = data["imageWidth"]
    mask = np.zeros((img_height, img_width), dtype=np.uint8)
    
    # translate porigon to mask
    for shape in data["shapes"]:
        points = np.array(shape["points"], dtype=np.int32)
        cv2.fillPoly(mask, [points], color=255)
    
    # save masks
    mask_filename = json_file.replace(".json", "_mask.png")
    mask_path = os.path.join(mask_dir, mask_filename)
    cv2.imwrite(mask_path, mask)
    
print("finish all tasks")