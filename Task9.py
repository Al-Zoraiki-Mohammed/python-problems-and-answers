print('----'*25)

x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter z: '))
n = int(input("enter n: "))
#----------------------------------- 
# Without list comperhension
    # l=list()
    # for i in range(x+1):
    #     for j in range (y+1):
    #         for k in range (z+1):
    #             if (i+j+k)!=n:
    #                 #print([i,j,k], sum((i,j,k)))
    #                 l.append([i,j,k])
    # print(l)
#-----------------------------------                  
#With list Comperhension:

# permutation = [[a, b, c] for a in range(x + y + z + 1) if a <= x for b in range(y + x + z + 1) if b <= y 
#                             for c in range(z + x + y + 1) if c <= z if a + b + c != n]
# print(permutation)
#-----------------------------------
# Different way:
permutations = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
answer = [permutation for permutation in permutations if sum(permutation) != n]
print(answer)
#-----------------------------------

# with list comperhension and itertoolsl library.
# import itertools

# x_l=[i for i in range(x+1)]
# y_l=[i for i in range(y+1)]
# z_l=[i for i in range(z+1)]

# print(list(itertools.product(x_l, y_l,z_l)))

# l= [[i,j,k]  for i,j,k in list(itertools.product(x_l, y_l,z_l)) if (i+j+k)!=n]
# print(l)
#-----------------------------------
# Recall for list comperhension with multiple for and if statements
#new_list = [expression for var1 in iterable1 if condition1 for var2 in iterable2 if condition2 ... for varN in iterableN if conditionN]
# l= [[i,j,k] for i in range(2) if i%2==0 for j in range(3,5) if j%2==0 for k in range(5,7) if k%2==0]
# print(l)
