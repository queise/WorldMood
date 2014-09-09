#!/usr/bin/python

import sys
from wm_func import *
from wm_DB import *
from wm_plot import *

def main():

# The info about the journals to be analysed is read from csv file and stored in dictionary:
  jdict = F_createdictfromcsv('journalsinfo.csv')

# Dates for which the journal headlines will be analysed and stored in database:
  year   = '2014' ; month  = '09' ; daymin = 01 ; daymax = 07 ; dates = []
  for i in xrange(daymax-daymin+1):
    dates.append(str("%02d" % (daymin + i))+month+year)

# creates dictionary with keywords and scores  
  dictwordsc = F_getdictafinn("AFINN/AFINN-111.txt")

# connects to database
  con = F_conDB('wm')
  with con:
    cur = con.cursor()

# creates table (COMMENT if you dont want existing table to be removed)
#  F_createtableinDB(cur,'wmtab')

  for journal in jdict:
    for date in dates:
      print journal, jdict[journal][0], jdict[journal][1], jdict[journal][2], date

      # reads from the html file (also tried with BeautifulSoup but was slower)
      html = F_textfromfile("html/" + journal + date + ".html")

      # cleans html text and turns it into a string of the news:
      newstext = F_newstextfromjournalhtml(journal,html)

      # chooses only the words in the text that give points:
      relevwords = F_relevantfromtext(newstext,dictwordsc)

      # calculates total score from text or list (sum of score of words divided by number of words):
      score = F_listscore(dictwordsc,relevwords)

      # inserts journal info and score in database:
      F_insertinDB(cur,'wmtab',date,jdict[journal][0],jdict[journal][2],len(relevwords),score)

      # deletes date entry from database;
#      F_deletefromDB(cur,'wmtab',date,jdict[journal][0])

  # show table from database:
  F_showtableDB(cur,'wmtab')

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
