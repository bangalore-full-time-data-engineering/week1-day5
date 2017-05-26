def isAnagram(a,b):
	set_a = set(a)
	set_b = set(b)
	if len(a) == len(b):
		i=0	
		while i<=len(a)-1:
			if(set_a[i] not in set_b) :
				anagram = False
				break
			else :
				i+=1
			anagram = True	
	else:			
		anagram = False				
	return(anagram)	
	print(anagram)		    
		    
	
isAnagram("abc","abc")	
