import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
from math import sqrt
from matplotlib import pyplot as plt

if __name__== "__main__":main()

def main():    
    file = choosefile()
    df = pd.read_csv(file)
    print(list(df.columns.values))
    col1 = input("Enter the x column name :") 
    col2 = input("Enter the y column name :")
    x_train = df[col1].tolist()
    y_train = df[col2].tolist()
    
    mean_x, mean_y = mean(x_train), mean(y_train)
    var_x, var_y = variance(x_train, mean_x), variance(y_train, mean_y)
    covar = covariance(x_train, mean_x, y_train, mean_y)
    b0,b1 = coefficients(x_train, y_train)
    print("The linear equation for the provided dataset is : y = ",b0,"+",b1,"x")
    
    file = choosefile()
    df = pd.read_csv(file)
    list(df.columns.values)
    x_test = df[col1].tolist()
    y_act = df[col2].tolist()
    y_pred = predict(b0,b1,x_test)
    rootmse = rmse(y_act, y_pred)
    print ('The cost function value is %.3f' %(rootmse))
    plt.scatter(x_test, y_act)
    plt.scatter(x_test, y_pred, color='red')
    plt.plot(x_test, y_pred, color='red')
    plt.title('Linear Regression Graph')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
    
def mean(values):
    return sum(values)/float(len(values))

def variance(values, mean):
    return sum([(x-mean)**2 for x in values])/float(len(values))

def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x)*(y[i] - mean_y)
    return covar/float(len(x))
    
def coefficients(x,y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean)/variance(x, x_mean)
    b0 = y_mean - b1*x_mean
    return [b0,b1]
    
def predict(b0,b1,data):
    pred = list()
    for x in data:
        y = b0+b1*x
        pred.append(y)
    return pred
    
def choosefile() :
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(filetypes=[("csv file","*.csv")],title='Choose a csv file')
    if filename != None:
        return filename
    else:
        return null
        
def rmse(act, pred):
    sum_error = 0.0
    for i in range(len(act)):
        pred_error = pred[i] - act[i]
        sum_error += (pred_error**2)
    mean_error = sum_error/float(len(act))
    return sqrt(mean_error)





