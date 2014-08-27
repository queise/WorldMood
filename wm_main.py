#!/usr/bin/python

import sys
from wm_func import *
from wm_DB import *
from wm_plot import *
from wm_plot2 import *

def main():

# Lists of journals, areas  and dates to be analysed:
  journals = ['nyt', 'lat', 'wsj', 'alj', 'teh', 'afr', 's24',
               'bbc', 'spi', 'elp', 'fra', 'ita', 'chd', 'toi', 'jap', 'ind', 'nau',
               'rio', 'pla', 'msu', 'arg', 'pra', 'stp' ]
  areas    = ['USA' ,'USA' ,'USA', 'Mid. East', 'Mid. East', 'Africa', 'Africa',
              'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia', 'Asia', 'Australia',
              'Latin Amer.', 'Latin Amer.', 'Latin Amer.', 'Latin Amer.', 'Russia', 'Russia' ]
  d_area = dict(zip(journals,areas))
  year   = '2014'
  month  = '08'
  daymin = 15
  daymax = 25
  dates = []
  for i in xrange(daymax-daymin+1):
    dates.append(str("%02d" % (daymin + i))+month+year)
    
# creates dictionary with keywords and scores:
  dictwordsc = F_getdictafinn("AFINN-111.txt")

# connects to database
  con = F_conDB('wm')
  with con:
    cur = con.cursor()

# creates table (COMMENT if you dont want existing table to be removed)
  F_createtableinDB(cur,'wmtab')

  for journal in journals:
    for date in dates:
      print journal, date

      # reads from the html file (also tried with BeautifulSoup but was more slower)
      html = F_textfromfile("html/" + journal + date + ".html")

      # cleans html text and turns it into a string of the news:
      newstext = F_newstextfromjournalhtml(journal,html)

      # chooses only the words in the text that give points:
      relevwords = F_relevantfromtext(newstext,dictwordsc)

      # calculates total score from text or list (sum of score of words divided by number of words):
      score = F_listscore(dictwordsc,relevwords)

      # inserts score in database:
      F_insertinDB(cur,'wmtab',date,journal,d_area[journal],len(relevwords),score)

      # deletes date entry from database;
#      F_deletefromDB(cur,'wmtab',date,journal)

  # show table from database:
  F_showtableDB(cur,'wmtab')

  # gets dataframe from database:
  df = F_getdffromDB(con,'wmtab')
  df.date = pd.to_datetime(df.date,dayfirst=True,format='%d%m%Y')

  # plots
  F_plot('wm.html',df,journals,areas)

  # commits and closes database:
  con.commit()
  con.close()

if __name__ == '__main__':
  main()
