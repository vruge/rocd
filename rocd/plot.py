# -*- encoding: utf-8 -*-
'''
Created on 11.10.2020

@author: Vitalij Ruge
'''
from typing import Dict
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot(df, filte_attr: Dict[str, str], smooth_seq: str = "14D") -> None:
    df_filter = df.copy()
    for k,v in filte_attr.items():
        if v is not None:
            df_filter = df_filter[df_filter[k]==v]
    
    if df_filter.shape[0] > 1:
        df_smooth_data = df_filter[["Refdatum", "AnzahlFall", "AnzahlTodesfall"]].groupby("Refdatum").sum().rolling(smooth_seq).mean()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=df_smooth_data.AnzahlFall.index, y=df_smooth_data.AnzahlFall.values, name="AnzahlFall"), secondary_y=False)
        fig.add_trace(go.Scatter(x=df_smooth_data.AnzahlTodesfall.index, y=df_smooth_data.AnzahlTodesfall.values, name="AnzahlTodesfall"), secondary_y=True)
        fig.show()
    else:
        print("No data")