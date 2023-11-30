def merge_the_tools(string, k):
    n = len(string)
    t = []
    for i in range(0,n,k):
        t.append(string[i:i+k])
    
    for j in range(len(t)):
        buffer =''
        for item in t[j]:
            if item not in buffer:
                buffer += item
        print(buffer)        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Example input
# s = AABCAAADA
# k = 3
