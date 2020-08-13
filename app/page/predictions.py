# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions
            In order to see the predictions for a particular item use the search bar to find and item
            that is in the database, after finding the item in the resulting dropdown you will be redirected to that items page
            from there there will be  agraph with the predictions and a link to download the prediction data in CSV format

            # The Global Index Valuation (GIV)
            """
        ),

    ],
    md=4,
)

column2 = dbc.Col([])

layout = dbc.Row([column1, column2])
