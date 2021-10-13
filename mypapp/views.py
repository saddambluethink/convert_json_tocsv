from django.shortcuts import render,HttpResponse
import csv
import json
import pandas as pd

# Create your views here.

def mycsv(request):
    #json file data
    data=pd.read_json('/home/saddam/Desktop/my.json')  
    data.to_csv('my_csv_file.csv')
    print("json data to csv")
    # read csv file
    # result = pd.read_csv("my_csv_file.csv")
    # print("csv file data",result)
    return HttpResponse("data saved into csv")
