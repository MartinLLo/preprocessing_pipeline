# -*- coding: utf-8 -*-
"""
S5.1 DICOM2STL.py
This code has been adapted from somada141. His work can be found on https://bitbucket.org/somada141/pyscience/src/master/
The adaptations to the original code makes it so that the creation of the STL files can be done concurrently through concurrent futures and the additional for loop options allows for entire directories of DCMs to be converted into STLs
@author: martin lo
"""

import vtk
import os
import re

## Loading the DICOM data
pwd = os.getcwd()
# print(pwd)
full_dir = []
dicom_dir = []
dcm_dir = []

## all the folders in pwd
for root, dirs, files in os.walk(pwd):
    for name in dirs:
        full_dir.append(os.path.join(root, name))
print(full_dir[:5])
## directory to the dicom files (CT-xxx folder)
for path in full_dir:
    if 'CT-' in path:
        dicom_dir.append(full_dir.pop(full_dir.index(path)))
print(len(dicom_dir))

## finds any directory/subdirectory containing .dcm files
for root, dirs, files in os.walk(pwd):
    for item in files:
        if item.lower().endswith('.dcm'):
            x = os.path.join(root, item)
            y = os.path.basename(item)
            z = x.replace(str(y), '')
            dcm_dir.append(z)
dcm_dir = list(set(dcm_dir))
print(dcm_dir)
print(len(dcm_dir))

for dirs in dcm_dir:
    reader = vtk.vtkDICOMImageReader()
    reader.SetDirectoryName(dirs)
    reader.Update()

    ## Loading pixel spacing values
    ConstPixelSpacing = reader.GetPixelSpacing()

    ## Use the vtkImageThreshold() to clean remaining soft-tissue from the image data after S2.1 Removenoise.py
    # change the thresholding value as needed
    threshold = vtk.vtkImageThreshold()
    threshold.SetInputConnection(reader.GetOutputPort())
    threshold.ThresholdByLower(250)  # remove all soft tissue
    threshold.ReplaceInOn()
    threshold.SetInValue(0)  # set all values below 400 to 0
    threshold.ReplaceOutOn()
    threshold.SetOutValue(1)  # set all values above 400 to 1
    threshold.Update()

    ## Use the `vtkDiscreteMarchingCubes` class to extract the surface
    dmc = vtk.vtkDiscreteMarchingCubes()
    dmc.SetInputConnection(threshold.GetOutputPort())
    dmc.GenerateValues(1, 1, 1)
    dmc.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(dmc.GetOutputPort())
    
    ## creating stl filename
    # replace 'substring_index' with directory/individual identifier of choice]
    y = (re.search('substring_index', dirs).span())
    substring_index = y[0]
    print(substring_index)
    new_name = dirs[substring_index:]
    stl_name = str(new_name.replace('\\', "_"))
    stl_name2 = str(new_name.replace('', "_"))
    print(stl_name2)

    ## Writing the extracted surface as an .stl file
    writer = vtk.vtkSTLWriter()
    writer.SetInputConnection(dmc.GetOutputPort())
    writer.SetFileTypeToBinary()
    writer.SetFileName(stl_name2 +".stl")
    writer.Write()
