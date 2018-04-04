import arcgisscripting
gp=arcgisscripting.create()
gp.workspace="c:/basedata"
#Buffer roads.shp based on each road feature's value in the Distance field,
# and dissolve buffers into groups according to values from Road_Type field.
gp.buffer("roads.shp","buffered_roads.shp","Distance","FULL","ROUND","LIST","Road_Type")

#Determine the type of vegetation within 100metres of all stream crossings

#Create the geoprocessor object
import arcgisscripting
gp=arcgisscripting.create()
 try:
     #Set the workspace
     gp.Workspace="c:/projects/RedRiverBasin/data.mdb"
     # process: find all stream crossings(points)
     gp.Intersect_analysis("roads;streams", "stream_crossings", "#",1.5, "point")
     #process: Buffer all stream crossings by 100 metres
     gp.Buffer("stream_crossings","stream_crossings_100m","100 meters")
     #Process:  clip the vegetation feature class to stream_crossing_100m
     gp.Clip("vegetation","stream_crossings_100m","veg_within_100m_of_crossings")
     #Process: summarise how much (area) of each type of vegetation is found within 100 metre of the stre
     gp.Statistics("veg_within_100m_of_crossings","veg_within_100m_of_crossings_stats","shape_area sum","

except:
    #If an error occured while running a tool, print the messages.
    print gp.GetMessages()