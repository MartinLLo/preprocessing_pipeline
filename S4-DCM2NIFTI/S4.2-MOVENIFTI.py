# -*- coding: utf-8 -*-
"""
S4.2 MOVENIFTI.py
This script moves all the nifti files made from DICOM2NIFTI.py to a designated directory - UCLH_NIFTI
@author: martin lo
"""

import os
import shutil

pwd = os.getcwd()

sourcelist = []

# edit the nifti_dir as needed
nifti_dir = pwd + os.path.join(os.sep + 'nifti_models' + os.sep)
isExist = os.path.exists(nifti_dir)
if not isExist:
    os.makedirs(nifti_dir)
print(pwd)
print(nifti_dir)

for root, dirs, files in os.walk(pwd):
	for item in files:
		if item.lower().endswith('.nii.gz'):
			sourcelist.append(os.path.join(root, item))
print(sourcelist[:10])

# for nifti in sourcelist:
#     shutil.move(nifti, nifti_dir)
