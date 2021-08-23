# Project Overview
This project uses python's sqlalchemy library in order to query a database (sqlite in this case), retrieve data, organize it in a pandas dataframe and produce an analysis. 
As a bonus point, a function has been added that converts Fahrenheit temperatures into Celsius. The temperatures in celsius are recorded in a separate column.\

# Software Used:
* Jupyter notebook
* Python (aqlalchemy, numpy, pandas)
* Sqlite
* Flask (see app.py)

# Overview of the analysis: 
The purpose of this analysis is to underdstand temperature trends for the months of June and December for an island called Oahu, in order to determine if a surf and ice cream shop business is sustainable year-round.

# Results: 
 - The mean temperatures in December on the island of Oahu are a bit lower than the temperatures in June, but stays above 20 degress C (70 degress F). 
 - In December, the temperatures can fluctuate slightly more during the day.
 - Dataframe summary screencaptures:
 
 ![June Dataframe](https://github.com/githubteodora/surfs_up/blob/main/June%20desc.PNG)
 ![Dec Dataframe](https://github.com/githubteodora/surfs_up/blob/main/Dec%20desc.PNG)

# Recommendations:
 - It is necessary to understand when people go surfing on the island of Oahu - are they more reluctant to suft in cooler temperatures?
 - It is also necessary to analyze weather conditions - rain, fog, storms, etc. By looking at temperatures alone, it is difficult to make a good judgement about the sustainability of a surf and ice-cream shop.

