'''Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.For example, the message
'111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.'''

def helper(data, k):
    if k == 0:
        return 1

    s = len(data) - k
    if data[s] == '0':
        return 0

    result = helper(data, k - 1)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k - 2)

    return result

def num_ways(data):
    return helper(data, len(data))

print(num_ways('121'))





