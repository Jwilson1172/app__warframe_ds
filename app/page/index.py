# -*- coding: utf-8 -*-
"""Application index.

This is the first page users will see when they visit your app.
"""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown("""
            # Warframe Market Predictions
            using this app you can see various predictions to the PC-Player Market values on WarFrame
            Sorry that is is only in PC if you would like to contribute please visit the
            contribution page to see what you can help with.
            """),
        dcc.Link(dbc.Button("Your Call To Action", color="primary"),
                 href="/predictions"),
        dcc.Link(dbc.Button("Contributing to the Project", color="primary"),
                 href="/contributing")
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

column2 = dbc.Col([
    dcc.Graph(figure=fig),
])

layout = dbc.Row([column1, column2])
