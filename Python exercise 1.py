def myfunc ():
    list1=[]
    list2=[]
    summation=0
    average=0
    while True:
        user_input=input("Enter a number: ")
        if(user_input.lower()=='done'):
            break;
        list1.append(int(user_input))
    delnum=int(input("Enter the number you want to delete: "))
    
    for i in range(len(list1)):
        if list1[i] != delnum:
            
            list2.append(list1[i])
     
    print ("new list =", list2)
    for j in range(len(list2)):
        summation+=list2[j]
        average=summation/len(list2)
    print("The final list is: ", average)
    
    
    
    

        
