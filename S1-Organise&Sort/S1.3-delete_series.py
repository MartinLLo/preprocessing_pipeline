# -*- coding: utf-8 -*-
"""
S1.3 delete_series.py

in this script you'll be able to call the deleteseries function and enter the 
desired series number in the function parameters to delete the scans with the 
corresponding series number in the metadata

@author: m3lo4
"""
import os
import time
import pydicom
import pandas as pd

def delete_series(directory, series_number):
    st = time.time()
    
    file_list = list()
    file_notdcm = list()

    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.lower().endswith('.dcm'):
                file_list.append(os.path.join(root, name))
                # print(file_list)
            else:
                file_notdcm.append(os.path.join(root,name))
     
    lst = []   
    
    for file in file_list[:]:
        if pydicom.dcmread(file).SeriesNumber == series_number:
            print('yes')
            x = os.path.abspath(file) + ' is a topogram and will be removed'
            lst.append(x)
            # os.remove(file)
                    
    print(len(lst))
    df = pd.DataFrame(lst)
    df.to_csv('Series_deleted.csv')

    et = time.time()
    elapsed_time = et - st
    print('Script took:', elapsed_time, 'seconds')
