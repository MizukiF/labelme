import cv2

# 画像を表示しながらクロップ範囲を決める
image_path = "image_files/No1/frame_001.png"  # 確認したい画像を指定
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: 画像が読み込めませんでした")
    exit()

# ウィンドウを作成して画像を表示
cv2.imshow("Select Crop Area", image)

# マウスクリックで座標を取得する関数
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 左クリックで座標取得
        print(f"Clicked at: x={x}, y={y}")

# マウスイベントを設定
cv2.setMouseCallback("Select Crop Area", click_event)

# 画像を表示し続ける
cv2.waitKey(0)
cv2.destroyAllWindows()