import csv
from random import randrange

imgfile = open("imagedesc.csv", "w", newline='')

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(row)

# Print the second column of data
items = list([row[1] for row in data])
ranking = [row[3] for row in data]
# print("data:")
# print(items)
# print("ranking:")
# print(ranking)
imagedesc = list()
size = len(items)

for i in range(500):
    imagedesc = list()
    promptvar = randrange(1,5)
    print("image 1 prompt count: ",promptvar)
    for j in range(promptvar):
        imagedesc.append(randrange(1,size))
        print("image 1 prompts: ",imagedesc)
    writer = csv.writer(imgfile)
    writer.writerow(imagedesc)

print(imagedesc)
