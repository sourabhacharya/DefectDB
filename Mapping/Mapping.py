import csv
from sets import Set
import sys

def main():
    from sys import argv
    myargs = getopts(argv)
    if '-i' in myargs:  # Example usage.
        print(myargs['-i'])
    print(myargs)

    buildIndex()
    searchIndex()

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def readMyFile(filename):
        defect2keywords = {} # defectno is key, will map to list<keywords>
        keyword2defects = {} # keyword is key, will map to list<defects>
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                defectid = row[1]
                keywords = row[5:15]
                for col in [5,6,8,10,11,12,13,14]:
                    if row[col]==" ":
                        continue
                    else:
                        keywords.append(row[col])
                defect2keywords[defectid] = keywords
                keyword2defects[kw] = []
                for kw in keywords:
                    keyword2defects[kw].append(defectid)
        return defect2keywords, keyword2defects

DE_id, keywords = readMyFile('C:\Users\soachary\Documents\sampleDE.csv')
print(DE_id)
print(keyword1)
dict1 = {}
i=1
for DE_id in DE_id and keyword1 in keyword1 and i<104:
    dict1[i] = (DE_id, keyword1)
    i=i+1
print dict1

def buildIndex():
  ## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['A'] = 'SrNo'
  dict['B'] = 'DE_id'
  dict['C'] = 'DE_Title'
  dict['D'] = 'verified'
  dict['E'] = 'ppt_link'
  dict['F'] = 'user_selection'
  dict['G'] = 'bug_against'
  dict['H'] = 'workaround'
  dict['I'] = 'mesh_type'
  dict['J'] = 'comments'
  dict['K'] = 'keyword1'
  dict['L'] = 'keyword2'
  dict['M'] = 'keyword3'
  dict['N'] = 'keyword4'
  dict['O'] = 'keyword5'
  dict['P'] = 'keyword6'
  dict1 = {}
  #dict2 = {}
  i=1
  for DE_id in DE_id and keyword1 in keyword1 and i<104:
    dict1[i] = (DE_id, keyword1)
    i=i+1
  
  print dict  ## {'A': 'SrNo', 'B': 'DE_id', 'C': 'DE_title', .... , dict['P'] = 'keyword6'}
  print dict1
  #print dict2
  #print dict['A']     ## Simple lookup, returns 'SrNo'
  #dict['A'] = 1       ## Put new key/value into dict i.e. Row2

def searchIndex():
    ## 'A' in dict         ## True
    ## print dict['Z']                  ## Throws KeyError
    keyword=input('Enter keyword: ')
    if keyword in dict['K':]: 
        return dict['B']     ## return Defect ID

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()