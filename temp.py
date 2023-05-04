import csv


with open('imagedesc.csv', newline='') as imgdes:
    reader = csv.reader(imgdes)
    imglist = [row for row in reader]

print(imglist)

with open('data.csv', newline='') as datafile:
    reader = csv.reader(datafile)
    data2 = list(reader)

# Extract each column as a separate list
itemname = [str.lower(row[1]) for row in data2]
ranks = [row[3] for row in data2]

# Print the first row of data
input_string = input("Enter a string: ")
delimiter = ","

# Split the input string into words using the delimiter
word_list = input_string.split(delimiter)

userimage=[]
imgratio=[]
sem=0

for i in word_list:
    if i in itemname:
        userimage.append(itemname.index(i)+1)
    else:
        print(i,"not present")


elementrank=[]

for listele in userimage:
    elementrank.append(int(ranks[listele-1]))


imgweight=sum(elementrank)


for x in range(len(elementrank)):
    ratioele=(100 * elementrank[x]) / imgweight
    imgratio.append(ratioele)
    print(itemname[userimage[x]-1],"ratio in image: ",ratioele)

# print(imgratio)
# print(sum(imgratio))

nested_list = imglist

foundat=[]

# Use a nested loop to search for the element
for y in range(len(userimage)):
    search_element = str(userimage[y])
    for sublist in nested_list:
        if search_element in sublist:
            id=int(search_element)-1
            print(itemname[id],f"found in sublist: {sublist}")
            foundat.append(nested_list.index(sublist)+1)

print(foundat)