def get_marks():
    print("Enter marks all subject out of 100")
    
    s1=float(input("java:"))
    s2=float(input("python:"))
    s3=float(input("RDBMS:"))
    s4=float(input("Web tech:"))
    s5=float(input("cpp:"))
    return s1,s2,s3,s4,s5

def calculatetotal(marks):
    return sum(marks)
    
name=input("enter your name:")
def calculatepercentage(totalmarks):
    percentage=(totalmarks/500)*100
    return percentage
def calculategrade(percentage):
    if percentage>=90:
        grade="A"
    elif percentage>=80:
        grade="B"
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    else:
        grade="E"

    return grade
    
def main():
    marks=get_marks()
    totalmarks=calculatetotal(marks)
    percentage=calculatepercentage(totalmarks)
    grade=calculategrade(percentage)
    print("/n==============================student result =================================")
    print("Name:",name)
    print("total marks:", totalmarks)
    print("percentage :", percentage)
    print("grade:", grade)
    print("thank you")
main()









