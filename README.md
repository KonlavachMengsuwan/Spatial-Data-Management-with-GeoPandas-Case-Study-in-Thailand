# Spatial-Data-Management-with-GeoPandas-Case-Study-in-Thailand

## Install Geopandas package

### pip
```
pip install geopandas
```

### conda
```
conda install python=3 geopandas
```

## Set up packages

```
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
```
## Read Shapefile
### Thailand provinces Shapefile

```
os.getcwd()
province = gpd.read_file('C:/Users/konla/Desktop/Python/geo_environment/Data/Shapefile/Thailand/Province-20210207T153315Z-001/Province/TH_Province.shp')
```


