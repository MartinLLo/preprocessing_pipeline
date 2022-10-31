# preprocessing_pipeline

The preprocessing_pipeline is a series of scripts written in Python3 that sorts and thresholds [DICOM](https://www.dicomstandard.org/about/) datasets to produce a number of relevant file formats that could be used for machine learning, 2D/3D image analysis, or 3D modelling work. The scripts can be run via the terminal on Windows OS, macOS, Ubuntu OS.

## How it works
1) S1-Organise&Sort
    - S1.1-datacleaning.py: checks for corrupted and non-DICOM files and deletes the identified files in the directory.
    - S1.2-sort.py: checks the metadata of each DICOM file and sorts them into folders according to the series denoted in the file metadata, this script is optional    depending on your desired ouputs or intent. If separating scan series from each other is unecessary then this script can be skipped.
    - S1.3-delete_series.py: deletes DICOM files using the series number provided in the metadata. This script is optional depending on your intent. If you know the series number of what needs to be deleted, S1.2 can be skipped and this script can be run instead. 

2) S2-Removenoise
    - S2-Removenoise.py: removes undesired structures such as the sliding bed that does into the CT gantry. A mask of the tissues of ineterest is detected and preserved while the surrounding material/tissues are overwritten and removed. The script also has similar functions to script 1.1 where corrupted and non-DICOM images are filtered out.

3) S3-DCM2IMG
    - S3.1-DICOM2PNG.py: converts the processed DICOM image files from S2-Removenoise into thresholded PNG files.
    - S3.2-DICOM2JPEG.py: converts the processed DICOM image files from S2-Removenoise into thresholded JPEG files.

4) S4-DCM2NIFTI
    - S4.1-DICOM2NIFTI.py: converts the DICOM dataset or the processed dataset from S2-Removenoise into NIfTI files.
    - S4.2-MOVENIFTI.py: moves the NIfTI files created and renamed according to subdirectory headings to a new and separate subdirectory.

5) S5-DCM2STL
    - S5-DICOM2STL.py: converts the processed scan series from S2-Removenoise into .stl files

## Required Packages
The collection of scripts is written in Python and will require the following packages
- matplotlib
- numpy
- os
- pydicom
- scipy
- skimage
- dicom2nifti
- VTK
