#Full Name Formatter
fname="laxmi"
lname="madar"
full_name=fname+" "+lname
print(full_name.upper())
print(full_name)                #LAXMI MADAR



text = "  Python Programming  "
print(len(text))
print(len(text.strip()))           #length is 18


msg="this is bad"
print(msg)
print(msg.replace("bad","good"))     #repaced


#display first and last using -tv index
word="enginnering"
print(word[-11])
print(word[-1])     


#remove extra space
msg = "   hello world   "
print(msg)
print(msg.strip()*2)            #print hello worldhello world


#Print characters at even index positions only
msg="programming"
print(msg[::2])    


#Remove extra spaces, Capitalize properly, Print total length (without spaces at start/end)
name = "  laxmi madar  "
clean = name.strip()
print("Hello", clean.title()+"!")
print("Length of name:", len(clean))




