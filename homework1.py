# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:30:24 2018

@author: CFSS-FS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import zipfile
dl_link='http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip'
dl=requests.get(dl_link)
with open('csv.zip','wb') as f:
    f.write(dl.content)
csvz=zipfile.ZipFile('csv.zip')
csvz.extract('Salaries.csv')
csvz.extract('Teams.csv')
sadata=pd.read_csv('Salaries.csv')
ye=sadata.yearID.drop_duplicates(keep='first')
yearsum={}
ye=list(ye)
for i in range(len(sadata)):
    for j in range(len(ye)):
        if sadata.iloc[i,0]==ye[j]:
            if ye[j] in yearsum:
                yearsum[ye[j]]=yearsum[ye[j]]+sadata.iloc[i,4]
            else:
                yearsum[ye[j]]=0
                yearsum[ye[j]]=yearsum[ye[j]]+sadata.iloc[i,4]
                