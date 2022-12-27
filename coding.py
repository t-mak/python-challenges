##14.4 CONCATENATING

##from PyPDF2 import PdfFileMerger
##from pathlib import Path
##
##pdf_merger = PdfFileMerger()

##
##print(Path.home())
##
##reports_dir = (
##    Path.home() /
##    "OneDrive" /
##    "Documents" /
##    "ch14-interact-with-pdf-files" /
##    "practice_files" /
##    "expense_reports"
##)

##
##
##print(reports_dir)
##
##expense_reports = list(reports_dir.glob("*.pdf"))
##expense_reports.sort()

##
##for path in expense_reports:
##    print(path.name)
##
##for path in expense_reports:
##    pdf_merger.append(str(path))

##
##with Path("expense_reports.pdf").open(mode="wb") as output_file:
##    pdf_merger.write(output_file)


##14.4 MERGING

##from PyPDF2 import PdfFileMerger
##from pathlib import Path
##
##pdf_merger = PdfFileMerger()

##
##reports_dir = (
##    Path.home() /
##    "OneDrive" /
##    "Documents" /
##    "ch14-interact-with-pdf-files" /
##    "practice_files" /
##    "quarterly_report"
##)
##
##report_path = reports_dir / "report.pdf"
##toc_path = reports_dir / "toc.pdf"
##
##pdf_merger.append(str(report_path))
##
##pdf_merger.merge(1, str(toc_path))

##
##with Path("full_report.pdf").open(mode="wb") as output_file:
##    pdf_merger.write(output_file)


##14.5 ROTATING PAGES





******
#Databases

import sqlite3



#####1
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     query = "SELECT datetime('now', 'localtime');"
#     time = cursor.execute(query).fetchone()[0]
# print(time)


#####2
# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()
# cursor.execute(
#     """CREATE TABLE People(
#         FirstName TEXT,
#         LastName TEXT,
#         Age INT
#     );"""
# )

# cursor.execute(
#     """INSERT INTO People VALUES(
#         'Ron',
#         'Obvious',
#         42
#     );"""
# )

# connection.commit()
# connection.close()


# ##3
# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM People;")
# cursor.fetchone()

# cursor.execute("DROP TABLE People;")
# connection.commit()
# connection.close()


##4
#no need to type commit, close when using 'with'
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );"""
    )
    cursor.execute(
        """INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
        );"""
    )


###multiple sql statements
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
        CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );
        INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            '42'
        );"""
)

people_values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28)
)

cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

##Avoiding security issues (SQL Injection) with parametrized statements
import sqlite3

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
data = (first_name, last_name, age) #using data instead of putting all 3 above separately into the database
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data)

cursor.execute(
    "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
    (45, 'Luigi', 'Vercotti')
)


##Recovering data
cursor.execute(
    "SELECT FirstName, LastName FROM People WHERE Age > 30;"
)

for row in cursor.fetchall():
    print(row)
    
    
# ##Webscrapping

# # from urllib.request import urlopen
# # url = "http://olympus.realpython.org/profiles/aphrodite"
# # html_page = urlopen(url)
# # html_text = html_page.read().decode("utf-8")
# # print(html_text)

# from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)
# html = page.read().decode('utf-8')

# start_tag = "<title>"
# end_tag = "</title>"
# start_index = html.find(start_tag) + len(start_tag)
# end_index = html.find(end_tag)

# print(html[start_index:end_index])


# ##regular expressions
# import re
# re.findall("ab*c", "ac")
# re.findall("ab*c", "abcac")
# re.findall("ab*c", "ABC", re.IGNORECASE)

# match_results = re.search("ab*c", "ABC", re.IGNORECASE)
# match_results.group()

# string = "Everything is <replaced> if it's in <tags>."
# string = re.sub("<.*>", "ELEPHANTS", string)
# string
# #Everything is ELEPHANTS.' ^greedy regular expression, replacing everything after <

# string = "Everything is <replaced> if it's in <tags>."
# string = re.sub("<.*>", "ELEPHANTS", string)
# string
# #"Everything is ELEPHANTS if it's in ELEPHANTS."

##webscrapping another website
# import re
# from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")

# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Remove HTML tags

# print(title)


#  Write a script that grabs the full HTML from the page
# http://olympus.realpython.org/profiles/dionysus


import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# print(html)

# Use the string .find() method to display the text following “Name:”
# and “Favorite Color:” (not including any leading spaces or trailing
# HTML tags that might appear on the same line).

start_text = "Name: "
end_text = "</h2>"
start_index = html.find(start_text) + len(start_text)
end_index = html.find(end_text)

print(html[start_index:end_index])

start_text = "Favorite Color: "
end_text = "</center>"
start_index = html.find(start_text) + len(start_text)
end_index = html.find(end_text)

print(html[start_index:end_index])

# Repeat the previous exercise using regular expressions. The end
# of each pattern should be a “<” (the start of an HTML tag) or a newline character, and you should remove any extra spaces or newline
# characters from the resulting text using the string .strip() method.





###Web scrapping using Beautiful Soup library

# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# url = "http://olympus.realpython.org/profiles/dionysus"

# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")

# print(soup)

# print(soup.get_text())

# soup.find_all("img")
# soup.find_all("img", src="/static/dionysus.jpg")

###Web scrapping using Mechanical Soup library

# import mechanicalsoup
# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)

# print(page.soup)

# import mechanicalsoup

# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# login_page = browser.get(url)
# login_html = login_page.soup

# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"

# profiles_page = browser.submit(form, login_page.url)

# print(profiles_page.url)

# links = profiles_page.soup.select("a")

# base_url = "http://olympus.realpython.org"

# for link in links:
#     address = base_url + link["href"]
#     text = link.text
#     print(f"{text}: {address}")


import mechanicalsoup
import time

browser = mechanicalsoup.Browser()


for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(30)

if i < 3:
    time.sleep(30)

