"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17"""

def finder(x, k):
    if k in x:
        #print("IF")
        return k 

    else:
        #print("ELSE")
        x.sort()
        for i in range(len(x)):
            for j in range(1, len(x)):
                if x[i] + x[j] == k:
                    return(x[i], x[j])
                



x = [int(x) for x in input().split()]
k = int(input())

res = finder(x, k)

print(f"{res[0]} and {res[1]} give {k}")


