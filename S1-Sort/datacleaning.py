# -*- coding: utf-8 -*-
"""
S1.1: datacleaning.py

This script (part of S1) allows you to catch corrupted files through the is_dicom_image function
    The function appends corrupted file paths to a list (notproper.txt), which is then removed from the entire directory 
    using a for-loop and the delete_corrupt function

@author: m3lo4
"""
## packages required
import os
import time
import pydicom
import pandas as pd

def is_dicom_image(file: str) -> bool:
    # Boolean specifying if the file in question is a proper DICOM file with an image
    result = False
    try:
        img = pydicom.dcmread(file, force=True)
        if 'TransferSyntaxUID' not in img.file_meta:
            img.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        img.pixel_array
        result = True
    except (AttributeError, TypeError, KeyError, ):
        with open("notproper.txt", "a") as proper_file: 
            proper_file.write(str(file)+'\n')  
            print(file + ' is not a proper DICOM file')
        proper_file.close()
        pass
    return result
    
def delete_notdcm(directory):
    st = time.time()
    
    directory = os.getcwd()

    file_notdcm = []
    
    # load the txt list from is_dicom_image to for-loop below
    
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.lower().endswith('notproper.txt'):
                txt_file = open('notproper.txt', 'r')
                file_notdcm = txt_file.readlines
                txt_file.close()                
        
    for file in file_notdcm:
        os.remove(file)
    et = time.time()
    elapsed_time = et - st
    print('deleting corrupt files took:', elapsed_time, 'seconds')
    
pwd = os.getcwd()

file_list = list()
path_list = list()
                    
for path in file_list:
    x = is_dicom_image(path)
    if x == True:
        path_list.append(path)
        
if len(path_list = 0):
    print('there are no nondcm files in this directory')

delete_notdcm(pwd)