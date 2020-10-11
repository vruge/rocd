# -*- encoding: utf-8 -*-
'''
Created on 11.10.2020

@author: Vitalij Ruge
'''

import numpy as np
import ipywidgets as widgets
from typing import Dict

def get_widgets(df) -> Dict[str, widgets.Dropdown]:
    """return widgets
    
    """
    Bundesland = np.sort(df.Bundesland.unique())
    Landkreis = np.sort(df.Landkreis.unique())
    Geschlecht = df.Geschlecht.unique()
    Altersgruppe = np.sort(df.Altersgruppe.unique())
    
    Bundesland = np.insert(Bundesland, 0, None)
    Landkreis = np.insert(Landkreis, 0, None)
    Geschlecht = np.insert(Geschlecht, 0, None)
    Altersgruppe = np.insert(Altersgruppe, 0, None)
    
    Bundesland_widget = widgets.Dropdown(
        options=Bundesland,
        description='Bundesland:',
        disabled=False,
    )
    
    Landkreis_widget = widgets.Dropdown(
        options=Landkreis,
        description='Landkreis:',
        disabled=False,
    )
    
    Geschlecht_widget = widgets.Dropdown(
        options=Geschlecht,
        description='Geschlecht:',
        disabled=False,
    )
    
    Altersgruppe_widget = widgets.Dropdown(
        options=Altersgruppe,
        description='Altersgruppe:',
        disabled=False,
    )
     
    return dict(Bundesland = Bundesland_widget, Landkreis=Landkreis_widget, Geschlecht=Geschlecht_widget, Altersgruppe=Altersgruppe_widget)