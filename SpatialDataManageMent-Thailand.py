# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:55:19 2021

@author: konla
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

from shapely.geometry import Point
import pandas as pd
import geopandas as gpd

from geopandas import GeoSeries
from geopandas import GeoDataFrame

import requests
import geojson

os.getcwd()
province = gpd.read_file('C:/Users/konla/Desktop/Python/geo_environment/Data/Shapefile/Thailand/Province-20210207T153315Z-001/Province/TH_Province.shp')

province.head(3)

province.plot(figsize = (6,5));

# Shapefile information

# Length of dataframe
len(province)

# First three lines
province.head(3)

# First Row
province.iloc[0]

# First Column
province.iloc[:,0]

# List all column names
list(province.columns) 

# Columns Names
province.columns

# First Column Name
province.columns[0]

# coordinate reference system
province.crs


# Calculate boundary of polygon
province.geometry.bounds

# Calculate area
province.geometry.area

# Average Area
province.Area_km2_.mean()

big_province = province[province.Area_km2_ > 8000]
list(big_province.columns) 

# How many province which has the area greater than 8000 km2
len(big_province)

# Add one more row after the last column
big_province['area'] = (province.geometry.area)
list(big_province.columns) 

big_province.plot(column = 'area', cmap = 'OrRd', figsize = (6,5));

