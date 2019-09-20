#!/usr/bin/python3.6

import pandas as pd
import numpy as np
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#Activate the Dash Server---------------------------------------------------------------------------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
    
#Import the data-------------------------------------------------------------------------------------------------------------------

df = pd.read_csv("forboxplot.csv") #import csv

#Create the app layout- This displays ordered dropdown menu of gene names----------------------------------------------------------

app.layout = html.Div(children=[
    html.H4(children='Horizontal coverage for WES'), #Header
    dcc.Dropdown(
        id='genechoice',
        options=[{'label': i, 'value': i} for i in sorted(df.Gene.unique())], #only lists each gene once (unique), and sorts them alphabetically
        multi=False, placeholder='Enter HGNC Gene Symbol:'), #Prevents simultaneous selection of genes, show "Filter by gene" in selection box
    dcc.Graph(id='boxplot'),
    html.Div(id='children')
])

@app.callback(Output(component_id='boxplot', component_property='figure'),
              [Input(component_id='genechoice', component_property='value')])
def update_graph(dropdown_value):
    if dropdown_value is None:
        return "None selected"

#-----------------------------------------------------------------------------------------------------------------------------------

#How do I get the boxplot on there?

if __name__ == '__main__':
    app.run_server(debug=True)

#------------------------------------------------------------------------------------------------------------------------------------