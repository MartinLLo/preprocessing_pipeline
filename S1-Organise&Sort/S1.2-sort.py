# -*- coding: utf-8 -*-
"""

S1.2-sort.py

This script does the following things
1)creates folders in the directory housing each patient's DICOM files
2)sorts and moves the DICOM files using the series number in the metadata of each DICOM file into the corresponding series folder
3)deletes any empty folders

@author: m3lo4
"""
import pydicom
import os
import shutil

pwd = os.getcwd()
extension = "*.dcm"
patientpaths = []
dicompaths = []
def dcms (filename, extension = ['*.dcm']):
    return any(filename.endswith('.dcm') for e in extension)

for root, dirs, files in os.walk(pwd):
    for filename in filter(dcms, files):
        patientpaths.append(os.path.abspath(root))

for root, dirs, files in os.walk(pwd):
    for filename in filter(dcms, files):
        dicompaths.append(os.path.join(root, filename))


# removes duplicates from paths
# set() removes duplicates from list
# ptpaths is list of paths to the CT folder of the Patient folder
ptpaths = set(patientpaths)
print(len(ptpaths))
# print(ptpaths)
# dicompaths is the list of paths to each dicom file
print(len(dicompaths))
# print(dicompaths[:5])
# print(dicompaths[-5:])

# define new series subfolders for CT series to go into, series subfolders are nested inside CTXXXXX folder
# new subfolder for ser1
ser1 = "series_1"
#  subfolder for ser2
ser2 = "series_2"
# new subfolder for ser3
ser3 = "series_3"
# new subfolder for ser4
ser4 = "series_4"
# new subfolder for ser5
ser5 = "series_5"
# new subfolder for ser6
ser6 = "series_6"
# new directory for ser7
ser7 = "series_7"
# new subfolder for ser8
ser8 = "series_8"
# new subfolder for ser9
ser9 = "series_9"
# new subfolder for ser10
ser10 = "series_10"
# new subfolder for ser11
ser11 = "series_11"
# new subfolder for ser12
ser12 = "series_12"
# new subfolder for ser13
ser13 = "series_13"

# iterate through patient list, using elements of list as pathnames
for path in ptpaths:
    # Path for series 1 (usually topograms)
    path1 = os.path.join(path, ser1)
    # check if path1 exists
    if not os.path.exists(path1):
        # make path1
        os.mkdir(path1)
     # Path for series 2
    path2 = os.path.join(path, ser2)
    # check if path1 exists
    if not os.path.exists(path2):
        # make path2
        os.mkdir(path2)
    # Path for series 3
    path3 = os.path.join(path, ser3)
    # check if path3 exists
    if not os.path.exists(path3):
        # make path3
        os.mkdir(path3)
    # Path for series 4
    path4 = os.path.join(path, ser4)
    # check if path4 exists
    if not os.path.exists(path4):
        # make path4
        os.mkdir(path4)
    # Path for series 5
    path5 = os.path.join(path, ser5)
    # check if path5 exists
    if not os.path.exists(path5):
        # make path5
        os.mkdir(path5)
    # Path for series 6
    path6 = os.path.join(path, ser6)
    # check if path6 exists
    if not os.path.exists(path6):
        # make path6
        os.mkdir(path6)
    # Path for series 6
    path7 = os.path.join(path, ser7)
    # check if path7 exists
    if not os.path.exists(path7):
        # make path7
        os.mkdir(path7)
    # Path for series 8
    path8 = os.path.join(path, ser8)
    # check if path8 exists
    if not os.path.exists(path8):
        # make path8
        os.mkdir(path8)     
    # Path for series 9
    path9 = os.path.join(path, ser9)
    # check if path9 exists
    if not os.path.exists(path9):
        # make path9
        os.mkdir(path9)
    # Path for series 10
    path10 = os.path.join(path, ser10)
    # check if path6 exists
    if not os.path.exists(path10):
        # make path10
        os.mkdir(path10)
    # Path for series 11
    path11 = os.path.join(path, ser11)
    # check if path11 exists
    if not os.path.exists(path11):
        # make path11
        os.mkdir(path11)
    # Path for series 12
    path12 = os.path.join(path, ser12)
    # check if path12 exists
    if not os.path.exists(path12):
        # make path12
        os.mkdir(path12)
    # Path for series 13
    path13 = os.path.join(path, ser13)
    # check if path13 exists
    if not os.path.exists(path13):
        # make path13
        os.mkdir(path13)
        
# SORT SERIES TO CORRECT SUBFOLDER
# list of filepaths to each dcm is dicompaths
for file in dicompaths:
    if pydicom.dcmread(file).SeriesNumber == 1:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser1
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 2:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser2
        shutil.move(file, filepath)       
    elif pydicom.dcmread(file).SeriesNumber == 3:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser3
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 4:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser4
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 5:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser5
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 6:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser6
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 7:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser7
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 8:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser8
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 9:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser9
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 10:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser10
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 11:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser11
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 12:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser12
        shutil.move(file, filepath)
    elif pydicom.dcmread(file).SeriesNumber == 13:
        filepath = '\\'.join(file.split('\\')[:-1]) + '\\' + ser13
        shutil.move(file, filepath)


# the folders are sorted into a list by listing all the paths in the directory, it is sorted from smallest to largest,
# hence the reverse = True condition.
folders = sorted(list(os.walk(pwd))[:-1], reverse = True)
for folder in folders:
# for folder in the sorted list 'folders', remove directory of the smallest folder, hence folder[0], the item listed in the 0th position is the smallest
    try:
        os.rmdir(folder[0])
    except OSError as error:
# this stops the os.rmdir as os.rmdir only remvoes empty folders, if a folder with files is passed through os.rmdir, error will be returned
        print("Directory '{}' contains files".format(folder[0]))