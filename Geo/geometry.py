from shapely.geometry import Polygon

poly = Polygon([(0,0), (0,5), (5,5), (5,0)])
print poly
print('area', poly.area)
print('geometry', poly.geom_type)