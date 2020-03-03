#Object Height
def findHeight():
    t = float(input("How long has your object been falling for? The time needs to be less than 4.5 seconds."))   
    if t < 4.5:
        h = 100-(4.9*(t**2))
        print("The height is ",h)
    else:
        print("The time needs to be less than 4.5 seconds")
        findHeight()
findHeight()
#Human age to dog age
print("Hello. Welcome to Dog Gone Fun Pet Shop. I can calculater your dogs age in dog years.")
humanAge=int(input("How old is your dog in human years?"))
dogAge=humanAge*7
print("Your dog is ",dogAge," in dog years.")
#Celsius to Fahrenheit
c = float(input("What is the temperature in Celsius?"))
f = (c*1.8)+32
print("Celcius is",c,"\nFahrenheit is",f)
#Grading Programme
examGrade=[0,0]
quizGrade=[0,0]
name=input("What is the students name and surname.")
classNo=input("What class is the student in?")
tempinp=float(input("What is the first exam grade"))
examGrade[0]=tempinp
tempinp=float(input("What is the second exam grade"))
examGrade[1]=tempinp
tempinp=float(input("What is the first quiz grade"))
quizGrade[0]=tempinp
tempinp=float(input("What is the second quiz grade"))
quizGrade[1]=tempinp
totalGrade=examGrade[0]*0.4+examGrade[1]*0.3+quizGrade[0]*0.15+quizGrade[1]*0.15
print("Hello ",name,"From",classNo,".Your total grade is",totalGrade)
