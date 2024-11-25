"""Task50"""
def print_upper_header():
    print("    ", end="   ")
    for i in range(1,11):
        print(i, end="    ")
    print()
    print("----" * 14)


def print_column_header(i):
    if i < 10:
        print(f"{i}  |", end="   ")
    else:
        print(f"{i} |", end="   ")


def print_mul_table():
    print_upper_header()
    for i in range(1,11):
        print_column_header(i)
        for j in range(1,11):
            if (i*j) <10:
                print (i * j, end= "    ")
            else:
                print (i * j, end= "   ")
        print()


if __name__ == "__main__":
    print_mul_table()
