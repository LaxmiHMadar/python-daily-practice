first_name="Laxmi"
last_name="madar"
full_name=first_name + " "+ last_name
print(full_name)          #concatination

meassage=" this is a warning "
print(meassage.upper())
print(meassage.lower())        
#repatition
print(meassage.strip()*2)    #space remove
print(meassage.replace("warning","error"))     #repace

msg='''laxmi said "hello"
       chaitra said "hi"'''

print(msg)
print(len(msg))     #length

 #position print
name="hanamant"
print(name[4])
  
#string slicing
print(name[1:5])   
print(name[:5])
print(name[2:5])  #substring //start end+1

#reverse indexing
print(name[0])
print(name[-8])  

print(name[::2])  #start:end:skip
print(name[::3])


s="laxmi is \n good girl" 
print(s)    # \n means next line
                     
s1="laxmi is \t good girl" 
print(s1)     #it gives tab space 
