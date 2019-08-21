#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime

geo = pd.read_csv('Geography.csv');

with open('./maps/china/china_geojson.json') as file:
    china = json.load(file)



fig = go.Figure(go.Choroplethmapbox(geojson=china,locations=geo.Regions,z=geo.followerPercentage,
                                    colorscale='Cividis',zmin=0,zmax=17,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 35.8617, "lon": 104.1954})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()





