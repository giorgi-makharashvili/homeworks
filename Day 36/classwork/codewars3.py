def count_sheep(n):
    str = ""
    
    if n == 0:
        return ""
    
    for i in range(1,n+1):
        str += f"{i} sheep..."
        
    return str