# preprocessing_pipeline

The preprocessing_pipeline is a series of scripts written in Python3 that sorts and thresholds [DICOM](https://www.dicomstandard.org/about/) datasets to produce a number of relevant file formats that could be used for machine learning, 2D/3D image analysis, or 3D modelling work. The scripts can be run via the terminal on Windows OS, macOS, Ubuntu OS.

## How it works
1) The first series of scripts in S1-Organise&Sort checks for corrupted and non-DICOM files, allows deletion, or sorting of scan series into discrete folders.
    - S1.1-datacleaning.py: checks for corrupted and non-DICOM files and deletes the identified files in the directory.
    - S1.2-sort.py: checks the metadata of each DICOM file and sorts them into folders according to the series denoted in the file metadata, this script is optional    depending on your desired ouputs or intent. If separating scan series from each other is unecessary then this script can be skipped.
    - S1.3-delete_series.py: deletes DICOM files using the series number provided in the metadata. This script is optional depending on your intent. If you know the series number of what needs to be deleted, S1.2 can be skipped and this script can be run instead. 

The second series of scripts in S2-Removenoise, removes undesired structures such as the sliding bed that does into the CT gantry. A mask of the tissues of ineterest is detected and preserved while the surrounding material/tissues are overwritten and removed. The script also has similar functions to script 1.1 where corrupted and non-DICOM images are filtered out.

The third script in S3-DCM2IMG, passes DICOM files through thresholding functions to produce 2D images in PNG and JPEG formats.

The fourth script 'DCM2NIFTI', aligns and converts DICOM files into single NIfTI files.

The fifth script 'DCM2STL', converts the thresholded and processed DICOM files into STL format using VTK.



## Required Packages
The collection of scripts is written in Python and will require the following packages
- matplotlib
- numpy
- os
- pydicom
- scipy
- skimage
- dicom2nifti
- Nibabel
- VTK
