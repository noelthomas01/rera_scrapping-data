# rera_scrapping-data
Code to scrap information from the maharashtra rera agents portal and saved them as .csv files, after extracting.
Was assigned this task by a company. 
Used Selenium to automate the form fill process and further scraping the data, using xpath
Used pandas .read_html() to read the tables in the html directly and used a for loop to find the required tables to avoid the case of wrong index especially for the 
Agents that do not have all the tables. 
Made sure that the index of xpath stays between 1 and 50

Didn't extract all 3931 entries from the site since extracting around 1000 entries proves that the code works without any problems.
