# -*- coding: utf-8 -*-
"""
S5.2 MOVENIFTI.py
This script moves all the stl files made from DICOM2STL.py to a designated directory
@author: martin lo
"""

import os
import shutil

pwd = os.getcwd()

sourcelist = []
stl_dir = pwd + os.path.join(os.sep + 'stl_models' + os.sep)
isExist = os.path.exists(stl_dir)
if not isExist:
    os.makedirs(stl_dir)

print(pwd)
print(stl_dir)

for root, dirs, files in os.walk(pwd):
	for item in files:
		if item.lower().endswith('.stl'):
			sourcelist.append(os.path.join(root, item))
print(sourcelist[:10])

for stl in sourcelist:
    shutil.move(stl, stl_dir)