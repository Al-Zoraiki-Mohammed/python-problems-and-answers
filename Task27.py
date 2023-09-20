# Succefully works, but I need to enhance the efficicy,document the code
# I also need to investigate why  k-j !! for the right half of center row
def print_rangoli(size):
    rows= (size - 1) * 2 + 1 
    cols = (rows - 1)* 2 + 1
    l=[['-' for i in range(cols)] for j in range(rows)] 
    c=1
    d=2
    for i in range(rows):
        for j in range(cols):
            #for the first row
            if i==0 :
                l[i][int(cols/2)]= chr(ord('a')+size -1)
            #for the center row
            elif i== int(rows/2):
                for k in range(0,cols,2):
                    #for the left half of center row
                    if k <= int(cols/2):
                        l[i][k]= chr(ord('a')+size-1-int(k/2))
                    #for the right half or the center row
                    elif k > int(cols/2):
                        l[i][k]= l[i][j-k]
                        
            
            
            else:
                if j == int(cols/2) and i<(int(rows/2)):
                    l[i][j]= chr(ord(l[i-1][j])-1)
                    for k in range(c):
                        l[i][j+2*k+2]= chr(ord(l[i][j])+k+1)
                        l[i][j-2*k-2]= chr(ord(l[i][j])+k+1)
                    c +=1         
        #for the below half
        if i> int(rows/2):
            l[i]=l[i-d]
            d +=2
                                   
        
    for item in (l):
        print(''.join(item))

if __name__ == '__main__':
    n = int(input('size: '))
    print_rangoli(n)