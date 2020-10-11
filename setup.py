'''
Created on 15.08.2020

@author: Vitalij Ruge
'''

from setuptools import setup,find_packages

extras_require = dict(plot=["plotly"], widgets=["ipywidgets"])

extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(
    name='rocd',
    version="0.0.1",
    author="Vitalij Ruge",
    packages=find_packages(),
    url='https://github.com/vruge/corona_data_load_germany',
    description='read open corona data from https://opendata.arcgis.com',
    license="Apache License Version 2.0",
    python_requires='>=3.7',
    install_requires=["pandas", "requests", "numpy"],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Data",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)