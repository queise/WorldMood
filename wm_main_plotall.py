#!/usr/bin/python

import sys
from wm_func import *
from wm_DB import *
from wm_plot import *

def main():

# The info about the journals to be analysed is read from csv file and stored in dictionary:
# Eg: for a journal abbr like 'nyt': jdict['nyt'][0] is the full journal name, [1] the url and [2] the area
  jdict = F_createdictfromcsv('journalsinfo.csv')

# connects to database
  con = F_conDB('wm')
  with con:
    cur = con.cursor()

  # show table from database:
  F_showtableDB(cur,'wmtab')

#  sys.exit(1)

  # gets dataframe from database:
  df = F_getdffromDB(con,'wmtab')
  df.date = pd.to_datetime(df.date,dayfirst=True,format='%d%m%Y')

  # plots
  F_plot('wm.html',df,jdict)

  # commits and closes database:
  con.commit()
  con.close()

if __name__ == '__main__':
  main()
