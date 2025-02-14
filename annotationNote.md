# Annotation method

1. do labelme

SSC:1
Delt:2

only annotate in moving frames

2. create folders

clahe_images <br>
|<br>
|-----No1<br>
|  |<br>
|  |---anno # anno and img files are needed to be same number 
|  |
|  |---img # (if you annotated x to y, frame_x.png to frame_y.png are here
|  |
|  |---images not used
|
|
|
|-----No2
|

3. run jsonToMask.py

you need to change the variables named 'video_No' to match the targeted folder
