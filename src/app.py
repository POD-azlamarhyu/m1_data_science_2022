# coding: utf-8
import os
# import openpyxl as pxl
import csv
import re
import glob
import pandas as pd
import numpy as np
import PIL
import math
import datetime as dt
import random
import matplotlib
from reportlab.pdfgen import canvas as cvs
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4 as a4, portrait
from reportlab.platypus import Table as tbl, TableStyle,Paragraph, PageBreak, FrameBreak
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import BaseDocTemplate,PageTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.frames import Frame
from reportlab.platypus.flowables import Spacer

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
    print(cols)
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
                        col.append(str(df.iloc[j,k]))
                        row_data.append(col)
                    elif k > 2 and k <= 10:
                        col.append(cols[k])
                        col.append(str(df.iloc[j,k]))
                        row_data.append(col)
                    elif k > 10:
                        col.append(cols[k])
                        col.append(str(df.iloc[j,k]))
                        row_data.append(col)
                    else:pass
            else:
                continue
        res_data += row_data
    return res_data
        
def make_dir(user):
    if os.path.exists('../study_history/') is not True:
        os.mkdir('../study_history/')
    if os.path.exists('../study_history/user_{}/'.format(user)) is not True:
        os.mkdir('../study_history/user_{}/'.format(user))
    dir_path = '../study_history/user_{}/'.format(user)
    return dir_path

def make_pdf(data,filename,pages,email):
    print_df(data,len(data),1)
    page = BaseDocTemplate(filename+'.pdf',title="学習履歴" ,pagesize=portrait(a4))
    font= "HeiseiMin-W3"
    
    titlex = 240
    titley = 750
    userx = 550
    usery = 700
    show = 1 #Frameの枠を表示
    frames = [
            Frame(25 * mm, 120*mm, 150*mm, 50*mm, showBoundary=0),
            Frame(10 * mm, 30*mm, 70*mm, 80*mm, showBoundary=show),
            Frame(110 * mm, 50*mm, 75*mm, 60*mm, showBoundary=show),
        ]
    style_dict ={
        "name":"normal",
        "fontName":"HeiseiKakuGo-W5",
        "fontSize":20,
        "leading":20,
        "firstLineIndent":15,
        }
    page_template = PageTemplate("frames", frames=frames)
    page.addPageTemplates(page_template)
    style = ParagraphStyle(**style_dict)

    flowables = []
    # for i in range(pages):
    #     if i == 0:
    #         page.drawString(260,700,"学習履歴")
    #     else:
    
    rows = len(data.index)
    cols = len(data.columns)
    space = Spacer(5*mm, 5*mm)
    count = 0
    primaryx = userx - 20
    primaryy = usery - 20
    textx = titlex + 20
    texty = titley + 20
    for i in range(rows):
        if data.iloc[i,0] == "date" and count == 0:
            count += 1
        elif data.iloc[i,0] == "date" and count == 1:
            flowables.append(FrameBreak())
            flowables.append(PageBreak()) 
        else:
            para = Paragraph(data.iloc[i,1])
            flowables.append(para)
            flowables.append(space)
        
    page.multiBuild(flowables)
    page.save()
    
def main():
    root = '../'
    dir_name = 'study_history'
    sou_path = '../datasour/**'
    data = glob.glob(sou_path)
    # user_id = input('ユーザidを入力してください : ')
    tuser_id = "id001"
    email = '{}@g.nihon-u.ac.jp'.format(tuser_id)
    test_email = 'id001@g.nihon-u.ac.jp'
    savepath = make_dir(tuser_id)
    filename = "study_history_user_{}".format(tuser_id)

    study_history = extract_study_his(data,email)
    # test_data = test(test_email,data)
    # print(test_data)
    # for i in range(len(data)):
        # print(data.loc[i])
    # print(study_history)
    
    df = pd.DataFrame(study_history)
    df.to_csv(savepath+filename+'.csv')
    df.to_excel(savepath+filename+'.xlsx')
    pdffile = savepath+filename
    make_pdf(df,pdffile,len(data),email)
    
main()