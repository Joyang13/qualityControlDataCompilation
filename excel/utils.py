import os, re, time, string

LI = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
INDEX = ['料號', '品名'] 
HEAD = ['不良總數', '變形', '尺寸不良', '髒汙', '烤漆不良', 
        '毛邊', '刮傷', '印刷不良', '缺件', '螺孔不良', '氣密不良', '功能不良',
        '破裂', '滑牙', '其他', '其他(備註)', '原材不良']

import pandas as pd
from numpy import NaN

def combine():
    #create a list where there are different names to store out files
    df_l = []

    #process 'em files first
    process_inner(df_l)
    process_outter(df_l)
    
    #concatanate all of the df inside the list
    df = concat(df_l)

    #start grouping them! While perserving 'other'
    #making sure that material numbers and 'others' are all non nan values
    df.iloc[:, [0,17]] = df.iloc[:,[0,17]].fillna('')
    #group all of the data using A and B
    j = df.groupby(['A','B']).sum()

    # order the number to see large to small
    j = j.sort_values(by= 'C', ascending=False)

    #change the head of the excel
    j.index.names = INDEX
    j.columns = HEAD

    #write into excel at somewhere else
    cur_dir = os.getcwd()
    print(cur_dir)
    os.chdir(r'..')
    print(os.getcwd())
    os.makedirs('temp', exist_ok = True)
    os.chdir(r'temp')
    j.to_excel('final.xlsx', 'Sheet1')

def process_inner(df_l):
    current_path = os.getcwd()
    if os.path.basename(current_path) == 'QA':
        os.chdir(current_path + r'/media/inner_files')
    else:
        os.chdir(current_path + r'/../inner_files')
    inner_files = get_inner_files()

    #put parsed inner data in df list
    for file in inner_files:
        df_l.append(parse_inner(file))

def process_outter(df_l):
    current_path = os.getcwd()
    os.chdir(current_path + r'/../outter_files')
    outter_files = get_outter_files()

    #put parsed outter data in df list
    for file in outter_files:
        df_l.append(parse_outter(file))

def get_outter_files():
    files = []
    for f in os.listdir():
        if (f.endswith('.xlsx') | f.endswith('.xls') | f.endswith('.xml')) and f.startswith ('20') and not f.startswith('~$'):
            files.append(f)
    return(files)

def get_inner_files():
    files = []
    for f in os.listdir():
        if (f.endswith('.xlsx') | f.endswith('.xls') | f.endswith('.xml')) and not f.startswith('20') and not f.startswith('~$'):
            files.append(f)
    return(files)

def parse_outter(file):
    df = pd.read_excel(file)
    #parse out the data parts and rename the head
    df = df.iloc[2:,5:24]
    df.columns = LI
    return(df)

def parse_inner(file):
    df = pd.read_excel(file)
    df.reset_index(level=[0,1,2], inplace=True)
    df = df.iloc[3:,0:19]
    df.columns = LI
    return(df)

def concat(df_list):
    df = df_list[0]
    for l in df_list[1:]:
        df = pd.concat([df,l])
    return(df)


if __name__ == '__main__':
    combine()