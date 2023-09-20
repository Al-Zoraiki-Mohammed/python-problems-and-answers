def split_and_join(line):
    s_l=line.split()
    s_j= '-'.join(s_l)
    return s_j

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)