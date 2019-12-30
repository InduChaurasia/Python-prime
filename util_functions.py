import math

def is_prime(inputValue):   
    num = inputValue
    if(num <= 1):
        return False
        
    sqrtNum = int(math.sqrt(num))
    for i in range(2 , sqrtNum+1):
        if(num%i==0):
            return False
            
    return True
    
      
def all_stripped_num_prime(inputValue, strip_frm_back):
    num = inputValue
    prime = True
    while (len(str(num))>=1 and prime):
        prime = is_prime(num)        
        if(len(str(num))>1):
            if(not strip_frm_back):
                stripped_str = str(num)[0:len(str(num))-1]
            else:
                stripped_str = str(num)[1:len(str(num))]
            num = int(stripped_str)
        else:
            break    
            
    return prime  
    

def is_double_side_prime(inputValue):
    try:      
        num = int(inputValue)
        if(num<0):
            return False
        is_prime = all_stripped_num_prime(num,False)
        if(is_prime):
            is_prime = all_stripped_num_prime(num,True)
        
        return is_prime
    except:
        return False