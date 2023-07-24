def Check( seq ):  
    while True:  
        if '()' in seq :  
            seq = seq.replace ( '()' , '' )
        elif '{}' in seq :  
            seq = seq.replace ( '{}' , '' )
        elif '[]' in seq :  
            seq = seq.replace ( '[]' , '' )
        else :  
            return not seq  
        
seq = '{[()]}'  
if(Check(seq)):
    print("valid")
else:
    print("not valid")