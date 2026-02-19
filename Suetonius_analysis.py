#import cltk

import re
from bs4 import BeautifulSoup

import requests

import matplotlib.pyplot as plt
import statsmodels.api as sms
import numpy as np


def request(url):
        return requests.get(url).text

#from cltk.prosody.latin.hexameter_scanner import HexameterScanner

with open('suetonius.txt', 'r', encoding = 'utf8') as file:
    text = file.read().replace('\n', '')

words = text.lower().split()
###

###Try Suetonius

###

'''
#lines = [re.sub(r'[0-9\n]', '', line).lower() for line in file]
lines = [re.sub(r'[0-9?!,.:;—\-“”\'\n)(|]', '', line).lower() for line in file]
for line in lines:
            if line == '':
                        lines.remove(line)

words = []

for line in lines:
          words += line.split()

stopwords = ['et', 'in', 'nec', 'per', 'ad',
             'atque', 'non',
             'cum', 'tum', 'quae',
             'est', 'aut', 'nunc', 'haec',
             'si', 'iam', 'te', 'hic',
             'se', 'qui', 'sic', 'sub', 'ille', 'ipse',
              'me', 'ut', 'sed', 'ab', 'mihi', 'at',
             'ac', 'inter', 'de', 'tibi',
             'quo', 'quem', 'ubi',
             'ante', 'o', 'qua', 'quam',
             'haud', 'hoc', 'ex', 'quid']


def most_common(lst):
          word_frequency = {}
          temp = lst.copy()
          for word in temp:
                    temp = list(filter((word).__ne__, temp))
                    #print(temp)
                    if word not in stopwords:
                              if word not in list(word_frequency.keys()):
                                        word_frequency[word] = 1
                              else :
                                        word_frequency[word] += 1
                                        
          return word_frequency
'''       
'''
frequency = most_common(words)
for i in list(frequency.keys()):
        if frequency[i] > 10:
                print(i, frequency[i]) 
'''
books = []

start = 0

#print(lines[0:5])
print(type(text))
counter = 0
while counter < len(text):
        #print(text[counter]) 
        if text[counter] == '=':
                #print('found')
                #print(text[start:counter])
                books.append(text[start:counter])
                start = counter
        counter+=1
 

#print(aeneid_books[2])
                

                
y_values = []

x_values = [1,2,3,4,5,6,7,8,9,10,11,12]

find = 'senat'

#print(len(books))

def count_occurrences(word, sentence):
        return sentence.count(word)

#print(books[1])
for book in books:
        y_values.append(count_occurrences(find, book))
        #print(len(book.split()))
'''
for i in x_values:
        count = 0
        #print(len(aeneid_books[i-1]))
        for line in books[i-1]: 
                if find in line: 
                        #print(found him) 
                        count+=1
        print(count) 
        y_values.append(count)
'''

print(x_values, y_values, [y_values[i]/len(books[i].split()) for i in range(12)])

# In the next line, replace boxplot with the filename you wish to save as:
output_filename = 'regression_figure.png'

# Use the next line to set figure height and width (experiment to check the scale):
figure_width, figure_height = 8,8

# These lines perform the regression procedure:
X_values = sms.add_constant(x_values)
regression_model_a = sms.OLS(y_values, X_values)
regression_model_b = regression_model_a.fit()
# and print a summary of the results:
print(regression_model_b.summary())
print() # blank line

# Now we store all the relevant values:
gradient  = regression_model_b.params[1]
intercept = regression_model_b.params[0]
Rsquared  = regression_model_b.rsquared
MSE       = regression_model_b.mse_resid
pvalue    = regression_model_b.f_pvalue

# And print them:
print("gradient  =", regression_model_b.params[1])
print("intercept =", regression_model_b.params[0])
print("Rsquared  =", regression_model_b.rsquared)
print("MSE       =", regression_model_b.mse_resid)
print("pvalue    =", regression_model_b.f_pvalue)

# This line creates the endpoints of the best-fit line:
x_lobf = [min(x_values),max(x_values)]
y_lobf = [x_lobf[0]*gradient + intercept,x_lobf[1]*gradient + intercept]

# This line creates the figure. 
plt.figure(figsize=(figure_width,figure_height))

# Uncomment these lines (remove the #) to set the axis limits (otherwise they will be set automatically):
#x_min,x_max = 0,5000000
#y_min,y_max = 0,5000000
#plt.xlim([x_min,x_max])
#plt.ylim([y_min,y_max])

# The next lines create and save the plot:
plt.plot(x_values,y_values,'b.',x_lobf,y_lobf,'r--')
plt.title('Occurrence of the morpheme \'{}\' in Suetonius\' De vita Caesarum'.format(find))
plt.xlabel('book number')
plt.ylabel('number of occurrences of \'{}\''.format(find))
plt.savefig(output_filename)


