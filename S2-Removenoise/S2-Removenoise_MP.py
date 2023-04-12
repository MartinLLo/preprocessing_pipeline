# -*- coding: utf-8 -*-
"""
@author: martin lo

Saving the boolean'd array as pixel_array and pixeldata on the dcm itself
For loop allows the whole directory to be processed
concurrent.futures allows the entire process to be carried out in parallel processes, the number of workers can be set to max or designated number

"""
# Packages required
import pydicom
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import morphology
import concurrent.futures

# Functions required

def transform_to_hu(medical_image, image):
    try:
        intercept = medical_image.RescaleIntercept
    except AttributeError:
        with open("rinterceptc.txt", "a") as rintercept_file:
            rintercept_file.write(str(os.path.abspath(medical_image))+'\n')
            print(os.path.abspath(medical_image) + ' does not have rescale intercept')
        rintercept_file.close()
        pass
    slope = medical_image.RescaleSlope
    hu_image = image * slope + intercept

    return hu_image

def window_image(image, window_center, window_width):
    img_min = window_center - window_width // 2
    img_max = window_center + window_width // 2
    window_image = image.copy()
    window_image[window_image < img_min] = img_min
    window_image[window_image > img_max] = img_max
    
    return window_image

def mask_only(file_path, display=False):
    medical_image = pydicom.read_file(file_path, force=True)
    image = medical_image.pixel_array
    
    hu_image = transform_to_hu(medical_image, image)
    thresholded_image = window_image(hu_image, 40, 80)
    
    segmentation = morphology.dilation(thresholded_image, np.ones((4, 4)))
    labels, label_nb = ndimage.label(segmentation)
    
    label_count = np.bincount(labels.ravel().astype(int))
    label_count[0] = 0

    mask = labels == label_count.argmax()
    
    # Improve the mask
    mask = morphology.dilation(mask, np.ones((1, 1)))
    mask = ndimage.morphology.binary_fill_holes(mask)
    mask = morphology.dilation(mask, np.ones((3, 3)))
    
    masked_image = mask * thresholded_image
    
    if display:
        plt.figure(figsize=(15, 2.5))
        plt.subplot(141)
        plt.imshow(thresholded_image)
        plt.title('Original Image')
        plt.axis('off')
        
        plt.subplot(142)
        plt.imshow(mask)
        plt.title('Mask')
        plt.axis('off')

        plt.subplot(143)
        plt.imshow(masked_image)
        plt.title('Final Image')
        plt.axis('off')       
    print(type(masked_image))
    return mask

def mask_array(file_path, display = False):
    mask = mask_only(file_path, display=False)
    # print(mask)

    # Invert the bool array generated in mask_only function
    inverted_mask = np.logical_not(mask)
    # check inveted_mask array
    # print(inverted_mask)

    # turn inverted_mask into int array
    inverted_mask_int = inverted_mask.astype(int)
    # check inveted_mask_int array
    # print(inverted_mask_int)

    # find minimum value in dcm
    image = pydicom.dcmread(file_path).pixel_array
    minval = np.min(image)

    # replace _int 1s with min_img[0] aka minval
    new_mask = np.where(inverted_mask_int > 0, minval, inverted_mask_int)
    # print(new_mask)
    
    if display:
        plt.figure(figsize=(15, 2.5))
        plt.subplot(141)
        plt.imshow(mask)
        plt.title('Mask')
        plt.axis('off')
        
        plt.subplot(142)
        plt.imshow(new_mask)
        plt.title('new_mask')
        plt.axis('off')  
        
        plt.subplot(143)
        plt.imshow(inverted_mask_int)
        plt.title('inv_mask')
        plt.axis('off')  
    return mask

def boolean_masking(file_path, display=True):
    masking = mask_array(file_path)
    image = pydicom.dcmread(file_path).pixel_array
    n = np.min(masking)
    masking_value = (masking == n)
    image[masking_value] = masking[masking_value]
    
    # Try Except Pass added 12/7/2022 to 'detect' corrupted files and skip over them, 
    # print statement will provide the corrupted filepath/file folder in question
    # the corrupted filepaths in question should be saved to the "corrupt.txt" file
    try:
        # Save into DCM
        print('entering bool mask try')
        CTimg = pydicom.dcmread(file_path)
        CTimg.PixelData = image
        CTimg.save_as(file_path)
        print('out of the bool mask')
    except AttributeError:
        with open("corruptedc.txt", "a") as corrupt_file:
            corrupt_file.write(str(file_path)+'\n')
            print(file_path + ' might be corrupted/ cannot be processed')
        corrupt_file.close()
        pass

    if display:
        plt.imshow(image)
        
    return image

# Function to avoid dcms that are not proper DICOM files readable image and metadata
def is_dicom_image(file: str) -> bool:
    # Boolean specifying if the file in question is a proper DICOM file with an image
    # The parameters 
    result = False
    try:
        img = pydicom.dcmread(file, force=True)
        if 'TransferSyntaxUID' not in img.file_meta:
            img.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        img.pixel_array
        result = True
    except (AttributeError, TypeError, KeyError):
        with open("notproperc.txt", "a") as proper_file: 
            proper_file.write(str(file)+'\n')  
            print(file + ' is not a proper DICOM file')
        proper_file.close()
        pass
    return result

# The below forloop should run in the directory housing all the DCMs
pwd = os.getcwd()

file_list = list()
file_notdcm = list()
path_list = list()

for root, dirs, files in os.walk(pwd):
    for name in files:
        if name.lower().endswith('.dcm'):
            file_list.append(os.path.join(root, name))
            #print(file_list)
        else:
            file_notdcm.append(os.path.join(root,name))
            # print(file_notdcm)     
            
print(file_list[:5])
# Removes dcm files that do not have metadata and will cause the boolean masking loop to interrupt
# from the list of paths which will be passed through the boolean_masking function
for path in file_list:
    x = is_dicom_image(path)
    if x == True:
        path_list.append(path)
print(path_list[:5])
# Boolean masking to get rid of the bed, concurrent.futures allows the process to be carried out in parallel
with concurrent.futures.ProcessPoolExecutor(max_workers = max) as executor:
     executor.map(boolean_masking, path_list)
