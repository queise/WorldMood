WorldMood
=========

These python scripts do a **simple** analysis of the headlines of some news websites (regex), attribute a score (with the word list afinn [1]), deal with the data (mysql and pandas) and plot the results (bokeh).

Check the results at: http://TheMoodOfTheWorld.weebly.com

- [wm_main.py](wm_main.py) :    Main structure, see the comments on the script for the details

- [wm_func.py](wm_func.py) :    Functions... including the re.findall that extract the headlines from dirty htmls

- [wm_DB.py](wm_DB.py)   :    Functions that insert and extract from the database (MySQLdb and pandas.io.sql)

- [wm_plot.py](wm_plot.py)    :    Interactive plot of the results with bokeh.

- [journalsinfo.csv](journalsinfo.csv) : With the name, web and area of each news website analysed.

and also:

- [wm_main_plotall.py](wm_main_plotall.py)    :  Useful to just plot all that is already in the database
 
- [wm_main_plotsample.py](wm_main_plotsample.py) :  Plots a sample dataframe, to test the plotting commands with no need of databases nor htmls



[1] http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
