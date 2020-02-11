# ROI_extraction_cv2
Code for manually extract ROI on images, save data on a .csv file, save image crop or draw rectangle om image.

## How to use the code?

In the same directory as the ROI.py file, create a folder where you will save the .csv file and the cropped images.

## CSV file description

Create a csv file with the following header: file, originalHeight, originalWidth, interpolation, resizedHeight, resizedWidth, x1, y1, width, height:

1) file will be the name of the image;
2) originalHeight and originalWidth will be the original dimensions of the image;
3) interpolation will be the method apllyed on the resize (In my case I used 'INTER_AREA');
4) resizedHeight and resizedWidth will be the resized dimensions of the image (In my case, I divided the original dimensions by 4);
5) x1 and y1 will be the location of the upper left point of ROI;
6) width, height will be the dimensions of the ROI, starting from x1 and y1 on resized image.

## Changing paths on code...
In line 6, change 'YOUR CODE DIRECTORY PATH HERE ...' to the path to the folder where the images are located;

On line 11, in 'YOUR .CSV PATH HERE ...', put the path of the .csv file;

On line 40, change the text 'YOUR DIRECTORY PATH FOR NEW IMAGES HERE ...' to the path of the folder where you want to save the new cropped images. Do not change '\ {files} Image.jpg' so that the image has the same caption as the original image;

In line 33, the code for drawing the rectangle in the image is commented out. Uncomment to use it.
