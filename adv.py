#functions
def greet():
    print("hello good morning")
greet()
greet()
#Defines a function that prints a greeting and calls it twice

def marrige(boy,girl):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} marries {girl}")
marrige("prabuddh","rachana")
marrige("prabuddha","sadie sink")

def table(num):
    for i in range (1,11):
        print(f"{num}X{i}={num*i}")
table(2)
table(3)
#table function takes a number as input and prints its multiplication table from 1 to 10,
