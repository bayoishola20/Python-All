import overpass
import geojson

api = overpass.API()

# api.get returns a FeatureCollection of type GeoJSON by default
res = api.get("""
    area[name="Enschede"];
    // query all highways “highway=*”
    (way["highway"](area);
    relation["highway"](area);
    );
    // output geometry
    out geom;
""")

# if desired as string, then dump as string
# geojson_str = geojson.dumps(res)

# save geojson as file
with open("C:/Users/Adebayo/Documents/stuffs/Python-All/Geo/data/output/enschede_highway.geojson",mode="w") as f:
  geojson.dump(res,f)

# Convert GeoJSON to Shapefile https://mapshaper.org/