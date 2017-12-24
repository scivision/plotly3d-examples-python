#!/usr/bin/env python
"""
slice plot
https://nbviewer.jupyter.org/github/empet/Plotly-plots/blob/master/Plotly-Slice-in-volumetric-data.ipynb
"""
import plotly
import plotly.graph_objs as pgo
import numpy as np

pl_BrBG=[[0.0, 'rgb(84, 48, 5)'],
         [0.1, 'rgb(138, 80, 9)'],
         [0.2, 'rgb(191, 129, 45)'],
         [0.3, 'rgb(222, 192, 123)'],
         [0.4, 'rgb(246, 232, 195)'],
         [0.5, 'rgb(244, 244, 244)'],
         [0.6, 'rgb(199, 234, 229)'],
         [0.7, 'rgb(126, 203, 192)'],
         [0.8, 'rgb(53, 151, 143)'],
         [0.9, 'rgb(0, 101, 93)'],
         [1.0, 'rgb(0, 60, 48)']]

def get_the_slice(x,y,z, surfacecolor,  colorscale=pl_BrBG, showscale=False):
    """https://plot.ly/python/reference/#surface"""

    return pgo.Surface(x=x,
                   y=y,
                   z=z,
                   surfacecolor=surfacecolor,
                   colorscale=colorscale,
                   showscale=showscale)
                   

def get_lims_colors(surfacecolor):# color limits for a slice
    return np.min(surfacecolor), np.max(surfacecolor)


alpha=np.pi/5
x=np.linspace(-2,2, 50)
y=np.linspace(-2,2, 50)
x,y=np.meshgrid(x,y)
z=-x*np.tan(alpha)

volume=lambda x,y,z: x*np.exp(-x**2-y**2-z**2)

x=np.linspace(-2,2, 50)
y=np.linspace(-2,2, 50)
x,y=np.meshgrid(x,y)
z=np.zeros(x.shape)
surfcolor_z=volume(x,y,z)
sminz, smaxz=get_lims_colors(surfcolor_z)

slice_z=get_the_slice(x,y,z, surfcolor_z)

x=np.linspace(-2,2, 50)
z=np.linspace(-2,2, 50)
x,z=np.meshgrid(x,y)
y=-0.5*np.ones(x.shape)
surfcolor_y=volume(x,y,z)
sminy, smaxy=get_lims_colors(surfcolor_y)
vmin=min([sminz, sminy])
vmax=max([smaxz, smaxy])
slice_y=get_the_slice(x,y,z, surfcolor_y)


axis = dict(showbackground=True,
            backgroundcolor="rgb(230, 230,230)",
            gridcolor="rgb(255, 255, 255)",
            zerolinecolor="rgb(255, 255, 255)",
            )


layout = pgo.Layout(
         title='Slices in volumetric data',
         width=700,
         height=700,
         scene=pgo.Scene(xaxis=pgo.XAxis(axis),
                     yaxis=pgo.YAxis(axis),
                     zaxis=pgo.ZAxis(axis, range=[-2,2]),
                     aspectratio=dict(x=1,
                                      y=1,
                                      z=1
                                     ),
                    )
        )



surfcolor_obl=volume(x,y,z)

smino, smaxo=get_lims_colors(surfcolor_obl)
vmin=min([sminz, smino])
vmax=max([smaxz, smaxo])

slice_obl=get_the_slice(x,y,z, surfcolor_obl)
slice_obl.update( cmin=vmin, cmax=vmax, showscale=True)

slice_z.update( cmin=vmin,
                cmax=vmax)

fig = pgo.Figure(data=pgo.Data([slice_z, slice_obl]), layout=layout)

plotly.offline.plot(fig, filename='Slice-volumetric-2.html')



