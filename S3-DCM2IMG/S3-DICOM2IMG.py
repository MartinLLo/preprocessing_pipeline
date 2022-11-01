# -*- coding: utf-8 -*-
"""
@author: martin lo

S3-DICIOM2IMG

Convert DICOM to thresholded PNG or JPEG
Threshold by entering the lower and upper thresholds required
Common thresholding values include:
    Bone --> 400, 1000
    Soft tissue --> 40, 80
    Water --> 0, 0
    Fat --> -60, -100
    Air --> -1000

"""
# Packages required
import pydicom
import numpy as np
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

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
# print(pwd)

def DCM2IMG(pwd, window_center, window_width, img_format, display = False):
    paths_pwd = []
    dicom_pwd = []
    
    for root, dirs, files in os.walk(pwd):
        for name in files:
            paths_pwd.append(os.path.join(root, name))
    # print(paths_pwd)
    # print(len(paths_pwd))
    # x = ((paths_pwd)[1])
    # print(type(x))
    
    # list of dicoms in pwd
    for path in paths_pwd:
        if '.dcm' in path:
            dicom_pwd.append(path)
    # print(len(dicom_pwd))
            
    for path in dicom_pwd:
            name = os.path.splitext(path)[0]
            # print(name)
            print(name + str(img_format))
            med_img = pydicom.read_file(path)
            img = med_img.pixel_array
            hu_img = transform_to_hu(med_img, img)
            thresholded = window_image(hu_img, window_center, window_width)
            mpimg.imsave(name + '.' + str(img_format), thresholded, cmap = 'gray', format=str(img_format))
            
            if display:
                plt.imshow(thresholded, cmap = 'gray')
                    
    return thresholded

DCM2IMG(pwd, 400, 1000, 'jpeg')
