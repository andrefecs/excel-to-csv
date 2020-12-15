from datetime import datetime
import csv

output_ppcp = "output_ppcp_06.12.csv"

# declaração de variáveis
new_file = []
new_file_line = []
header = []
rawData_header = []
row = 0

# incluir header
header = ["sku", "date", "quantity"]
new_file.append(header)

with open(output_ppcp, "r") as rawData:
    for line in rawData:
        if (row == 0): # ignore raw header
            line = line.strip("\n")
            rawData_header = line.split(";")
            row = row + 1
            continue
        
        line = line.strip("\n")
        lineData = line.split(";")
        
        for i in range(len(lineData)):
            if (i == 0):
                sku = lineData[0]
                
            else: 
                production_date = datetime.strptime(rawData_header[i], "%d/%m/%y").date()
                new_file_line = [sku, production_date.strftime("%d/%m/%y"), int(lineData[i])]
                new_file.append(new_file_line)
            
        row = row + 1


with open("formatted_ppcp_06.12.csv", "w") as csvfile:
    writer = csv.writer(csvfile, lineterminator = "\n")
    for i in new_file:
        writer.writerow(i)
