import cv2

# 画像パス（任意の画像を指定）
image_path = "image_files/No1/frame_001.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: 画像が読み込めませんでした")
    exit()

# クロッピング領域を試しに設定（クリックで取得した座標を入力）
x, y, w, h = 250, 140, 780, 690  # ここを変更しながら調整

# クロッピング
cropped_image = image[y:y+h, x:x+w]

# 元画像とクロップ画像を並べて表示
cv2.imshow("Original", image)
cv2.imshow("Cropped", cropped_image)

# キーを押すまで表示
cv2.waitKey(0)
cv2.destroyAllWindows()