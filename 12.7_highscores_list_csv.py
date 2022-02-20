import csv
from pathlib import Path

file_path = Path.home() / "scores.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    csvreader = csv.DictReader(file)
    list_of_scores = list(csvreader)
#print(list_of_scores)

output = {}
for dict_item in list_of_scores:
    name = dict_item['name']
    score = int(dict_item['score'])
    if name in output:
        if score > output[name]:
            output[name] = score
    else:
        output[name] = score
        
#print(f"After maxing: {output}")

new_list = []

#change this so instead of {'LLCoolDave': 27} it becomes {'name': 'LLCoolDave', 'score': '23'} as list items and can be saved into the file as rows
for name, score in output.items():
    #print(name, score)
    row = {}
    row['name'] = name
    row['score'] = score
    new_list.append(row)

#print(new_list)

file_path = Path.home() / "high_scores.csv"
with open(file_path, mode="w", encoding="utf-8") as file:
    csvwriter = csv.DictWriter(file, fieldnames=["name", "score"])
    csvwriter.writeheader()
    csvwriter.writerows(new_list)
##    for i in range(len(new_list)):  
##        csvwriter.writerow(new_list[i])

#print(list_of_dicts)
