import os
# import openpyxl as pxl
import csv
import re
import glob
from unittest import result
import pandas as pd
import numpy as np
import PIL
import math
import datetime as dt
from scipy.stats import wilcoxon,shapiro,ttest_rel
from scipy import stats
import matplotlib.pyplot as plt
import random
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

def import_data(root):
    
    res_data = pd.read_csv(root)
        
    return res_data

def print_df(d,row,col):
    for i in range(row):
        print(d.iloc[i])

def test(email,data):
    df = pd.read_csv(data[0])
    df_index = len(df.index)
    df_col = len(df.columns)-1
    res_data = []
    cols = df.columns
    print_df(df,df_index,df_col)
    for i in range(df_index):
        if df.iloc[i,1] == email:
            for j in range(df_col):
                col = []
                if j > 2:
                    col.append(cols[j])
                    col.append(df.iloc[i,j])
                    res_data.append(col)
                elif j == 0:
                    col.append("date")
                    col.append(df.iloc[i,j])
                    res_data.append(col)
                else:pass
        else:
            pass
    
    return res_data                

def extract_study_his(data,email):
    res_data = []
    count = len(data)
    for i in range(count):
        row_data = []
        df = import_data(data[i])
        df_index = len(df.index)
        df_col = len(df.columns)-1
        cols = df.columns
        for j in range(df_index):
            if df.iloc[j,1] == email:
                for k in range(df_col):
                    col = []
                    if k == 0:
                        col.append("date")
                        col.append(df.iloc[j,k])
                        row_data.append(col)
                    elif k > 2:
                        col.append(cols[k])
                        col.append(df.iloc[j,k])
                        row_data.append(col)
                    else:pass
            else:
                continue
        res_data += row_data
    return res_data
        
def make_dir(user):
    if os.path.exists('../study_history/') is not True:
        os.mkdir('../study_history/')
    if os.path.exists('../study_history/user_00{}/'.format(user)) is not True:
        os.mkdir('../study_history/user_00{}/'.format(user))
    dir_path = '../study_history/user_00{}/'.format(user)
    return dir_path

def main():
    root = '../'
    dir_name = 'study_history'
    sou_path = '../datasour/**'
    data = glob.glob(sou_path)
    # user_id = int(input('ユーザidを入力してください : '))
    test_user_id = 1
    # email = 'id00{}@g.nihon-u.ac.jp'.format(user_id)
    test_email = 'id001@g.nihon-u.ac.jp'
    savepath = make_dir(test_user_id)
    filename = "study_history_user_{}".format(test_user_id)

    study_history = extract_study_his(data,test_email)
    # test_data = test(test_email,data)
    # print(test_data)
    # for i in range(len(data)):
        # print(data.loc[i])
    print(study_history)
    
    df = pd.DataFrame(study_history)
    df.to_csv(savepath+filename+'.csv')

    

    
main()