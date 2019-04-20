
import math
# I comment

''' multiline comment


   Whenever the Python interpreter reads a source file, it does two things:

   it sets a few special variables like __name__, and then

   it executes all of the code found in the file.

'''


def greeting_from_river(): 
    print("Rise & Shine!!")

name = "Unknown"

def demo_global_var():
    global name
    name = "River"
    print(name)

def demo_arithmetic():
    print("demo_arithmetic~\n")
    print("7+2 =",7+2)
    print("7-2 =",7-2)
    print("7*2 =",7*2)
    print("7/2 =",7/2)
    print("7%2 =",7%2)
    print("7**2 =",7**2) #power
    print("7//2 =",7//2) #Floor

    print("math.floor(7/2) = ", math.floor(7/2))
    print("math.ceil(7/2) = ", math.ceil(7/2))

def demo_function_param(a="a", b="unknow"):
    print("I am getting "+ a +" "+ b)



def demo_if(): 
    myScore = 99
    if myScore >= 100:
        print("You are awesom")
    elif myScore >=90:
        print("Still very good")
    else:
        print("That is fine")

    if(myScore >= 90 and myScore <=99):
        print("You are the best")

def demo_list():
    friends = ['Kuan', 'Chiu', 'Jen', 'Yan','Juchi']
    print("ALL FRIENDS = ", friends)
    print("Friend 1 ", friends[1])
    print("Friend 1 ", friends[1:])
    print("Friend 1 ", str(friends[:3]))
    print("Friend 1 ", friends[-1])
    famliy = ['Chou', 'Yang']
    people = [friends, famliy]
    print(people)
    print(people[1][1])
    
def main():
    #demo_function_param("River", "Chou") #I am getting River Chou
    #demo_function_param(a="River") #I am getting River unknow
    demo_list()


if __name__ =="__main__":
    main() 