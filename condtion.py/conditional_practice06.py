# marks decide student grade

marks=input("Enter your marks :")

if(marks<=100 and marks>=90):
    grade="Ex"
elif(marks<=90 and marks>=80):
    grade="A"    
elif(marks<=80 and marks>=70):
    grade="B" 
elif(marks<=70 and marks>=0):
    grade="C"       
elif(marks<=60 and marks>=0):
    grade="D"    
elif(marks<=50 and marks>=0):
    grade="F"    
    
print(grade)    