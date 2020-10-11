# -*- encoding: utf-8 -*-
'''
Created on 09.10.2020

@author: Vitalij Ruge
'''

import json
from os.path import dirname, join
import requests
import pandas as pd
    
def download_corona_data() -> pd.DataFrame:
    """download corona data from https://opendata.arcgis.com
     for germany and convert to :class:`pd.DataFrame`
    
    :rtype: :class: pd.DataFrame
    """
    tok = read_corona_token(k="de_corona")
    data_url = get_url_corona(tok=tok)
    r = requests.get(data_url, allow_redirects=True)
    raw_data = json.loads(r.content)['features']
    df = parse_data(raw_data)
    return df


def read_corona_token(k: str) -> str:
    with open(join(dirname(__file__), "token.json"), "r") as f:
        token = json.load(f)
    return token[k]


def get_url_corona(tok) -> str:
    return f'https://opendata.arcgis.com/datasets/{tok}.geojson'


def parse_data(raw_data) -> pd.DataFrame:
    df = pd.DataFrame([d["properties"] for d in raw_data])
    
    for c in ("Meldedatum", "Refdatum"):
        df[c] = pd.to_datetime(df[c], format='%Y/%m/%d %H:%M:%S')
    df.Datenstand = pd.to_datetime(df.Datenstand, format='%d.%m.%Y, %H:%M Uhr')
        
    df.set_index("ObjectId", inplace=True)
    df.IstErkrankungsbeginn.astype("bool")
        
    return df

