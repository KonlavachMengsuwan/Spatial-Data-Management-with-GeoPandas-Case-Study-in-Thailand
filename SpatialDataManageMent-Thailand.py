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
