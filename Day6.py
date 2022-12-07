i=0
b1=0
b2=1
b3=2
b4=3
counter=3
running = True
    
while running == True: 
    with open('Day6Data.txt', 'r') as f:
        lines = f.readlines()
        data=(lines[i][b1], lines[i][b2], lines[i][b3], lines[i][b4])
        mainset= set(data)
        length = len(mainset)
        print(mainset)
        if length >= 4:
            counter=counter+1
            print("The unique 4 letters where found in",counter, "moves")
            running = False
        else:
            b1=b1+1
            b2=b2+1
            b3=b3+1
            b4=b4+1
            counter=counter+1
            print(counter)
            print(b1)



        #print(data)
        #print(mainset)

        #b1=b1+1
        #b2=b2+1
        #b3=b3+1
        #b4=b4+1
        
        
        ##print(lines[i][b1], lines[i][b2], lines[i][b3], lines[i][b4])


        


    
