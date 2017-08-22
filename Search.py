"""
#  Programmer     : Dhruv Patel
#  Problem Name   : Search
#  Used In        : Practice
#  Used As        : Data Processing
#  Thoughts      =>  
#  O(N)             This program opens the database and split the .csv file into the two coloumns.
#                   One is a product name and other one is a company.The search_utility simply
#                   search for the key in out built up dictionary and return its value if found.
"""
import time

"""
    The following operation read csv file and built up data dictionary with key as a
    product_name and company and value as a record.
    
"""
file = open('search_dataset.csv','r',encoding='UTF-8')
data = {}
for record in file:
    record = record.split(",")
    code = record[1]+record[2]
    data[code.lower()] = record[0]+record[1]+record[2]

"""
    The below function will match search for input string in match it with our built
    dictionary's keys.If there is a match then will update the result and return it in ends
    Time Complexity  : O(n^2)
    Space Complexity : O(n)
"""


def search_utility(search):
    result = []
    for j in data:                              # Getting keys as a search parameter
        key = j.split(" ")                      # Splitting keys into chunks
        for k in key:
            if k == search:                     # The kth box is compared with search term
                result.append(data.get(j))      # If a match found than we update our result.
                break
    result.sort(reverse=True)
    return result

print(len(search_utility("red")))



