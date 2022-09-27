import re


def find_name(line):
    #First Second Last1 Last2
    pattern = r'[A-Z]\w*\s[A-Z]\w*'
    result = re.findall(pattern,line)

    #First Middle Last
    #First Last
    #F. Last
    #F Last
    #Dr. 
    #Dra. 
    #Dr. 
    #Mr. 
    #Mrs. 
    #Ms. 
    #Miss 
    return result

f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
