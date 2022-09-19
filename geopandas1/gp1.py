import geopandas
import matplotlib

path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)
print(gdf)

gdf["area"] = gdf.area
print(gdf["area"])

gdf['boundary'] = gdf.boundary
print(gdf['boundary'])

gdf['centroid'] = gdf.centroid
print(gdf['centroid'])

first_point = gdf['centroid'].iloc[0]
gdf['distance'] = gdf['centroid'].distance(first_point)
print(gdf['distance'])

gdf.plot("area", legend=True)
matplotlib.pyplot.show()

#gdf.explore("area", legend=False)

print("done")
