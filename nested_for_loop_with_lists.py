"""Write a function with one parameter, a list of lists (containing solely
numbers). Your function should print on the screen the very first
element and the very last. This function should also return the total
of the sum of all elements"""

def myfunc(manylists):
    lst1=manylists[0]
    lst2=manylists[-1]
    print(f"the firssst list is {lst1} and the last list is {lst2}")
    summation=0
    for lists in range(len(manylists)):
        for columns in range (len(manylists[lists])):
                    summation=summation+manylists[lists][columns]
    print(f"the sum of all elements of the list is {summation}")
   
