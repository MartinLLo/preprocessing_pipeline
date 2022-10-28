# preprocessing_pipeline

The preprocessing_pipeline is a series of scripts written in Python3 that sorts and thresholds [DICOM](https://www.dicomstandard.org/about/) datasets to produce a number of relevant file formats that could be used for machine learning, 2D/3D image analysis, or 3D modelling work.

## How it works
THe first script 'Dataset sorting and extraction' takes DICOM images as input and sorts them into folders according to the series numbers denoted in the file metadata.

The second script 'Noise removal and segmentation', removes undesired structures such as the sliding bed that does into the CT gantry. A mask of the tissues of ineterest is detected and preserved while the surrounding material/tissues are overwritten and removed.

The third script 'Thresholding for tissues of interest', passes DICOM files through thresholding functions to produce 2D images in PNG and JPEG formats.

The fourth script 'Conversion to NIfTI format', aligns and converts DICOM files into single NIfTI files.

The fifth script 'Conversion to Stereolithography format', converts the thresholded and processed DICOM files into STL format using VTK.



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

