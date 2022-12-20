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
