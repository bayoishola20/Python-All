# split image into 4 parts

gdal2tiles.py --zoom=9 lasvegas_tm5_07jun04_crop_geo.tif output


# get general info of the image

gdalinfo lasvegas_tm5_07jun04_crop_geo.tif

# get SRS of the image

gdalsrsinfo lasvegas_tm5_07jun04_crop_geo.tif

'''
PROJ.4 : '+proj=utm +zone=11 +datum=WGS84 +units=m +no_defs '

OGC WKT :
PROJCS["WGS 84 / UTM zone 11N",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-117],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH],
    AUTHORITY["EPSG","32611"]]
'''

# reporoject (that is, change SRS), resampled using cubic resampling and compressed using LZW

gdalwarp -t_srs EPSG:3857 -r "cubic" -co "COMPRESS=LZW" lasvegas_tm5_07jun04_crop_geo.tif output.tif

'''
Creating output file that is 2187P x 2197L.
'''


