#print("Laxmi madar")   
 # name=input("Name is: ")  #input
#print(name)              #output


boy_name=input("Enter boy name: ")
boy_age=int(input("Age: "))
girl_name=input("Enter girl name: ")
girl_age=int(input("Age: "))

age_diff=abs(boy_age-girl_age)     #absolute difference value 

#print(boy_name ,"loves" ,girl_name)
#print(boy_name +" loves "+ girl_name)  #concantination

print(f"{boy_name} loves {girl_name} Age difference is {age_diff}")   #formated strings