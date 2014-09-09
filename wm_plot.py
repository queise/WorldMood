#!/usr/bin/python

import sys
from datetime import datetime, timedelta
from bokeh.plotting import *
from bokeh.sampledata.autompg import autompg
from bokeh.objects import HoverTool
from numpy import *
import pandas as pd
from collections import OrderedDict

def F_plot(filename,df,jdict):
# Plots data from a pandas dataframe using bokeh.
# Info about dictionary jdict:
#  key            : journal abbr. 	eg: 'nyt'
#  jdict[key][0]  : full journal name 	eg: 'The New York times'
#  jdict[key][1]  : journal url		eg: 'www.nyt.com'
#  jdict[key][1]  : journal area	eg: 'USA'

# chooses colors for areas:
  areas4col = [ 'Africa', 'Asia', 'Australia', 'Europe', 'Latin Amer.', 'Mid. East', 'Russia', 'USA' ]
  colors    = [ 'darkgreen', 'orange', 'limegreen', 'blue', 'darkviolet', 'sienna', 'skyblue', 'red' ]
  d_a_color = dict(zip(areas4col,colors))  

# starts to prepare figure
  output_file(filename, mode="cdn")
  hold(True)
  figure(title="", x_axis_type="datetime", plot_width=900, plot_height=500, x_axis_label = "Date (m/d)", y_axis_label = "Mood Score",
         tools="pan,wheel_zoom,box_zoom,reset,previewsave,hover")

# plot the scores's average of areas together, along the dates, and the std deviation in grey quads
  F_plot_total(df)

# plot the score's average of each area, along the dates:
  F_plot_areaavg(df,jdict,d_a_color,True)

# plot the score of each journal:
#  F_plot_journals(df,jdict,d_a_color,True)

  hold(False)

  # cleans html ouput file for embedding in web:
  F_htmltoembed('wm.html','wm2embed.html')

def F_plot_total(df):
# plot the scores's average of areas together, along the dates, and the std deviation in grey quads
  scores = df.groupby("date")["score"]
  avg = scores.mean().values
  std = scores.std()
  dates = scores.mean().index.map(pd.Timestamp.date)
  line(dates, avg, line_color="grey", line_width=8, line_alpha=0.7, line_join="round")
  quad(left=dates,right=dates,bottom=avg-std, top=avg+std, fill_alpha=0.4, line_color="grey",line_width=15,line_alpha=0.3)

def F_plot_areaavg(df,jdict,d_a_color,hoverFT):
# plot the score's average of each individual area, along the dates:
  areas = []
  for journal in jdict:
    areas.append(jdict[journal][2])
  for area in sorted(list(set(areas))):
    tal = df[df["area"]==area]
    tal_gr = tal.groupby("date") ; tal_sc = tal_gr["score"] ; tal_av = tal_sc.mean() ; tal_std = tal_sc.std()
    x = tal_av.index
    y = tal_av
    if not hoverFT:
#     without hover:
      circle(x, y, size=17, alpha=0.4, line_color=d_a_color[area], fill_color=d_a_color[area], line_width=2, legend=area)
    if hoverFT:
#     with hover:
      N=len(x)
      arealist = [ area ]*N
      source = ColumnDataSource(data=dict( x=x, y=y, arealist=arealist) )
      circle(x, y, source=source, size=17, alpha=0.4, line_color=d_a_color[area], fill_color=d_a_color[area], line_width=2, legend=area)
      line(x, y, line_color=d_a_color[area], line_width=6, line_alpha=0.2, line_join="round")
      hover = [t for t in curplot().tools if isinstance(t, HoverTool)][0]
      hover.tooltips = OrderedDict([ ("Area", "@arealist"),("Score", "$y") ])

def F_plot_journals(df,jdict,d_a_color,hoverFT):
# plot the score of each journal:
  for journal in jdict:
    x = asarray(df[df["journal"]==jdict[journal][0]]["date"])
    y = asarray(df[df["journal"]==jdict[journal][0]]["score"])
    color = d_a_color[jdict[journal][2]]
    if not hoverFT:
#     without hover:
      circle(x, y, size=5, alpha=0.4, line_color=color,fill_color=color, line_width=2)
    if hoverFT:
#     with hover
      N=len(x)
      journallist = [ jdict[journal][0] ]*N
      arealist    = [ jdict[journal][2] ]*N
      urllist     = [ jdict[journal][1] ]*N 
      source = ColumnDataSource(data=dict( x=x, y=y, journallist=journallist, arealist=arealist, urllist=urllist) )
      diamond(x, y, source=source, size=8, alpha=0.4, line_color=color,fill_color=color, line_width=2)
      hover = [t for t in curplot().tools if isinstance(t, HoverTool)][0]
      hover.tooltips = OrderedDict([ ("Journal", "@journallist (@arealist)"), ("URL", "@urllist"), ("Score", "$y") ]) 

def F_htmltoembed(infile,outfile):
  words = ['html>', '<html', 'head>', '<meta', 'title>', 'body>']
  with open(infile) as oldfile, open(outfile, 'w') as newfile:
    for line in oldfile:
      if not F_any(word in line for word in words):
        newfile.write(line)
    oldfile.close() ; newfile.close()

def F_any(iterable):
    for element in iterable:
        if element:
            return True
    return False
