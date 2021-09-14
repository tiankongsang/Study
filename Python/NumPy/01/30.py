import csv

content = [['0', 'hanmeimei', '10', '15'],
           ['1', 'mayi', '20', '25'],
           ['2', 'jack', '30', '35']]
f = open("test.csv", "w", newline='')
content_out = csv.writer(f)
for con in content:
    content_out.writerow(con)
f.close()
