'''
Given a string s containing 0's and 1's. You have to return a smallest positive integer C, such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.

Input:
The first line of the input contains T denoting the number of test cases. For each test case, there is a string s.

Output:
For each test case, the output is an integer C. If no such cuts are possible then return -1. 

Constraints:
1<=s.length()<=50
Note: The string s is a binary string.

Example:
Input
3
101101101
1111101
00000
Output:
3
1
-1

Explanation:
1.We can split the given string into three “101”s, where 101 is the binary representation of 5.
2."1111101 " is 125 which is 5^3.
3.0 is not a power of 5.
'''

import math
input = ['101101101', '1111101', '00000']


def binary_to_decimal(binary_str):
    if '1' not in binary_str:
        return 0
    j = len(binary_str) - 1
    decimal_num = 0
    for i in range(len(binary_str)):
        if int(binary_str[i]) == 1:
            decimal_num += math.pow(2, j-i)
    return decimal_num


def isPowerOfFive(data):
    for bin_str in data:
        x = binary_to_decimal(bin_str)
        if x < 5:
            return False
        while x % 5 == 0:
            x = x / 5
        return x == 1


def cutting_binary_string(b_string):
    for i in range(2, len(b_string)):
        if len(b_string) % (i+1) == 0:
            if isPowerOfFive([b_string[k:k + (i+1)] for k in range(0, len(b_string), i+1)]):
                return int(len(b_string)/(i+1))
    return -1


for item in input:
    print(cutting_binary_string(item))
