import csv

with open('imagedesc.csv', newline='') as imgdes:
    reader = csv.reader(imgdes)
    data = [row for row in reader]



# imageno = randrange(1,len(data)+1)
#
# print(imageno+1)
# print(data[imageno])


with open('data.csv', newline='') as datafile:
    reader = csv.reader(datafile)
    data2 = list(reader)

# Extract each column as a separate list
itemname = [row[1] for row in data2]
ranks = [row[3] for row in data2]

# Print the first row of data
input_string = input("Enter a string: ")
delimiter = ","

# Split the input string into words using the delimiter
word_list = input_string.split(delimiter)
print(word_list)
userimage=[]
imgratio=[]

for i in word_list:
    if i in itemname:
        userimage.append(itemname.index(i)+1)
    else:
        print(i,"not present")

print(userimage)

elementrank=[]

for listele in userimage:
    elementrank.append(int(ranks[listele-1]))

print(elementrank)
imgweight=sum(elementrank)
print(imgweight)

for x in range(len(elementrank)):
    ratioele=(100 * elementrank[x]) / imgweight
    imgratio.append(ratioele)

print(imgratio)
print(sum(imgratio))