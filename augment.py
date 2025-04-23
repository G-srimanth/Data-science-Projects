import os
import cv2
import numpy as np
from ultralytics.data.augment import RandomHSV,RandomFlip,Compose,CopyPaste
def flipud(image_path,label_path,output_img_path=os.getcwd(),output_lab_path=os.getcwd()):
    if image_path:
        image_name=image_path.split('/')[-1]
        label_name=label_path.split('/')[-1]
        print(image_name,label_name)

        flipud_img_name=image_name.replace(image_name.split('.')[0],str('ud_'+image_name.split('.')[0]))
        flipud_lab_name=label_name.replace(label_name.split('.')[0],str('ud_lab'+label_name.split('.')[0]))
        print(flipud_img_name,flipud_lab_name)
        output_img_path+="/"+flipud_img_name
        output_lab_path+="/"+flipud_lab_name
        image_arr=cv2.imread(image_path)
        flip_img_arr=cv2.flip(image_arr,0)
        cv2.imwrite(output_img_path,flip_img_arr)
        with open(label_path,'r') as file:
            data = file.readlines()
        output_lines=[]w
        for line in data:
            parts=line.strip().split()
            cls_id=parts[0]
            coords=list(map(float,parts[1:]))
            new_cords=np.array([[coords[i],round(1.0-coords[i+1],3)] for i in range(0,len(coords),2)]).flatten()
            new_line=f'{cls_id} '+' '.join(list(map(str,new_cords)))
            output_lines.append(new_line)
        with open(output_lab_path,'w') as wfile:
            wfile.write('\n'.join(output_lines))

def fliplr(image_path,label_path,output_img_path=os.getcwd(),output_lab_path=os.getcwd()):
    if image_path:
        image_name=image_path.split('/')[-1]
        label_name=label_path.split('/')[-1]
        print(image_name,label_name)

        fliplr_img_name=image_name.replace(image_name.split('.')[0],str('lr_'+image_name.split('.')[0]))
        fliplr_lab_name=label_name.replace(label_name.split('.')[0],str('lr_lab'+label_name.split('.')[0]))
        print(fliplr_img_name,fliplr_lab_name)
        output_img_path+="/"+fliplr_img_name
        output_lab_path+="/"+fliplr_lab_name
        image_arr=cv2.imread(image_path)
        flip_img_arr=cv2.flip(image_arr,1)
        cv2.imwrite(output_img_path,flip_img_arr)
        with open(label_path,'r') as file:
            data = file.readlines()
        output_lines=[]
        for line in data:
            parts=line.strip().split()
            cls_id=parts[0]
            coords=list(map(float,parts[1:]))
            new_cords=np.array([[round(1-coords[i],3),coords[i+1]] for i in range(0,len(coords),2)]).flatten()
            new_line=f'{cls_id} '+' '.join(list(map(str,new_cords)))
            output_lines.append(new_line)
        with open(output_lab_path,'w') as wfile:
            wfile.write('\n'.join(output_lines))

def hsv()







            


                #cv2.fillPoly(flip_image_arr,pts=pts.reshape(-1,1,2),color=255)
        # cv2.imshow('poly',flip_image_arr)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    #print(len(flip_lines))
# def fliplr(image_path,label_path,output_img_path=os.getcwd(),output_lab_path=os.getcwd()):
#     if image_path:
#         image_arr=cv2.imread(image_path)
#         image_name=image_path.split('/')[-1].split('.')[0]+'.png'
#         flip_image_arr=cv2.flip(image_arr,1)
#         flip_image_name=f'ud_{image_name}'
#         flip_label_name=f'/ud_{image_name.replace(".png",".txt")}'
#         print(output_img_path+'/'+flip_image_name,len(image_arr))
#         cv2.imwrite(output_img_path+"/"+flip_image_name,flip_image_arr)
#         h,w,_=image_arr.shape
#         #flip_lines=[]
#         with open(label_path,'r') as file:
#             for line in file:
#                 parts=line.split()
#                 cls_ids = parts[0]
#                 coords = list(map(float,parts[1:]))
#                 pts = np.array([[int(coords[i]*w) , int(coords[i+1]*h)] for i in range(0,len(coords),2)])
#                 pts[:, 0] = h - pts[:, 0]
#                 norm_pts=(np.round(pts/[w,h],3).flatten())
#                 label_line=f'{cls_ids} '+' '.join(list(map(str,norm_pts)))
#                 with open(output_lab_path+flip_label_name,'w') as w:
#                     w.write(label_line+'\n')

fliplr('images/train/images.jpeg','labels/train/images.txt')
print(os.getcwd())

                

                

