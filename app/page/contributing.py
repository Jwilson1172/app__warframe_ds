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
        dcc.Markdown("""
            To Contribute to the project please visit the github page to see what issues are open,
            if there are none then take a look at the roadmap and open an issue for it,
            TravisCI should take care of the rest as far as rebuilding and deploying once the feature is peer reviewed
            """),
    ],
    md=4,
)

column2 = dbc.Col([])

layout = dbc.Row([column1, column2])
