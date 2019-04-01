
'''
Description: collect background data for your study area from OSMnx python package
Author: Diao
'''

import osmnx as ox
from PIL import Image
import matplotlib.pyplot as plt
# from IPython.display import Image

# Downloading the administrative boundary of a city, e.g. the bounday of Munich
# Change "Munich" to your own city
gdf_city = ox.gdf_from_place('munich')

filename ='city_boudary' + '.geojson'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(gdf_city.to_json())

# Downloading building footprints
# The following codes will download all the buildings with 1km distance around TUM
# Since the downloading is a little bit time-cosuming , better to set a small threshold (e.g. under 3000 m)
tum = (48.1514082, 11.567568)
gdf_build = ox.buildings_from_point(point = tum, distance = 1000)

filename = 'TUM_buildings' + '.geojson'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(gdf_build.to_json())

# Downloading a certain type of road network in a city, e.g. all the walkable roads in Munich
# Select a type of road network that you want to download 
# ['all_private', 'all', 'bike', 'walk', 'drive', 'drive_service']
G = ox.graph_from_place('Munich',	network_type='bike')
G_projected	= ox.project_graph(G)
#ox.save_graph_shapefile(G_projected, filename= 'munich_road_bike', folder='C:/documents/')
ox.save_graph_shapefile(G_projected, filename= 'munich_road_bike')


""" # Step 4, Downloading a certain types of POI in a city, e.g. all universities in Munich
city_polygon = city.geometry[0]
#gdf_POIs_Unis = ox.create_poi_gdf(polygon = city_polygon, amenities = 'university', north=None, south=None, east=None, west=None)
gdf_POIs_Unis = ox.pois_from_place('Munich',amenities = ['university'])

# kept certain fileds
keep_columns = ['addr:city', 'addr:country', 'addr:housename', 'addr:housenumber', 'addr:postcode', 'addr:street', 'addr:suburb',
'geometry', 'name','name:en', 'osmid','landuse', 'nodes',  'opening_hours','type', 'ways']
gdf_POIs_Unis_simplify = gdf_POIs_Unis[keep_columns]

# find the coordiante of TUM
POIs_Unis = gdf_POIs_Unis_simplify[gdf_POIs_Unis_simplify['name'] == 'Technische Universität München']  # 11.567568 48.1514082
 """