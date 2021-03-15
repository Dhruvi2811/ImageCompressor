import PIL
from PIL import Image
import os

mywidth = 2000
source_dir ='C:/Users/admin/Desktop/image'
destination_dir ='C:/Users/admin/Desktop/image1'

def resize_pic(old_pic,new_pic):
    img=Image.open(old_pic)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img=img.resize((mywidth,hsize),PIL.Image.ANTIALIAS)
    img.save(new_pic)

def entire_directory(source_dir,desti_dir):
    files=os.listdir(source_dir)
    i=0
    for file in files:
        i+=1
        old_pic=source_dir + "/" + file
        new_pic=desti_dir + "/" +file
        resize_pic(old_pic,new_pic)
        print(i,"done")

entire_directory(source_dir,destination_dir)