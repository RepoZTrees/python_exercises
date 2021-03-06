# This is a master file for all Python exrcises.
# To add changes for commit/once you made your local commits, you can then push it to your remote GitHub.
   # git add . # Will add all the files from the folder
   # git add filename # Will add only those files
   # git commit -m "write some message"
   # git push

# To run this module from bash:
# $ python3
# >>>import module /module means filename.py file
# >>>filename.module /function name
# Select line, Select word, Select Sentence, Select Paragraph
#

#-------------*******-----------------*****----------------

# Q1 Return number of digits in number

def digits(n):
    a = str(n)
    print(a)
    print(len(a))
#digits(n)

#Q1a. evenOdd function
def evenOdd(x):
    if(x % 2 == 0):
        print("Even")
    else:
        print("Odd")
#evenOdd(x)

#----------

# Q2 - Return number of words in a sensentence

def words(s):
    a = s.split(" ")
    print(a)
    #"Returns number of words in sentences"
    return len(a)
#words(s)

# Q2a - Return number of letters in a sentence

def letters(s):
    a = list(s)
    print(a)
    return len(a)
#letters(s) 
        
#----------

# Q3 Tables
#tables(3,10)
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# .
# .
# .
# .
# 3 * 10 = 30

def tables(m, n):
    for a in range(m, m+1):
        for i in range(1, n+1):
            b = a*i
            print(f"{a} * {i} = {b}")
#tables(m,n)

#----------

# Q4
# tables2(5)
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# Logic for the above table:
# | i | j | i*j | q   | row |
# |---+---+-----+-----+-----+
# | 1 | 1 | 1   | '1' | ['1']
# | 1 | 2 | 2   | '2' | ['1','2']
# | 1 | 3 | 3   | '3' | ['1','2','3']
# | 1 | 4 | 4   | '4' | ['1',2','3','4']
# | 1 | 5 | 5   | '5' | ['1','2','3','4','5']
# | 2 | 1 | 2   | '2' | ['2']
# | 2 | 2 | 4   | '4' | ['2','4']
# | 2 | 3 | 6   | '6" | ['2','4','6']


def tables2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print (f"{i*j}", end="  ")
        print()
    print()
#tables2()
        
#----------

# Q5 FizBizz
# Write a function fizzbizz that takes a number n as input
# It should print numbers from 1 to n with the following rules.
# 1. If it's a multiple of 3, it should print fizz
# 2. If it's a multiple of 5, it should print bizz
# 3. If it's a multiple of 15, it should print fizzbizz
# 4. Otherwise, it should just print the number.
# Example output:
# fizzbizz(15)
# should print
# 1
# 2
# fizz
# 4
# bizz
# fizz
# .
# .
# .
# 13
# 14
# fizzbizz

# modulo operator
def fizzbizz(o):
    for i in range(1, o+1):
        if i%15 == 0:
            print('fizzbizz')
        elif i%3 == 0:
            print('fizz')
        elif i%5==0:
            print('bizz') 
        else:
            print(f"{i}")
#fizzbizz(o)

#----------

#Q6 Write a program biggest which will retrun the largest element of a
# list of numbers
# e.g.
#     biggest ([1,5,9,20,7,-5,23,4,12])
# will return
#     23

def biggest(l):
    biggest_num = l[0]
    for i in l:
        if i > biggest_num:
            biggest_num = i
   # print(f"the biggest number is:{biggest_num}")
    return biggest_num

#biggest(l)

#----------

#Q7 Write a program biggest2 which will return the largest 2 elements of
# a list of numbers
# e.g.
#    biggest2([1,5,9,20,7,-5,23,4,12])
# will return
#    [20,23]

def biggest2(l):
    numbers = l
    if numbers[0]>numbers[1]:
        largest, second_largest = numbers[0], numbers[1]
        #print(largest, second_largest)
    else:
        largest, second_largest = numbers[1], numbers[0]
        #print(largest, second_largest)

    for i in numbers[2:]:
        if i>second_largest:
            if i>largest:
                second_largest, largest = largest, i
                #print(second_largest, largest)
            else:
                second_largest = i
                #print(second_largest)
            #print(second_largest, largest)
    return second_largest, largest

#----------

#Q8 A panagram is a sentence that contains all letters of the alphabet.
# e.g. ' The quick brown fox jumps over the lazy dog'
# Implement a function called 'panagram' which takes a string s as input
# and will return True if s is a panagram and False if not.
# e.g.
#panagram("the quick brown fox jumps over the lazy dog") # > True
#panagram("the quick brown fox jumped over the lazy dog") # > False
# "sphinx" of black quartz, judge my vow"

def panagram(s):
#"Will return True if s is a panagram. False otherwise"
#s = "the quick brown fox jumps over the lazy dog"

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in s.lower():
            return False
    return True

#----------

# Q9 Write a function called "freq" which will take a string s as
# input and return a dictionary that contains the number of times each
#letter occurs  in s.
#e.g. freq("six sick sheep") will return:
# {'s':3, ' ':2, 'e':2,'i':2, 'c':1, 'h':1, 'k':1, 'p':1, 'x':1}

"""
Logic:

{'s': 1}
{'s': 1, 'i': 1}
{'s': 1, 'i': 1, 'c': 1}
{'s': 1, 'i': 1, 'c': 1, 'k': 1}
{'s': 1, 'i': 1, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 1, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 1, 'x': 1}
{'s': 2, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 1}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 2}
{'s': 3, 'i': 2, 'c': 1, 'k': 1, ' ': 2, 'x': 1, 'h': 1, 'e': 2, 'p': 1}
's':3 'i':2 ' ':2 'e':2 >>> 
"""

def freq(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        #print(count) / will print the logic table

    for key in count:
        if count[key] > 1:
            print (f"'{key}':{count[key]}",end=" ")

#----------

# Q10 Write a function 'breakdown' which will take an amount as an input and
# give the breakdown of number of currency notes required.
# We have 2000, 500, 200,100, 50, 20, 10, 5, 2, 1 notes in denominations.

def breakdown(amt):
    denominations = [2000,500,200,100,50,20,10,5,2,1]
    for denomination in denominations:
        number_of_notes = amt // denomination
        sub_amount = number_of_notes * denomination
        amt = amt - sub_amount
        if number_of_notes >= 1:
            print(f'\t{denomination:4}  *{number_of_notes:4} = {sub_amount:5}')


#----------

# Q11 Write a function 'triangle' and 'reverse_triangle' which will read a number and print a triangle using "*"
#Eg:                                                                                                                                                                                
#input: 5                                                                                                  
#-----Output-----                                                                                                                                                                   
#*
#**  
#***                                                                                                                                                                                
#****                                                                                                                                                                               
#*****                                                                                                                                                                              

def triangle(n):
    stars = 0
    for r in range(1,n+1):
        stars = stars + 1
        print(f'*' * stars)


# Write a function to read a number and print a triangle in reverse order.                                                                                                          
#-----Output-----                                                                                                                                                                   
#*****                                                                                                                                                                              
#****                                                                                                                                                                               
#***                                                                                                                                                                                
#**                                                                                                                                                                                 
#*

def reverse_triangle(n):
    stars = n
    for r in range(1,n+1):
        print(f'*' * stars)
        stars = stars - 1
        #print(f'*' * stars)

#----------
"""
#Q12 Write a program/function called 'word_count'. Whatever 'wc' command in Linux would do,
#it would do by executing Python file. It's a command line argument.
#It should print a number of words, lines, and character of a file.
#for e.g.input: python3 word_count.py wc.py would git the output: 5  13  25  wc.py. 

from sys import argv

script, file_name = argv #script(script being another name for your .py files)  

def word_count():

        txt = open(file_name, 'r')
        s = txt.read()
        lines = s.split('\n')
        line_count = lines
        line_count = len(line_count)
        words = s.split(' ')
        word_count = words
        word_count = len(word_count)
        char_count = len(s)
        print(f'\t{line_count}\t{word_count}\t{char_count}\t{file_name}')

#word_count()

#Following code is an another version of the above question (Q12) with
#total_line_count, total_word_count and total_characters_count.
# for e.g.:let's say there are following 3 files in a folder.
# $ python3 exercises.py *.* #will print the following output.  
# 100  50  125  file_name1.py
#  50 100   50  file_name2.py
#  50  25  100  file_name3.txt
# 200  175 275  total

from sys import argv

script = argv[0]
file_names = argv[1:] #script(script being another name for your .py files)     

def word_count(fname):
        txt = open(fname, 'r')
        s = txt.read()
        lines = s.split('\n')
        line_count = lines
        line_count = len(line_count)
        words = s.split(' ')
        word_count = words
        word_count = len(word_count)
        char_count = len(s)
        return line_count, word_count, char_count
        #print(f'\t{line_count}\t{word_count}\t{char_count}\t{fname}')`         

tlc = twc = tcc = 0
for i in file_names:
        lc, wc, cc = word_count(i)
        print(f'\t{lc}\t{wc}\t{cc}\t{i}')
        tlc += lc
        twc += wc
        tcc += cc
if len(file_names) > 1:
        print(f'\t{tlc}\t{twc}\t{tcc}\ttotal')
"""
#----------

# Q13.Write a function `evaluate` which will receive a string `s` as
# input. `s` will be a postfix expression. All the numbers in the
# expression will be single digits.
# `evaluate` should evaluate `s` and return the result
# e.g. 
# evaluate("32+")
# should return 
# 5
#  Algorithm
#  1. For each element `i` in `s`
#     1. If i is an operand (a number), push it onto the stack
#     2. If i is an operator
#        1. pop 2 numbers from the stack
#        2. Combine it using i
#        3. Push the result back onto the stack
#  2. The stack will contain a single number which is the result
# $python3, >>>import filename, >>>filename.evaluate("32+")

#evaluate("32+")

def evaluate(s):
    list1 = []
    l = "0123456789"
    
    for i in s:                                                                
        if i in l:
            list1.append(int(i))
        else:
            if i == "+":
                a = list1.pop()
                b = list1.pop()
                c = int(a) + int(b)
                list1.append(c)

            elif i == "*":
                a = list1.pop()
                b = list1.pop()
                c = int(a) * int(b)
                list1.append(c)

            elif i == "-":
                a = list1.pop()
                b = list1.pop()
                c = int(a) - int(b)
                list1.append(c)

            else:
                a = list1.pop()
                b = list1.pop()
                c = int(a) // int(b)
                list1.append(c)
    return list1

#----------

#Q14a. Write a function which will print the following pattern

# o ....
# oo ...
# ooo ..
# oooo .
# ooooo 

def pattern(r,c):
    for i in range(1,r+1):
        for j in range(1,c+1):
            print('o'*j, '.'*(c-1))
            c=c-1
        return c

#a = pattern(5,5)
#print(a)

#Q14b
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print('o'*j, '.'*(n-1))
            n=n-1
        return n
        
#p = pattern(5)
#print(p)

#----------
