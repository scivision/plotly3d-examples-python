#!/usr/bin/env python

import plotly
import plotly.graph_objs as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('tests/mt_bruno_elevation.csv')

data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='elevations-3d-surface.html')
