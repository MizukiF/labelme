import os


output_dir = "mask_folder"
os.makedirs(output_dir, exist_ok=True)

for i in range(142):
    video_folder = f"Mask_No_{i+1}"
    output_folder = os.path.join(output_dir, video_folder)
    os.makedirs(output_folder, exist_ok=True)
    
print("Fnish")