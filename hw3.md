## code
```
def truthTable(n): 
	p = [] 
    #print(p)
	return tableNext(n, p) 

def tableNext(n, p):
	i = len(p)      
	if i == n:		
		print(p)	
		return      
	for x in [0,1]:     
		p.append(x)		
        #print(p)
		tableNext(n, p)
        #print(p)
		p.pop()			
        #print(p)
truthTable(2) 

## 結果
```
[0, 0]
[0, 1]
[1, 0]
[1, 1]
```