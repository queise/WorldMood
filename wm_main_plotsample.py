#!/usr/bin/python

from wm_plot import *

def main():

# dictionary with info about the journals:
  jdict = {}
  jdict['nyt'] = [ 'The New York Times', 'www.nyt.com', 'USA' ]
  jdict['lat'] = [ 'Los Angeles Times', 'www.latimes.com', 'USA' ]
  jdict['bbc'] = [ 'BBC', 'www.bbc.com', 'Europe' ]
  jdict['elp'] = [ 'El Pais', 'www.elpais.com/elpais/inenglish.html', 'Europe' ]
  jdict['chd'] = [ 'China Daily Asia', 'www.chinadailyasia.com', 'Asia' ]
  jdict['toi'] = [ 'The Times of India', 'timesofindia.indiatimes.com', 'Asia' ]

# dataframe with the scores for each journal and date:
  df = pd.DataFrame( {u'date' : ['2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22',
                                 '2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22',
                                 '2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22',
                                 '2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22',
                                 '2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22',
                                 '2014-08-18', '2014-08-19', '2014-08-20', '2014-08-21', '2014-08-22'],
                      u'journal': ['nyt', 'nyt', 'nyt', 'nyt', 'nyt',
                                   'lat', 'lat', 'lat', 'lat', 'lat',
                                   'bbc', 'bbc', 'bbc', 'bbc', 'bbc', 
                                   'elp', 'elp', 'elp', 'elp', 'elp', 
                                   'chd', 'chd', 'chd', 'chd', 'chd', 
                                   'toi', 'toi', 'toi', 'toi', 'toi'],
                      u'area': ['USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA',
                                'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                                'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Asia'],
                      u'score': [-0.36363636, -0.225, -0.48979592, -0.02439024, -0.91489362,
                                 -0.3,  -0.48837209, -0.26666667, 0.15151515, -0.18918919,
                                 0.06666667, 0.24137931, -0.41025641, -0.35483871, -0.71428571,
                                 0.16666667, -0.88571429, -1.15625, -0.81481481, -0.45,
                                 0.83333333, 0.95348837, 0.87234043, 0.86, 0.52777778,
                                 -0.03225806, -1.05882353, -0.23076923, -0.88888889, -0.6] })

  df.date = pd.to_datetime(df.date,format='%Y-%m-%d')

  # call plot funtion in wm_plot
  F_plot('wm.html',df,jdict)

if __name__ == '__main__':
  main()
