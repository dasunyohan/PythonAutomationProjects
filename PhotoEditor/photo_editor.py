from PIL import Image, ImageEnhance, ImageFilter
import os

#declaring the input folder and output folder
path = './images'
pathOut = '/editedImages'

#for loop for the input (images) folder
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L') #editing the image 
    
    #Increasing the contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg') #saving the image