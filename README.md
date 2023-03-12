PGE Practices 03

import time

# Practices 03

 Common input format
 -------------------
 (Read the tasks descriptions below before reading this paragraph.)
 All tasks in practices 03 set share common data input format:
 The first line contains the number of the task (1 - 5).
 The second line contains the number N of strings in the input.
 Next, there are N lines of input, each contains one input string.
 Each string consists only of alphanumerical symbols, and it does not contain any blank space(s).
 The input of the whole program always contain exactly one data set of one task.
 In the evaluation system, the code is run repeatedly, each time with different input.

 Solution code structure
 -----------------------
 The code reads the input data, including the number of the task.
 Next, it runs a function or a block of code which accepts the input data
 and computes and prints the solution to it.
 It is recommended to wrap the solution of each task in a separate function,
 an example (not obligatory!) structure of the code
 is illustrated by the contents of this file.


# ====================================================================================================================
# Task 01

 We are given a list of strings. We have to divide each  string
 in half and create two new strings, A and B. String A will contain all
 first halves of the strings in the list and string B will contain
 all second halves of the strings in the list.
 The order of the halves in the resulting string will correspond to the
 order of their respective strings in the input list.
 When the length of a string is odd, its first half ends
 immediately after the middle character of the string, and also there the second half begins.
 The total of lengths of all strings in the list is less than 10^5.
 Print A and B on separate lines
'''
Example
  Input
1
3
bcdef
gk
lmnoprs
  Output
bcdglmno
efkprs
'''

# ====================================================================================================================
# Task 02

# In the given string, find the number of substrings
# which contain exactly one symbol 0 and exactly one symbol 1.
# In this problem, we count each occurrence of a substring separately.
# That is, when two identical substrings occur at different
# positions in the original string, each of these substrings is counted separately.
# The input list of strings contains at most 5 strings, the length of each is at most 5000 characters.
# Print the result for each string on a separate line.

'''
Example
  Input
2
2
n0v10se11g1c01
010100100010111011010
  Output
13
14

  Comment
The substrings in the first string are are  n0v1 ,0v1, v10, v10s, v10se, 10, 10s, 10se, 0se1, g1c0, 1c0, c01, 01.
'''

# ====================================================================================================================
# Task 03

# A substring S1 of string S is a constant substring when
# all four following conditions are met:
#   (1)   len(S1) > 1,
#   (2)   all characters in S1 are the same,
#   (3)   the character immediately before S1 is
#               either non-existing (S1 is at the beginning of S)
#               or it differs from characters in S1,
#   (4)   the character immediately after S1 is
#               either non-existing (S1 is at the end of S)
#               or it differs from characters in S1,
# The task is to identify all constant substrings in a given string
# and then to remove them all from the given string.
# Note that two constant substrings cannot overlap one another in the string.
# After removal of all constant substrings from a given string,
# the reduced string may contain new constant substrings.
# Example:
#     S = abcxxcbdyyyzzzzfgzzgf
#     The constant substrings are: xx, yyy, zzzz, zz.
#     After removal of constant substrings:
#     S = abccbdfggf
#     Now S contains other constant substrings: cc, gg
#
# In your solution, proceed in repeated steps. In each step, remove from S all constant substrings
# which are in S at the beginning of the step.
# Stop when S contains no constant substring and print S.
# The length of the given input string S is at most 5000, there are at most 5 strings in the input.

'''
Example
  Input
3
3
abcxxcbdyyyzzzzfgzzgf
xxyzzyzzyxx
tlmoybbbbptttpavvjssvwhhhhhttenryaaaavlo
  Output
ad
None
tlmoyajvwenryvlo
'''

# ====================================================================================================================
# Task 04

# In the given input string, find the longest substring which contains exactly one word 'May'.
# If more substrings share the same maximum length print them all,
# in the order in which they appear in the original string, from left to right.
# Each output string occupies exactly one text line.
# if the word May is not present in the entire string, output string None on one line.
# Print a row of four asterisks, and no other symbols,
# after the entire output for each input string.
# (It helps to separate visually the outputs corresponding to different input strings.)
# The length of the given input string  is at most 5000, there are at most 5 strings in the input.

'''
Example
  Input
4
3
MayMayzzAprilzzMayFebruaryJanuaryMayzz
MayMayMayMay
xxMayzzMayttMayuuMaywwMayrr
  Output
ayzzAprilzzMayFebruaryJanuaryMa
****
ayMayMa
ayMayMa
****
ayzzMayttMa
ayttMayuuMa
ayuuMaywwMa
****
'''

# ====================================================================================================================
# Task 05

# In the given input string,  find the longest substring
# which contains exactly one word 'May', and it does not
# contain any other month name.
# If more substrings share the same maximum length print them all,
# in the order in which they appear in the original string, from left to right.
# Each output string occupies exactly one text line.
# if the word May is not present in the entire string, output string None on one line.
# Print a row of four asterisks, and no other symbols,
# after the entire output for each input string.
# (It helps to separate visually the outputs corresponding to different input strings.)
# The names of the months are:
#  January, February, March, April, May, June, July, August, September, October, November, December
# They are considered only in this format, with the capital first  letter.
# Other formats like e.g. JUne, jUNE, ApRiL, august, are not considered to be names of the months.
# The length of the given input string  is at most 5000, there are at most 5 strings in the input.

'''
Example
  Input
5
2
MayMayzzAprilzzMayFebruaryJanuaryMayzz
xJuneMayJulyMaybeAugustMayMayMaybeJanuaryx
  Output
prilzzMayFebruar
****
ulyMaybeAugus
ayMaybeJanuar
****
'''

def task05(ss):
    # your solution here
    pass


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int( input() )
Nstrings = int( input() )
strings = []
for k in range( Nstrings ):
    strings.append(input())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G

t1 = time.time()
if taskNo == 1:  task01( strings )
if taskNo == 2:  task02( strings )
if taskNo == 3:  task03( strings )
if taskNo == 4:  task04( strings )
if taskNo == 5:  task05( strings )
t2 = time.time()
# print( 'time', str(t2-t1)[:5] )

Public data
The public data set is intended for easier debugging and approximate program correctness checking. The public data set is stored also in the upload system and each time a student submits a solution it is run on the public dataset and the program output to stdout and stderr is available to him/her.
Link to the public data set
