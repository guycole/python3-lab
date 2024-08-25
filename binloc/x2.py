import numpy as np
import pandas as pd
import geopandas
import geoplot

from geopy import distance

station1 = np.array((40.415440, -122.250052))
station2 = np.array((40.398758, -122.218681))
print(distance.distance(station1, station2).miles)



newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)
