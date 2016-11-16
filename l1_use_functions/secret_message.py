import os
import re

path = "prank"

for filename in os.listdir(path):
    newfilename = re.sub('[\d]', '', filename)
    print(newfilename)
    #os.rename(filename, re.sub('[\d]', '', filename))
   
