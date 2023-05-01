# preprocessing_pipeline

The preprocessing_pipeline is a series of scripts written in Python3 that sorts, thresholds, and segments [DICOM](https://www.dicomstandard.org/about/) datasets to produce a number of relevant file formats that could be used for machine learning, 2D/3D image analysis, or 3D modelling work. The scripts can be run via the terminal on Windows OS, macOS, Ubuntu OS.

## How it works
1) S1-Organise&Sort
    - S1.1-datacleaning.py: checks for corrupted and non-DICOM files and deletes the identified files in the directory.
    - S1.2-sort.py: checks the metadata of each DICOM file and sorts them into folders according to the series denoted in the file metadata, this script is optional    depending on your desired ouputs or intent. If separating scan series from each other is unecessary then this script can be skipped.
    - S1.3-delete_series.py: deletes DICOM files using the series number provided in the metadata. This script is optional depending on your intent. If you know the series number of what needs to be deleted, S1.2 can be skipped and this script can be run instead. 

2) S2-Removenoise
    - S2-removenoise.py: removes undesired structures such as the sliding bed that does into the CT gantry or other biological structures using thresholding. A mask of the tissues of interest is detected and preserved while the surrounding material/tissues are overwritten and removed. The script also has similar functions to script 1.1 where corrupted and non-DICOM images are filtered out.
    - S2-removenoise-MP.py: is the multi-processing version of S2-removenoise.py. It uses concurrent.futures to run the process on a designated number of processors available on your computing device. The number of processors used can be changed in the script to suit your hardware specifications.

3) S3-DCM2IMG
    - S3-DICOM2IMG.py: converts the DICOM image files or processed DICOM image files processed through S2-Removenoise thresholded PNG or JPEG files.
        - DCM2IMG(pwd, threshold_value_1, threshold_value_2,  img_format)
            - Parameters:
                - **pwd:** _present working directory_
                
                    Path to your directory holding the DICOM files you want to threshold and save as PNG or JPEG files
                - **threshold_value_1:** _lower bound of the HU threshold value_
                - **threshold_value_2:** _upper bound of the HU threshold value_                   
                    
                                    Common thresholding values:

                                         Bone --> 400, 1000

                                         Soft tissue --> 40, 80

                                         Water --> 0, 0

                                         Fat --> -60, -100

                                         Air --> -1000
                - **img_format:** _the image extension of your output file_                  
                    
                    If portable network graphics files are needed, simply enter 'png'
                    
                    If Joint Photographic Experts Group files are needed, simply enter 'jpeg'

4) S4-DCM2NIFTI
    - S4.1-DICOM2NIFTI.py: converts the DICOM dataset or the processed dataset from S2-Removenoise into NIfTI files.
    - S4.2-MOVENIFTI.py: moves the NIfTI files created and renamed according to subdirectory headings to a new and separate subdirectory exclusively.

5) S5-DCM2STL
    - S5.1-DICOM2STL.py: converts and thresholds the DICOM image files processed through S2-Removenoise or unprocessed DICOM image files into STL files
    - S5.2-MOVENIFTI.py: moves the stl files created and renamed according to subdirectory headings to a new and separate subdirectory exclusively.
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
