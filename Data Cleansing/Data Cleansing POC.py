import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd


if __name__== "__main__":main()

def choosefile() :
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(filetypes=[("csv file","*.csv")],title='Choose a csv file')
    if filename != None:
        return filename
    else:
        return null
        
def choosedir() :
    root = tk.Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(title='Choose the folder to save file')
    if dirname != None:
        return dirname
    else:
        return null

def dropCol(df, null_column):
    user = input("Do you want to drop the column? (y/n) :")
    if(user == 'y'):
        del df[null_column]
    elif(user == 'n'):
        nullFunc(df, null_column)
    else:
        print("Invalid input")

def dropRow(df, null_column):
    user3 = input("Do you want to drop the rows? (y/n) :")
    if(user3 == 'y'):
        df.drop(df[df[null_column].isnull()].index, inplace=True)
    elif(user == 'n'):
        nullFunc(df, null_column)
    else:
        print("Invalid input")

def nullFunc(df, null_column):
    type = df[null_column].dtypes
    if(type == 'O'):
        print("The column is a categorical variable")
        names = df[null_column].unique()
        cleanNames = [z for z in names if str(z) != 'nan']
        print (cleanNames)
        user1 = input("Enter any values from the above list to replace null value. :")
        if(user1 in cleanNames):
           df[null_column].replace(np.NaN, user1, inplace=True)
        else:
            print("Invalid input")
    elif(type == 'float64' or type == 'int64'):
        print("The column is a numerical variable")
        user2 = input("Do you want to replace null values with average value or with zero? (avg/zero) :")
        if(user2 == 'avg'):
            avg = df[null_column].mean()
            df[null_column].fillna(avg, inplace=True)
        elif(user2 == 'zero'):
            df[null_column].fillna(0, inplace=True)

def main():
    file = choosefile()
    df = pd.read_csv(file)
    null_columns=df.columns[df.isnull().any()]
    m = max(df.count())
    n = len(null_columns)
    
    for i in range(n):
        x = df[null_columns[i]].count()
        valper = x*100/m
        nullper = 100-valper
        print("Percentage of null values in ", null_columns[i], " column is ", nullper)
        if(nullper>50):
            dropCol(df, null_columns[i])
        elif(nullper<10):
            dropRow(df, null_columns[i])
        else:
            nullFunc(df, null_columns[i])
    
    dirname = choosedir()
    df.to_csv(dirname+'\df_out.csv', index=False)
    print("Data has been cleansed and saved in", dirname, "folder")