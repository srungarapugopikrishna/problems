
import re
input = raw_input()
regex = re.compile('[^a-zA-Z]')
input = regex.sub('', input).lower()


def is_palindrome(input):
    ip1 = list(input)
    ip2 = list(input)[::-1]
    for i in range(0, len(input)):
        if ip1[i] != ip2[i]:
            return False
    return True


if is_palindrome(input):
    print 'YES'
else:
    print 'NO'