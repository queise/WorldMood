#!/usr/bin/python

import sys
from datetime import datetime, timedelta
from bokeh.plotting import *
from bokeh.sampledata.autompg import autompg
from bokeh.objects import HoverTool
from numpy import *
import bokeh as bk
import pandas as pd
import MySQLdb
from collections import OrderedDict

def F_plot(filename,df,journals,areas):

  output_file(filename, mode="cdn")

  hold(True)
  figure(title="", x_axis_type="datetime", plot_width=800, plot_height=500, ylabel="Mood score",
         tools="pan,wheel_zoom,box_zoom,reset,previewsave,hover")

# 1) plot the scores's average of areas together, along the dates, and the std deviation in grey quads:
  scores = df.groupby("date")["score"]
  avg = scores.mean().values
  std = scores.std()
  dates = scores.mean().index.map(pd.Timestamp.date)
  line(dates, avg, line_color="grey", line_width=8, line_alpha=0.7, line_join="round")
  quad(left=dates,right=dates,bottom=avg-std, top=avg+std, fill_alpha=0.4, line_color="grey",line_width=15,line_alpha=0.3)
  
# 2) plot the score's average of each individual area, along the dates:
  areas4col = [ 'USA', 'Europe','Africa','Asia','Australia','Mid. East','Latin Amer.','Russia']
  colors    = [ 'red', 'blue', 'darkgreen', 'orange', 'limegreen','sienna', 'darkviolet', 'skyblue']
  d_a_color = dict(zip(areas4col,colors))

  for area in list(set(areas)):
    tal = df[df["area"]==area]
    tal_gr = tal.groupby("date") ; tal_sc = tal_gr["score"] ; tal_av = tal_sc.mean()
    x = tal_av.index
    y = tal_av
#   without hover:
    circle(x, y, size=15, alpha=0.4, line_color=d_a_color[area], fill_color=d_a_color[area], line_width=2, legend=area)
#   with hover:
#    N=len(x)
#    arealist = [ area ]*N
#    source = ColumnDataSource(data=dict( x=x, y=y, arealist=arealist) )
#    circle(x, y, source=source, size=15, alpha=0.4, line_color=d_a_color[area], fill_color=d_a_color[area], line_width=2, legend=area)
#    hover = [t for t in curplot().tools if isinstance(t, HoverTool)][0]
#    hover.tooltips = OrderedDict([ ("area", "@arealist"),("score", "$y") ])

# 3) plot the score of each journal:
  d_j_area = dict(zip(journals,areas))
  for journal in journals:
    x = asarray(df[df["journal"]==journal]["date"])
    y = asarray(df[df["journal"]==journal]["score"])
    color = d_a_color[d_j_area[journal]]
#   without hover:
#    circle(x, y, size=3, alpha=0.4, line_color=color,fill_color=color, line_width=2)
#   with hover
    N=len(x)
    journallist = [ journal ]*N
    source = ColumnDataSource(data=dict( x=x, y=y, journallist=journallist) )
    circle(x, y, source=source, size=3, alpha=0.4, line_color=color,fill_color=color, line_width=2)
    hover = [t for t in curplot().tools if isinstance(t, HoverTool)][0]
    hover.tooltips = OrderedDict([ ("journal", "@journallist"),("score", "$y") ])   

  hold(False)

  show()

  # cleans html ouput file for embedding in web:
  F_htmltoembed('wm.html','wm2embed.html')

def F_htmltoembed(infile,outfile):
  words = ['html', 'head>', '<meta', 'title>', 'body>']
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
