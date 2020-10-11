from .core import download_corona_data

try:
    from .widgets import get_widgets
except ImportError:
    def get_widgets(*arg, **kwargs):
        raise ImportError("ipywidgets is missing")
    
try:
    from .plot import plot
except ImportError:
    def plot(*arg, **kwargs):
        raise ImportError("plotly is missing")

    