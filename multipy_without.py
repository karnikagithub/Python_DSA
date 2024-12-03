def mul(a,b):
    tot = 0
    l = min(abs(a),abs(b))
    add = b if abs(a) < abs(b) else a
    for _ in range(l):
        tot += add
    
    if add == a and l != b:
        tot = 0 - tot
        
    return tot
    
print(mul(100,-10))     


def mul(a,b):
    tot = 0
    for _ in range(a):
        tot += b
    
    return tot
