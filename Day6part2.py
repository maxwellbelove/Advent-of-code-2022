i=0
b1=0
b2=1
b3=2
b4=3
b5=4
b6=5
b7=6
b8=7
b9=8
b10=9
b11=10
b12=11
b13=12
b14=13

counter=13
running = True
    
while running == True: 
    with open('Day6Data.txt', 'r') as f:
        lines = f.readlines()
        data=(lines[i][b1], lines[i][b2], lines[i][b3], lines[i][b4], lines[i][b5], lines[i][b6], lines[i][b7], lines[i][b8], lines[i][b9], lines[i][b10], lines[i][b11], lines[i][b12] , lines[i][b13] , lines[i][b14])
        mainset= set(data)
        length = len(mainset)
        print(mainset)
        if length >= 14:
            counter=counter+1
            print("The unique 4 letters where found in",counter, "moves")
            running = False
        else:
            b1=b1+1
            b2=b2+1
            b3=b3+1
            b4=b4+1
            b5=b5+1
            b6=b6+1
            b7=b7+1
            b8=b8+1
            b9=b9+1
            b10=b10+1
            b11=b11+1
            b12=b12+1
            b13=b13+1
            b14=b14+1                      
            counter=counter+1
            ##print(counter)
            ##print(b1)



        #print(data)
        #print(mainset)

        #b1=b1+1
        #b2=b2+1
        #b3=b3+1
        #b4=b4+1
        
        
        ##print(lines[i][b1], lines[i][b2], lines[i][b3], lines[i][b4])


        


    
