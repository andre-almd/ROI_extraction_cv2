import cv2
import os
import csv

# Select the directory which the image files are in
dircont = 'YOUR CODE DIRECTORY PATH HERE...'

# Get the list of image files
directory = os.listdir(dircont)

with open('YOUR .CSV PATH HERE...', 'a', newline='\n') as csvFile:
    for files in directory:
        if files.endswith('.jpg') or files.endswith('.JPG'):
            file_path = os.path.join(dircont, files)
            print(file_path)
    
            # Read image
            im = cv2.imread(file_path)
            originalSize = im.shape
            
            # Resize image
            im = cv2.resize(im, (int(im.shape[1]/4), int(im.shape[0]/4)), interpolation=cv2.INTER_AREA)        
            resizedSize = im.shape
            
            # Select ROI in resized image 
            r = cv2.selectROI(im)
            
            # Crop image
            imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
            print(imCrop.shape)
            
            # Make rectangle on image
            #im = cv2.rectangle(im, (r[0],r[1]), (r[0]+r[2], r[1]+r[3]), (0,255,0))
            
            # Display cropped image
            cv2.imshow("Image", imCrop)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            cv2.imwrite(f'YOUR DIRECTORY PATH FOR NEW IMAGES HERE...\{files[:-4]}Image.jpg', imCrop)
            
            # Data for csv file
            dados = [files, originalSize[0], originalSize[1], 'INTER_AREA', resizedSize[0], resizedSize[1], r[0], r[1], r[2], r[3]]
            
            writer = csv.writer(csvFile)
            writer.writerow(dados)
csvFile.close()
        
