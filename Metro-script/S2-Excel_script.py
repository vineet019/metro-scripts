from s2 import s2
import pandas as pd
from geopy import distance
import matplotlib.pyplot as plt


xls = pd.ExcelFile(r"/home/vineet/metro-route/yellow-line.xlsx")
var= pd.read_excel('/home/vineet/metro-route/yellow-line.xlsx')

report = xls.parse(0)

lat = report['Latitude']
lon = report['Longitude']
res = 13

i =-1 
while True :
#for i in range(24):
    i = i+1;
    s2_address = s2.geo_to_s2(lat[i], lon[i], res)
    aaa = s2.s2_to_geo_boundary(s2_address)
    print(aaa)



