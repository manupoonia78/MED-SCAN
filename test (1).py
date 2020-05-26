import os 
directory = "GeeksforGeek"
parent_dir = "C:\\Users\\Laptop\\Desktop"

path = os.path.join(parent_dir, directory) 

os.mkdir(path) 

from pdf2image import convert_from_path

pages = convert_from_path('TDA.pdf',500)
j=1;

for page in pages:
    page.save((path+'\\'+str(j)+'.jpg'),'JPEG')
    j+=1
    
