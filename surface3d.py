#!/usr/bin/env python
import plotly
import plotly.graph_objs as go
import numpy as np

fn = 'tests/mt_bruno_elevation.csv'

Z = np.loadtxt(fn,delimiter=',',skiprows=1,usecols=range(1,25))

data = [
    go.Surface(
        z = Z
    )
]
#layout = go.Layout(
#    title='Mt Bruno Elevation',
#    autosize=False,
#    width=500,
#    height=500,
#    margin=dict(
#        l=65,
#        r=50,
#        b=65,
#        t=90
#    )
#)
fig = go.Figure(data=data)#, layout=layout)
plotly.offline.plot(fig, filename='elevations-3d-surface.html')
