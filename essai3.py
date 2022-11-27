import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np

state = ox.gdf_from_place('Georgia, US')
ox.plot_shape(ox.project_gdf(state))

# Defining the map boundaries
north, east, south, west = 33.798, -84.378, 33.763, -84.422
# Downloading the map as a graph object
G = ox.graph_from_bbox(north, south, east, west, network_type = 'drive')
# Plotting the map graph
ox.plot_graph(G)
