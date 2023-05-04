import csv
import random

with open('imagedesc.csv', newline='') as imgdes:
    reader = csv.reader(imgdes)
    imglist = [row for row in reader]

with open('artists.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    alist = []
    for row in csvreader:
        alist.append(row)

artists=[]

for i in range(len(imglist)):
    rng = random.randint(1, len(alist)-1)
    artists.append(alist[rng])

with open('data.csv', newline='') as datafile:
    reader = csv.reader(datafile)
    data2 = list(reader)

# Extract each column as a separate list
itemname = [str.lower(row[1]) for row in data2]
ranks = [row[3] for row in data2]

# Print the first row of data
input_string = input("Enter the image prompt: ")
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

nested_list = imglist

foundat=[]
imgcredit=[]

print("\nsearching prompt for matching images in dataset\n")
# Use a nested loop to search for the element
for y in range(len(userimage)):
    search_element = str(userimage[y])
    for sublist in nested_list:
        if search_element in sublist:
            id=int(search_element)-1
            print(itemname[id],"found in image number ",nested_list.index(sublist)+1)
            print("artist: ",artists[nested_list.index(sublist)])
            print("image number ",nested_list.index(sublist)+1,"is made up of: ")

            if artists[nested_list.index(sublist)+1] not in imgcredit:
                imgcredit.append(artists[nested_list.index(sublist)])
            for i in sublist:
                i=int(i)
                print(itemname[i-1],end=",")
            print("\n")
            foundat.append(nested_list.index(sublist)+1)

elementrank=[]

for listele in userimage:
    elementrank.append(int(ranks[listele-1]))

imgweight=sum(elementrank)

print("The new genrated image is built in the proportion:")
for x in range(len(elementrank)):
    ratioele=(100 * elementrank[x]) / imgweight
    imgratio.append(ratioele)
    print(ratioele,"% of the image will be",itemname[userimage[x]-1])
print("genrated image was derived from",len(foundat),"training images from dataset")

print("\nartists to be credited: ")
for i in imgcredit:
    print(i)