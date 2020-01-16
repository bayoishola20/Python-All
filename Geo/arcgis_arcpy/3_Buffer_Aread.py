""" The analysis we will create with the model, and eventually export to Python for further
refinement, will use bus stops along a specific line in San Francisco. These bus stops will
be buffered to create a representative region around each bus stop. The buffered areas will
then be intersected with census blocks to find out how many people are within each
representative region around the bus stops. """

# Windows Explorer: "C:\Projects\PacktDB.gdb\Chapter3Results\Intersect71Census"
# Pythonic version: "C:/Projects/PacktDB.gdb/Chapter3Results/Intersect71Census"

import arcpy

bufferDist = 200
bufferDistUnit = "Meter"


def selectBufferIntersect(selectIn,selectOut,bufferOut,intersectIn, intersectOut, sqlStatement, bufferDist, buffDistUnit, lineName, busSignage):
    pass
