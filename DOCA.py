#Author: S Middleton
#Date: Nov 2019
#Purpose: To analyse outcome of Cosmic Fit

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly as py
import pandas as pd

x0 = pd.read_csv('highstatdocas.csv')

fig = go.Figure()

data = [
    go.Histogram2dContour(
    x=x0['recodoca'],
    y=x0['truedoca'],
    xbins=dict(start=0, end=2.5, size=0.025),
    ybins=dict(start=0, end=2.5, size=0.025),
    colorscale='YlGnBu',
    zmax=10,
    nbinsx=14,
    nbinsy=14,
    zauto=False,
    #colorscale = 'Jet',
    contours = dict(
            showlabels = True,
            labelfont = dict(
                family = 'Raleway',
                color = 'black'
            )
        ),
        hoverlabel = dict(
            bgcolor = 'white',
            bordercolor = 'white',
            font = dict(
                family = 'Raleway',
                color = 'black'
            )
        )
),
    go.Histogram(
        y = x0['truedoca'],
        xaxis = 'x2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ),
    go.Histogram(
        x = x0['recodoca'],
        yaxis = 'y2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
               )
]

layout = go.Layout(
    autosize = False,
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    xaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    yaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    height = 600,
    width = 600,
    bargap = 0,
    hovermode = 'closest',
    showlegend = False
)

fig = go.Figure(data=data,layout=layout)
fig.show()
