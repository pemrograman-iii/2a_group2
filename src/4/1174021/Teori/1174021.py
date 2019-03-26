import csv

with open('coba.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    


import csv

contoh = [
    ('fahmi', 'A', 90),
    ('bayu', 'B', 85),
    ('niko', 'A', 80),
    ('arjun', 'B', 90),
    ('mantan', 'C', 70)
]

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('contoh.csv', 'w')
w = csv.writer(f)
w.writerow(('Nama','Kelas','Nilai'))

# menulis file csv
for s in contoh:
    w.writerow(s)

# menutup file csv
f.close()




import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('contoh.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
    print row

# menutup file csv
f.close()



import csv

with open('coba.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
    
    

import pandas
df = pandas.read_csv('contoh.csv')
print(df)
    