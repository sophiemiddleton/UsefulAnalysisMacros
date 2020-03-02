import plotly.graph_objects as go
import matplotlib.pyplot as plt

import plotly as py

x0 = pd.read_csv('highstatdocas.csv')

fig = go.Figure()

data = [
    go.Histogram2dContour(
    x=x0['FitA0'],
    y=x0['TrueA0'],
    xbins=dict(start=-6000, end=6000, size=50),
    ybins=dict(start=-6000, end=6000, size=50),
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
        y = x0['TrueA0'],
        xaxis = 'x2',
        xbins=dict(start=-6000, end=6000, size=50),
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ),
    go.Histogram(
        x = x0['FitA0'],
        yaxis = 'y2',
        ybins=dict(start=-6000, end=6000, size=50),
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
