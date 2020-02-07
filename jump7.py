'''
   zuozhe:MrWang-pig
   gongneng:zai 100 yi nei feng 7 jiu bu shu chu tiao guo
   suoyongyuju:for  if
   data:2020.2.7
'''
for a in range(1,101): 
    if a%7 == 0:          
        a+=1
    elif a%10 == 7:     
        a+=1
    elif a//10==7:        
        a+=1
    else:                      
        print (a)
