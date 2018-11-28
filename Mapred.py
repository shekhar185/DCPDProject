import os
import re
import sys
import pprint

def get_text(file):
    text1 = open(file,'r').read().strip("\n")
    text2 = text1.lower()
    return text2



def mapper(textp):
    text = textp.split()
    vowelRegx = re.compile(r'[aeiou]')
    ToReduce= {}
    for word in text:
        a = vowelRegx.findall(word)
        if a != []:
            ToReduce[word] = a
    pprint.pprint(ToReduce)
    return ToReduce

def Reducer(ToReduce):
    reduced={}
    for word in ToReduce:
        reduced[word] = (len(ToReduce.get(word)))
    return reduced


# the file to be processed should be in mentioned path below.In case of different directory location, change the Working directory path in variable path
  # file name or the file to be processed in working directory should be passed as the argument to the string
filename = str(sys.argv[1])  # file name is passed on as the argument to the mapred python script on CLI 
path = 'C:/Users/Shashank/Desktop/Mapred'  # file path
file = os.path.join(path,filename)
print('Processing file',file)
Text = get_text(file)
ToReduce = mapper(Text)
Reduced = Reducer(ToReduce)
pprint.pprint(Reduced)
