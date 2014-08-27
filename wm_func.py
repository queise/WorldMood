#!/usr/bin/python

import sys
import re

def F_getdictafinn(file):
  # Builds a dictionary of the words and their scores from the list in the file
  afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open(file) ]))
  return afinn

def F_textfromfile(file):
  try:
    f = open(file,'r')
    str = f.read()
    f.close()
  except IOError:
    print 'FILE:', file, ' DOES NO EXISTS'
    str = ''
  return str

def F_relevantfromtext(text,dictwordsc):
  # returns the words of the text that are in the dic
  listrelevtext = []
  for word in text.lower().split():
    if word in dictwordsc:
      listrelevtext.append(word)
  return listrelevtext

def F_listscore(dictwordsc,listwords):
 # Summs the score of all the words in a list
  score = sum(map(lambda word: dictwordsc.get(word, 0), listwords))
  print float(score)," / ",len(listwords)
  try:
    score = float(score) / len(listwords)
  except ZeroDivisionError:
    pass
  return score

def F_textscore(dictwordsc,text):
  # Summs the score of all the words in a text
  score = sum(map(lambda word: dictwordsc.get(word, 0), text.lower().split()))
  try:
    score = float(score) / len(text.split())
  except ZeroDivisionError:
    pass
  return score

def F_newstextfromjournalhtml(journal,html):
  # from a dirty html string it takes only the relevant text of the news and puts it in a single string   
  if journal=='nyt':
    matchs = re.findall(r'p.class..summary.>(.*?)</p>',html, re.DOTALL)
    matchs += re.findall(r'html\">\s*([\w\s\,\']*)\s*</a>\s*\n*<span',html, re.DOTALL)
    matchs += re.findall(r'story-heading\">([\w\s\,\']*)<span',html, re.DOTALL)
  elif journal=='lat':
    matchs = re.findall(r'ListTitle_a\">(.*?)</a><span',html, re.DOTALL)
    matchs += re.findall(r'content_text\">(.*?)</span',html, re.DOTALL)
    matchs += re.findall(r'column.html\">(.*?)</a>',html, re.DOTALL)
  elif journal=='wsj':
    matchs = re.findall(r'<!--p>(.*?)</p-->',html, re.DOTALL)
    matchs += re.findall(r'\">([\w\s\,\'\-\:\&\#\;]*)\n*</a></h2></li>',html, re.DOTALL)
  elif journal=='alj':
    matchs = re.findall(r'indexSummaryText.>(.*?)</div>',html, re.DOTALL)
  elif journal=='teh':
    matchs = re.findall(r'contentpagetitle\s\'\s>(.*?)</a></h2>',html, re.DOTALL)
    matchs += re.findall(r'/><br>(.*?)\.\.\.</span></span>',html, re.DOTALL)
    matchs += re.findall(r'class=\'\s\'\s>(.*?)</a></span><br',html, re.DOTALL)
  elif journal=='afr':
    matchs = re.findall(r'</a></b>(.*?)\n*</font></br>',html, re.DOTALL)
    matchs += re.findall(r'\d{5}\'>([\w\s\,]*)</a><br>',html, re.DOTALL)
  elif journal=='s24':
    matchs = re.findall(r'\d{5}\">([\w\s\,\']*)</a></li>',html, re.DOTALL)
  elif journal=='bbc':
    matchs = re.findall(r'media.title.>(.*?)</span>',html, re.DOTALL)
    matchs += re.findall(r'</span>([\w\s\,\']*)</a>\s*</li>',html, re.DOTALL)
    matchs += re.findall(r'content\">([\w\s\,\']*)</a>\s*</li>',html, re.DOTALL)
    matchs += re.findall(r'hero_summary\">(.*?)</p>\s*</*div>',html, re.DOTALL)
  elif journal=='spi':
    matchs = re.findall(r'rticle.intro.clearfix\">\s*(.*?)<span',html, re.DOTALL)
    matchs += re.findall(r'headline.intro\">(.*?)</span>',html, re.DOTALL)
  elif journal=='elp':
    matchs = re.findall(r'Ver.noticia.>([\w\s\,\']*)</a><[/li]*[/h2]*>',html, re.DOTALL)
    matchs += re.findall(r'</a>\s*</div>\s*<p>(.*?)</p>\n</*div>',html, re.DOTALL)
    matchs += re.findall(r'</a>\s*</h\d>\s*<p>(.*?)</p>\n</*div>',html, re.DOTALL)
    matchs += re.findall(r'</span>\s*</div>\s*<p>(.*?)</p>\n</*div',html, re.DOTALL)
  elif journal=='fra':
    matchs = re.findall(r'class.\"desc\">([\w\s\,\'\-\:]*)</p>',html, re.DOTALL)
    matchs += re.findall(r'\.\.\.\">(.*?)</a>',html, re.DOTALL)
  elif journal=='ita':
    matchs = re.findall(r'html\">([\w\s\,\'\-\:\&\#\;]*)</a></h3>',html, re.DOTALL)
    matchs += re.findall(r'abs">([\w\s\,\'\-\:\&\#\;]*)</p>',html, re.DOTALL)
    matchs += re.findall(r'stit\"><p>(.*?)</p></div>',html, re.DOTALL)
    matchs += re.findall(r'category\">([\w\s\,\'\-\:\&\#\;]*)</em><a',html, re.DOTALL)
  elif journal=='chd':
    matchs = re.findall(r'span>\s\n\n<p>(.*?)</p>\n</div>',html, re.DOTALL)
    matchs += re.findall(r'pdesc02.>(.*?)</p>',html, re.DOTALL)
    matchs += re.findall(r'pmart.>(.*?)</p>',html, re.DOTALL)
  elif journal=='toi':
    matchs = re.findall(r'cms.>([\w\s\,]*)</a></li>',html, re.DOTALL)
    matchs += re.findall(r'<stname>(.*?)</stname>',html, re.DOTALL)
  elif journal=='jap':
    matchs = re.findall(r'<p>\n\t+(.*?)\t+</p>\n\t+</',html, re.DOTALL)
    matchs += re.findall(r'\">([\w\s\,]*)</a></h1>',html, re.DOTALL)
    matchs += re.findall(r'class=\"featured_excerpt\s*\">(.*?)\t+</p>',html, re.DOTALL)
    matchs += re.findall(r'class=\"entry\">\n\t+<p>\n\t+(.*?)\t+</p>',html, re.DOTALL)
  elif journal=='ind':
    matchs = re.findall(r'php\">([\w\s\,\.\'\-\:\;\?\&\#]*)</a>\s*</h\d>',html, re.DOTALL)
    matchs += re.findall(r'></a>\s*<p>(.*?)<a\shref',html, re.DOTALL)
  elif journal=='nau':
    matchs = re.findall(r'\">([\w\s\,\.\'\-\:\;\?\&\#]*)</a></li>',html, re.DOTALL)
    matchs += re.findall(r'\"standfirst\">\s*([\w\s\,\.\'\-\:\;\?\&\#]*)\s*</p>',html, re.DOTALL)
    matchs += re.findall(r'\"standfirst\">\s*([\w\s\,\.\'\-\:\;\?\&\#]*)\s*<span',html, re.DOTALL)
  elif journal=='rio':
    matchs = re.findall(r'right\"></i>([\w\s\,\'\-\:]*)\s+</a>\s+</h2>',html, re.DOTALL)
    matchs += re.findall(r'\"\s*>([\w\s\,\'\-\:]*)</a></h2>',html, re.DOTALL)
  elif journal=='pla':
    matchs = re.findall(r'Itemid=1\"\s>(.*?)</a></td>',html, re.DOTALL) #</td>
    matchs += re.findall(r'Itemid=1\">([\w\s\,\'\-\:]*)</li>',html, re.DOTALL)
    matchs += re.findall(r'Itemid=1\">([\w\s\,\'\-\:]*)</a></div>',html, re.DOTALL) #</td>
    matchs += re.findall(r'\d\d\:\d\d</span>(.*?)</p></div>',html, re.DOTALL)
  elif journal=='msu':
    matchs = re.findall(r'\">([\w\s\,\'\-\:\&\#\;]*)</a></li>',html, re.DOTALL)
    matchs += re.findall(r'\">([\w\s\,\'\-\:\&\#\;]*)<small>',html, re.DOTALL)
    matchs += re.findall(r'<span>([\w\s\,\'\-\:\&\#\;]*)</span>\s*</a>\s*</li>',html, re.DOTALL)
    matchs += re.findall(r'<span>([\w\s\,\'\-\:\&\#\;]*)</span>\s*</a>\s*</dd>',html, re.DOTALL)
  elif journal=='arg':
    matchs = re.findall(r'\">([\w\s\,\'\-\:\&\#\;]*)</a></li>',html, re.DOTALL)
    matchs += re.findall(r'</div>\s*<p>(.*?)</p>',html, re.DOTALL)
    matchs += re.findall(r'self\">([\w\s\,\'\-\:\&\#\;]*)</a></h2>',html, re.DOTALL)
  elif journal=='pra':
    matchs = re.findall(r'0\/\">([\w\s\,\'\-\:\&\#\;]*)</a>\s*<div',html, re.DOTALL)
    matchs += re.findall(r'0\/\">([\w\s\,\'\-\:\&\#\;]*)</a></li',html, re.DOTALL)
  elif journal=='stp':
    matchs = re.findall(r'story\_text\_o\">(.*?)</p></a>',html, re.DOTALL)
    matchs += re.findall(r'story\_link\_o\">(.*?)</a></h2',html, re.DOTALL)
  else:
    print "\n ERROR: journal not recognized \n"
    sys.exit(1)
  str_news = ''
  for match in matchs:
    str_news += match + ' '
#    print match
  return str_news
