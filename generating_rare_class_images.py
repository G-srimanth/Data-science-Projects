import os
import cv2
import numpy as np



images_path='/media/srimanth/A86AB2196AB1E3EA/yolo/images.jpeg'
image=cv2.imread(images_path)
labels_path='/media/srimanth/A86AB2196AB1E3EA/yolo/images.txt'
target_id=1
h,w = image.shape[:-1]




def quality_incresing(cropped):

# === Step 2: Reduce Blur / Denoise ===
    denoised = cv2.fastNlMeansDenoisingColored(cropped, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)

    # === Step 3: Sharpen the Image ===
    sharpen_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])
    sharpened = cv2.filter2D(denoised, -1, sharpen_kernel)

    # === Step 4: Super-Resolution Upscaling (4x using EDSR) ===
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel("EDSR_x4.pb")  # Make sure this file is in your working directory
    sr.setModel("edsr", 4)

    upscaled = sr.upsample(sharpened)
    return upscaled

# === Step 5: Display and Save the Output ===
import cv2
import numpy as np

with open(labels_path, 'r') as f:
    data = f.readlines()

for line in data:
    cls_id = line.split()[0]
    parts = line.split()[1:]
    points = list(map(float, parts))

    # Get original polygon in image scale
    pts = (np.array(points, dtype=np.float32).reshape(-1, 2) * [w, h]).astype(np.int32)
    
    # Get bounding box
    x, y, w1, h1 = cv2.boundingRect(pts)
    cropped = image[y:y+h1, x:x+w1]

    # Offset polygon to cropped space
    pts_cropped = pts - np.array([x, y])

    # Resize image
    image_new = cv2.resize(cropped, dsize=(w, h))

    # Scale polygon points to resized image
    scale_x = w / w1
    scale_y = h / h1
    pts_scaled = (pts_cropped * [scale_x, scale_y]).astype(np.int32).reshape(-1, 1, 2)

    # Draw polygon
    cv2.polylines(image_new, [pts_scaled], isClosed=True, color=(255, 0, 0), thickness=2)

    # Display
    cv2.imshow('object', image_new)
    cv2.waitKey(0)

cv2.destroyAllWindows()


# with open(labels_path,'r') as f:
#     data = f.readlines()

# for line in data:
#     cls_id = line.split()[0]
#     parts= line.split()[1:]
#     points=list(map(float,parts))
#     pts = (np.array(points, dtype=np.float32).reshape(-1, 2) * [w, h]).astype(np.int32).reshape(-1, 1, 2)
#     print(pts)

#     x,y,w1,h1 = cv2.boundingRect(pts)
#     print(x,y,w1,h1)
#     image_new=cv2.resize(image[y:y+h1,x:x+w1],dsize=(h,w))
#     new_polygons=pts-np.array([x+w,y+h])
#     cv2.polylines(image_new,new_polygons,color=(255,0,0),isClosed=True,thickness=4)
#     # new_polygons=
#     # enhanced=quality_incresing(image_new)
#     cv2.imshow('object',image_new)
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
