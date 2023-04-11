# -*- coding: utf-8 -*-
"""
Using concurrent.futures - map method
Using new process_scan function - this saves the resized and rotated volume as a .npy file
This multiprocessing script processes all scans passes all the paths through process_scan function to resize and rotate, then save the output as a .npy file
This allows the later ML scripts to simply call the processed scans as .npy files (much smaller and lightweight) as the training, validation, and test sets
@author: m3lo4
"""
import time
import os
import numpy as np
import multiprocessing
import nibabel as nib
from scipy import ndimage
import concurrent.futures

def read_nifti_file(filepath):
    """Read and load volume"""
    # Read file
    scan = nib.load(filepath)
    # Get raw data
    scan = scan.get_fdata()
    return scan

def normalize(volume):
    """Normalize the volume"""
    min = -1000
    max = 400
    volume[volume < min] = min
    volume[volume > max] = max
    volume = (volume - min) / (max - min)
    volume = volume.astype("float32")
    return volume

def resize_volume(img):
    """Resize across z-axis"""
    # Set the desired depth
    desired_depth = 64
    desired_width = 128
    desired_height = 128
    # Get current depth
    current_depth = img.shape[-1]
    current_width = img.shape[0]
    current_height = img.shape[1]
    # Compute depth factor
    depth = current_depth / desired_depth
    width = current_width / desired_width
    height = current_height / desired_height
    depth_factor = 1 / depth
    width_factor = 1 / width
    height_factor = 1 / height
    # Rotate
    img = ndimage.rotate(img, 90, reshape=False)
    # Resize across z-axis
    img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=1)
    return img

# original process_scan from the Zunair 3DCNN for lung code
# save volume as .npy in the same directory as path was called from
def process_scan(path):
    """Read and resize volume"""
    # Read scan
    volume = read_nifti_file(f'{path}')
    # Normalize
    volume = normalize(volume)
    # Resize width, height and depth
    volume = resize_volume(volume)
    # Creating npy pathname for np.save
    pathname = os.path.basename(path)
    name = pathname.replace('.nii.gz', '.')
    # print(f'os.path.basename({path}), normalized and resized')
    # print(str(path), 'volume resize and normalized')
    print(str(pathname), 'normalized and resized')
    npy_path = path.replace(".nii.gz", ".npy")
    # Saving volume as .npy
    processed = np.save(str(npy_path), volume)
    print(str(name), 'has been saved as .npy')
    # print(f'os.path.basename({path}) has been processed and saved as .npy')
    # print(str(npy_path), 'npy saved')
    return processed


# Below are the list of paths that lead to the training data in their respective age ranges
# Pass the process_scan function using a for loop in concurrent.futures map
# This should return resized and rotated .npy files in the relevant subdirs

paths_train_1824 = [os.path.join(os.getcwd(), "census_train/cen_1824", x)
    for x in os.listdir("census_train/cen_1824")]
paths_train_2529 = [os.path.join(os.getcwd(), "census_train/cen_2529", x)   
    for x in os.listdir("census_train/cen_2529")]
paths_train_3034 = [os.path.join(os.getcwd(), "census_train/cen_3034", x)
    for x in os.listdir("census_train/cen_3034")]
paths_train_3539 = [os.path.join(os.getcwd(), "census_train/cen_3539", x)
    for x in os.listdir("census_train/cen_3539")]
paths_train_4044 = [os.path.join(os.getcwd(), "census_train/cen_4044", x)
    for x in os.listdir("census_train/cen_4044")]
paths_train_4549 = [os.path.join(os.getcwd(), "census_train/cen_4549", x)
    for x in os.listdir("census_train/cen_4549")]
paths_train_5054 = [os.path.join(os.getcwd(), "census_train/cen_5054", x)
    for x in os.listdir("census_train/cen_5054")]
paths_train_5559 = [os.path.join(os.getcwd(), "census_train/cen_5559", x)
    for x in os.listdir("census_train/cen_5559")]
paths_train_6064 = [os.path.join(os.getcwd(), "census_train/cen_6064", x)
    for x in os.listdir("census_train/cen_6064")]
paths_train_6569 = [os.path.join(os.getcwd(), "census_train/cen_6569", x)
    for x in os.listdir("census_train/cen_6569")]
paths_train_7074 = [os.path.join(os.getcwd(), "census_train/cen_7074", x)
    for x in os.listdir("census_train/cen_7074")]
paths_train_7579 = [os.path.join(os.getcwd(), "census_train/cen_7579", x)
    for x in os.listdir("census_train/cen_7579")]
paths_train_8084 = [os.path.join(os.getcwd(), "census_train/cen_8084", x)
    for x in os.listdir("census_train/cen_8084")]
paths_train_8589 = [    os.path.join(os.getcwd(), "census_train/cen_8589", x)
    for x in os.listdir("census_train/cen_8589")]
paths_train_90 = [os.path.join(os.getcwd(), "census_train/cen_90", x)
    for x in os.listdir("census_train/cen_90")]

# Below are the list of paths that lead to the validation data in their respective age ranges

paths_validation_1824 = [os.path.join(os.getcwd(), "census_validation/cen_1824", x)
    for x in os.listdir("census_validation/cen_1824")]
paths_validation_2529 = [os.path.join(os.getcwd(), "census_validation/cen_2529", x)
    for x in os.listdir("census_validation/cen_2529")]
paths_validation_3034 = [os.path.join(os.getcwd(), "census_validation/cen_3034", x)
    for x in os.listdir("census_validation/cen_3034")]
paths_validation_3539 = [os.path.join(os.getcwd(), "census_validation/cen_3539", x)
    for x in os.listdir("census_validation/cen_3539")]
paths_validation_4044 = [os.path.join(os.getcwd(), "census_validation/cen_4044", x)
    for x in os.listdir("census_validation/cen_4044")]
paths_validation_4549 = [os.path.join(os.getcwd(), "census_validation/cen_4549", x)
    for x in os.listdir("census_validation/cen_4549")]
paths_validation_5054 = [os.path.join(os.getcwd(), "census_validation/cen_5054", x)
    for x in os.listdir("census_validation/cen_5054")]
paths_validation_5559 = [os.path.join(os.getcwd(), "census_validation/cen_5559", x)
    for x in os.listdir("census_validation/cen_5559")]
paths_validation_6064 = [os.path.join(os.getcwd(), "census_validation/cen_6064", x)
    for x in os.listdir("census_validation/cen_6064")]
paths_validation_6569 = [os.path.join(os.getcwd(), "census_validation/cen_6569", x)
    for x in os.listdir("census_validation/cen_6569")]
paths_validation_7074 = [ os.path.join(os.getcwd(), "census_validation/cen_7074", x)
    for x in os.listdir("census_validation/cen_7074")]
paths_validation_7579 = [os.path.join(os.getcwd(), "census_validation/cen_7579", x)
    for x in os.listdir("census_validation/cen_7579")]
paths_validation_8084 = [os.path.join(os.getcwd(), "census_validation/cen_8084", x)
    for x in os.listdir("census_validation/cen_8084")]
paths_validation_8589 = [os.path.join(os.getcwd(), "census_validation/cen_8589", x)
    for x in os.listdir("census_validation/cen_8589")]
paths_validation_90 = [os.path.join(os.getcwd(), "census_validation/cen_90", x)
    for x in os.listdir("census_validation/cen_90")]

# Below are the list of paths that lead to the test data in their respective age ranges

paths_test_1824 = [os.path.join(os.getcwd(), "census_test/cen_1824", x)
    for x in os.listdir("census_test/cen_1824")]
paths_test_2529 = [os.path.join(os.getcwd(), "census_test/cen_2529", x)
    for x in os.listdir("census_test/cen_2529")]
paths_test_3034 = [os.path.join(os.getcwd(), "census_test/cen_3034", x)
    for x in os.listdir("census_test/cen_3034")]
paths_test_3539 = [os.path.join(os.getcwd(), "census_test/cen_3539", x)
    for x in os.listdir("census_test/cen_3539")]
paths_test_4044 = [os.path.join(os.getcwd(), "census_test/cen_4044", x)
    for x in os.listdir("census_test/cen_4044")]
paths_test_4549 = [os.path.join(os.getcwd(), "census_test/cen_4549", x)
    for x in os.listdir("census_test/cen_4549")]
paths_test_5054 = [os.path.join(os.getcwd(), "census_test/cen_5054", x)
    for x in os.listdir("census_test/cen_5054")]
paths_test_5559 = [os.path.join(os.getcwd(), "census_test/cen_5559", x)
    for x in os.listdir("census_test/cen_5559")]
paths_test_6064 = [os.path.join(os.getcwd(), "census_test/cen_6064", x)
    for x in os.listdir("census_test/cen_6064")]
paths_test_6569 = [os.path.join(os.getcwd(), "census_test/cen_6569", x)
    for x in os.listdir("census_test/cen_6569")]
paths_test_7074 = [ os.path.join(os.getcwd(), "census_test/cen_7074", x)
    for x in os.listdir("census_test/cen_7074")]
paths_test_7579 = [os.path.join(os.getcwd(), "census_test/cen_7579", x)
    for x in os.listdir("census_test/cen_7579")]
paths_test_8084 = [os.path.join(os.getcwd(), "census_test/cen_8084", x)
    for x in os.listdir("census_test/cen_8084")]
paths_test_8589 = [os.path.join(os.getcwd(), "census_test/cen_8589", x)
    for x in os.listdir("census_test/cen_8589")]
paths_test_90 = [os.path.join(os.getcwd(), "census_test/cen_90", x)
    for x in os.listdir("census_test/cen_90")]

path_train_all = []
path_val_all = []
path_test_all = []
path_train_all.extend(paths_train_1824 + paths_train_2529 + paths_train_3034 + paths_train_3539 + paths_train_4044 + paths_train_4549 + paths_train_5054 + paths_train_5559 + paths_train_6064 + paths_train_6569 + paths_train_7074 + paths_train_7579 + paths_train_8084 + paths_train_8589 + paths_train_90)
path_val_all.extend(paths_validation_1824 + paths_validation_2529 + paths_validation_3034 + paths_validation_3539 + paths_validation_4044 + paths_validation_4549 + paths_validation_5054 + paths_validation_5559 + paths_validation_6064 + paths_validation_6569 + paths_validation_7074 + paths_validation_7579 + paths_validation_8084 + paths_validation_8589 + paths_validation_90)
path_test_all.extend(paths_test_1824 + paths_test_2529 + paths_test_3034 + paths_test_3539 + paths_test_4044 + paths_test_4549 + paths_test_5054 + paths_test_5559 + paths_test_6064 + paths_test_6569 + paths_test_7074 + paths_test_7579 + paths_test_8084 + paths_test_8589 + paths_test_90)

path_all = []
path_all.extend(path_train_all + path_val_all + path_test_all)
print(type(path_all))
print(len(path_all))
print(path_all[:10])
print(path_all[-9:])


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_scan, path_all)