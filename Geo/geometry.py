from shapely.geometry import Polygon, Point, mapping, shape
import json

poly = Polygon([(0,0), (0,5), (5,5), (5,0)])
print poly
print('area', poly.area)
print('geometry', poly.geom_type)

patch = Point(12.0, 5.0).buffer(15.0)
print patch.area

# Shapely does not read and write data files but serializes and deserializes
a = shape(json.loads('{"type": "Point", "coordinates": [6.2, 3.3] }'))
print a
print json.dumps(mapping(a))