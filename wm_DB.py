#!/usr/bin/python

import MySQLdb as mdb
import pandas.io.sql as psql

def F_conDB(dbname):
  try: 
    con = mdb.connect('localhost', 'wmuser', '--removed--', dbname);
    cur = con.cursor()
  except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
  return con

def F_createtableinDB(cur,tabname):
  cur.execute("DROP TABLE IF EXISTS " + tabname)
  cur.execute("CREATE TABLE " + tabname + "(date text, journal text, area text, numwords int, score real)")

def F_insertinDB(cur,tabname,date,journal,area,numwords,score):
  if numwords==0:
    cur.execute("INSERT INTO " + tabname + " VALUES( '"+date+"', '"+journal+"' , '"+area+"' , null , null )")
  else:
    cur.execute("INSERT INTO " + tabname + " VALUES( '"+date+"', '"+journal+"' , '"+area+"' ,"+str(numwords)+","+str(score)+")")

def F_deletefromDB(cur,tabname,date,journal):
  cur.execute("DELETE FROM " + tabname + " WHERE date=" + date + " AND journal='" + journal+"'")

def F_showtableDB(cur,tabname):
  cur.execute("SELECT * FROM " + tabname)
  rows = cur.fetchall()
  for row in rows:
    print row

def F_getdffromDB(con,tabname):
  df_mysql = psql.read_sql('SELECT * FROM ' + tabname + ';', con)
  print 'loaded dataframe from MySQL. records:', len(df_mysql)
  return df_mysql
