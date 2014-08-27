worldmood
=========

These python scripts do a **simple** analysis of the headlines of some online journals (regex), attribute a score (with the word list afinn [1]), deal with the data (mysql and pandas) and plot the results (bokeh).

- wm_main.py :    Main structure, see the comments on the script for the details

- wm_func.py :    Functions... including the re.findall that extract the headlines from dirty htmls

- wm_DB.py   :    Functions that insert and extract from the database (MySQLdb and pandas.io.sql)

- wm_plot    :    Interactive plot of the results with bokeh.

and:

- wm_main_onlyplot.py:  Useful to just execute the plot (with a simpler example dataframe)



[1] http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
