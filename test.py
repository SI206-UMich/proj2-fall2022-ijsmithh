from f22_Project2 import *

import os

 #List all of listing files
#print(listofFiles)
listofFiles = next(os.walk("./html_files"))
fileMatchs = [os.path.join(listofFiles[0],x) for x in listofFiles[2] if "listing_" in x and "reviews" not in x]
fileMatchs2 = []
for x in fileMatchs:
    start = 0
    end = 0
    for y in range(len(x)):
        if x[y] == "_":
            start = y
        if x[y] == ".":
            end = y
    fileMatchs2.append(x[start+1:end])


for x in fileMatchs2:
    get_listing_information(x)

