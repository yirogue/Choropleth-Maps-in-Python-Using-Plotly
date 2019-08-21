# Choropleth-Maps-in-Python
The easiest way to build a choropleth map in Python using Plotly

After the release of plotly's latest version (version 4.1.0), building a choropleth map in Python is no longer difficult and complex. 
All you need now to build a choropleth map are only three things:
- The latest version of plotly which comes with a new chart type -- **Choroplethmapbox**
- A geojson file which contains the coordinates of the country/regions that you'd like to draw
- A csv file which contains the data that you'd like to plot on the map

## Install plotly
plotly.py can be installed using pip or pip3

```
$ pip install plotly==4.1.0
```

or conda.

```
$ conda install -c plotly plotly=4.1.0
```

## Find your geojson file
You can find the maps for most countries in the world in topojson format via this [repository](https://github.com/deldersveld/topojson).  
After finding the right topojson file, you will need to convert the file into geojson format. While you can also write python codes to convert the file, I find this [website](https://mapshaper.org/) rather easy to use.

Note that the geojson file is a dictionary which typically contains two keys:
- **type**
- **features**: a list containing multiple dictionaries, each of which has four keys - *type*, *geometry*, *properties*, *id*
 
In the geojason file of Chinese map I used this time, each dictionary in features represents a province in China, where the geometry contains the coordinates of the province, the properties contains the province's specific info, and I used the province's name as its id.

***id is an important feature that will be used to plot your data on the map later**
 
## Basic codes for mapping

The basic codes for mapping are as follows:
```
fig = go.Figure(go.Choroplethmapbox(geojson=china,locations=geo.Regions,z=geo.followerPercentage,
                                    colorscale='Cividis',zmin=0,zmax=17,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 35.8617, "lon": 104.1954})
```

I will explain some of the most important features in the codes above.
- geojson: the geojson file of the country's map
- locations: a list or numpy array of the indexs or names of the different regions from the csv file that you'd like to plot its data on the map, which should match the 'id' part of the geojson file
- z: the data of different regions that you'd like plot from the csv file
- colorscale: the type of colorbar that you'd like to use to plot the data, which can also be customized
- zmin: the minimum value of z
- zmax: the maxmum value of z
- mapbox_center: the lattitude and longtitude of the country

## Outcome

The map that I drawed is as follows:

![Image of the Map](https://github.com/yg2619/Choropleth-Maps-in-Python/blob/master/choropleth-map-image.png)
