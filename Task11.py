print('----'*25)
if __name__ == '__main__':
    data=[]
    names=[]
    scores=[]
    for i in range(int(input('Enter Number of Studets N: '))):
        name = input(f'Enter the name of studet number{i+1}:  ')
        score = float(input(f'Enter the score of studet number{i+1}:  '))
        names.append(name)
        scores.append(score)
        data.append([score,name])
    
    sorted_data = sorted(data)

    print(sorted_data)
    
    first= sorted_data[0][0]
    second = False
    last = sorted_data[0][0]
    for i,j in sorted_data:
        if i>first and not second:
            print(j)
            second = True                  
        elif i ==last and second:
             print(j)
        elif i> first and second:
            break
                
        last = i

            
        
    
        

            

           
       
''' 4
Sona
-25.001
Mona
-25.0001
Mini
-25.000
Rita
-25.0
'''      
        
''' 5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39'''