# rera_scrapping-data
Code to scrap information from the maharashtra rera agents portal and saved them as .csv files, after extracting.

Used Selenium to automate the form fill process and further scraping the data.
Used find_element_by_xpath extensively to find the required data and appended the required data to a list to make it easy for me to create a dataframe from it. 

Used pandas .read_html() to read the tables in the html directly.
Used a for loop to find the required tables to avoid the case of wrong index especially for the Agents that do not have all the tables in their form.

Made sure that the index of xpath stays between 1 and 50
Made sure the loop goes to the next page without breaking in between. 

Didn't extract all 3931 entries from the site since extracting around 1000 entries proves that the code works without any problems.
