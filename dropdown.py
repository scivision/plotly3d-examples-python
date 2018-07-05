#!/usr/bin/env python
"""https://plot.ly/python/dropdowns/"""
import plotly
import plotly.graph_objs as go
import numpy as np

fn = 'data/volcano.csv'


def main():
    dat = np.loadtxt(fn, delimiter=',', skiprows=1)

    data = [go.Surface(z=dat)]  # , colorscale='Viridis')]

    layout = go.Layout(
        width=800,
        height=900,
        autosize=False,
        margin={'t': 0, 'b': 0, 'l': 0, 'r': 0},
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230, 230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            aspectratio=dict(x=1, y=1, z=0.7),
            aspectmode='manual'
        )
    )

    updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=['type', 'surface'],
                    label='3D Surface',
                    method='restyle'
                ),
                dict(
                    args=['type', 'heatmap'],
                    label='Heatmap',
                    method='restyle'
                )
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.1,
            xanchor='left',
            y=1.1,
            yanchor='top'
        ),
    ])

    annotations = list([
        dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
    ])
    layout['updatemenus'] = updatemenus
    layout['annotations'] = annotations

    fig = dict(data=data, layout=layout)

    plotly.offline.plot(fig, filename='dropdown.html')


if __name__ == '__main__':
    main()
