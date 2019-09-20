#!/usr/bin/python3.6

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

#Activate the Dash Server----------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
    
#Import the data------------------------------------------------------------

df = pd.read_csv("forboxplot.csv") #import csv

#Create the app layout- This displays ordered dropdown menu of gene names-----------------

app.layout = html.Div(children=[
    html.H4(children='Horizontal coverage for WES'), #Header
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in sorted(df.Gene.unique())], #only lists each gene once (unique), and sorts them alphabetically
        multi=False, placeholder='Enter HGNC Gene Symbol:'), #Prevents simultaneous selection of genes, show "Filter by gene" in selection box
    html.Div(id='dropdown-container')
])

@app.callback(Output('dropdown-container', 'children'),
              [Input('dropdown', 'value')])
def display_table(dropdown_value):
    

    dff = df[df.state.str.contains('|'.join(dropdown_value))]
    return generate_table(dff)

if __name__ == '__main__':
    app.run_server(debug=True)
