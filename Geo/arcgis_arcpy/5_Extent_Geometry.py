import arcpy

arcpy.env.workspace = r'C:\path\to\ws'

rasters = arcpy.ListRasters()

for raster in rasters:
    f = arcpy.Raster(raster)
    xmin = f.extent.XMin
    ymin = f.extent.YMin
    xmax = f.extent.XMax
    ymax = f.extent.YMax
    rectangle = "%s %s %s %s" % (xmin, xmax, ymin, ymax)

# [getattr(extent, x) for x in ("XMin", "YMin", "XMax", "YMax")]