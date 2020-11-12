# Python3 interpreter used

import gdal # gdal 3.0.4 used
import ogr
from osgeo import osr


# open the images
image_left = gdal.Open("C:/Users/Adebayo/Documents/stuffs/Python-All/Geo/data/overlap_data/left.tif")
image_right = gdal.Open("C:/Users/Adebayo/Documents/stuffs/Python-All/Geo/data/overlap_data/right.tif")

# get transformations
gt1 = image_left.GetGeoTransform()
gt2 = image_right.GetGeoTransform()

# find each image's bounding box
# get r1 & r2 top-left(long, lat) and bottom-right(long, lat) bounding coordinates.
r1 = [gt1[0], gt1[3], gt1[0] + (gt1[1] * image_left.RasterXSize), gt1[3] + (gt1[5] * image_left.RasterYSize)]
r2 = [gt2[0], gt2[3], gt2[0] + (gt2[1] * image_right.RasterXSize), gt2[3] + (gt2[5] * image_right.RasterYSize)]
print ('\timage1 bounding box: %s' % str(r1))
print ('\timage2 bounding box: %s' % str(r2))


# this intersection is the top-left(long, lat) and bottom-right(long, lat)
intersection = [ [max(r1[0], r2[0]), min(r1[1], r2[1])], [min(r1[2], r2[2]), max(r1[3], r2[3])] ]

print ('\tintersection: %s' % str(intersection))

# forming full overlap area rectangle clock-wise direction starting from top-left. First point is also repeated at the end to form closed geometry
overlap_rect = [ [max(r1[0], r2[0]), min(r1[1], r2[1])], 
                 [min(r1[2], r2[2]), min(r1[1], r2[1])],
                 [min(r1[2], r2[2]), max(r1[3], r2[3])], 
                 [max(r1[0], r2[0]), max(r1[3], r2[3])],
                 [max(r1[0], r2[0]), min(r1[1], r2[1])] ]

print ('\toverlap rectangle: %s' % str(overlap_rect))


# create ring
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(overlap_rect[0][0], overlap_rect[0][1])
ring.AddPoint(overlap_rect[1][0], overlap_rect[1][1])
ring.AddPoint(overlap_rect[2][0], overlap_rect[2][1])
ring.AddPoint(overlap_rect[3][0], overlap_rect[3][1])
ring.AddPoint(overlap_rect[0][0], overlap_rect[0][1])

# create polygon geometry
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)

# print(poly.ExportToWkt())

# creating shapefile
driver = ogr.GetDriverByName('Esri Shapefile')
ds = driver.CreateDataSource("C:/Users/Adebayo/Documents/stuffs/Python-All/Geo/data/overlap_output/overlap.shp")

# srs = osr.SpatialReference()
# srs.ImportFromEPSG(4326)

layer=ds.CreateLayer('C:/Users/Adebayo/Documents/stuffs/Python-All/Geo/data/overlap_output/overlap', None, ogr.wkbPolygon) # replace None with srs if able to resolve
fieldDefn_=ogr.FieldDefn('id', ogr.OFTInteger)
layer.CreateField(fieldDefn_)
featureDefn=layer.GetLayerDefn()
feature=ogr.Feature(featureDefn)
feature.SetGeometry(poly)
feature.SetField('id',1)
layer.CreateFeature(feature)
