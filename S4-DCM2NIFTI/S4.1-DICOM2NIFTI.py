# -*- coding: utf-8 -*-
"""

S4.1 DICOM2NIFTI.py

This script does the following things
1)CONVERTS DICOM directories TO NIFTI and saves the NIFTI files in the same level as the DCM images
2)RENAMES NIFTI files TO UCLXXX_CTXXX_X.nii.gz

@author: m3lo4
"""

import os
import dicom2nifti as d2n

pwd = os.getcwd()
# print(pwd)

full_dir = []
dicom_dir = []

## all the folders in pwd
for root, dirs, files in os.walk(pwd):
    for name in dirs:
        full_dir.append(os.path.join(root, name))
# print(full_dir)
## directory to the dicom files (CT-xxx folder)
for path in full_dir:
    if 'CT-' in path:
        dicom_dir.append(full_dir.pop(full_dir.index(path)))
# print((dicom_dir))

# converting dicom directory to nifti
for item in dicom_dir:
    d2n.convert_dir.convert_directory(item, item)

## renaming nifti inside each CT-xxx folder
nifti_path = []

for nifti_dir in dicom_dir:
    for root, dirs, files in os.walk(nifti_dir):
        for item in files:
            if item.lower().endswith('.nii.gz'):
                # print(item)
                nifti_path.append((os.path.join(root, item)))

nifti_ext = '.nii.gz'
# print(len(nifti_path))
# print(nifti_path)

i = 0
prev_old = ''
for old_path in nifti_path:
    # print(old_path)
    # print(os.path.split(old_path))
    # print(type(os.path.split(old_path)))
    # print((os.path.split(old_path))[0])
    # print((os.path.split(old_path))[0].split(os.sep))
    # print((os.path.split(old_path))[0].split(os.sep)[-1])
    # print((os.path.split(old_path))[0].split(os.sep)[-2])
    # print(os.path.split(old_path)[0] + os.path.split(old_path)[0].split(os.sep)[-2] + '_' + os.path.split(old_path)[0].split(os.sep)[-1] + '_' + str(i) + nifti_ext)
    print(prev_old == os.path.split(old_path)[0])
    if prev_old == os.path.split(old_path)[0]:
        i += 1    
    else:
        prev_old = os.path.split(old_path)[0]
        i = 1
    new_path = ((os.path.split(old_path))[0])  + os.sep + (os.path.split(old_path))[0].split(os.sep)[-2] + '_' + (os.path.split(old_path))[0].split(os.sep)[-1] + '_' + str(i) + nifti_ext
    print(new_path)
    os.rename(old_path, new_path)