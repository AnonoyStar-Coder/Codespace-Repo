# for i in range(6):
#    print(i)
#    break
#
# for i in range(6):
#    print(i)
#
# name = "balraj"
# for char in name:
#    print(char)
#
# students = ["balraj", "tamanna", "ajay", "anshu"]
# for student in students:
#    print(student)
#
# for i in range(7):
#    print(i)
# else:
#    print("loop completed successfully")
#
# for i in range(7):
#    print(i)
#    break
# else:
#    print("loop completed successfully")
#
## else:
## print("loop completed successfully")
##
## for i in range(7):
##    print(i)
## else:
##    print("loop completed successfully")
## for i in range(7):
##    print(i)
##    break
## else:
##    print("loop completed successfully")
##
## for i in range(7):
##    print(i)
## else:
##    print("loop completed successfully")
##
## count = 0
## while count <= 3:
##    print(count)
##    count += 1
## count = 1
## while count <= 3:
##    print(count)
##    count += 1
##
## while count < 3:
##    print(count)
##    count += 1

name = input("What's your name? : ")


def greet(name):
    print("Hello", name)


greet(name)

print()


def main():
    print("Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("area of circle is", area_c(r))

    elif choice == "2":
        len = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("area of rectangle is", area_rect(len, w))

    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("area of triangle is", area_t(b, h))

    else:
        print("Wrong Choice")


def area_c(r):
    return 3.14 * r * r


def area_rect(len, w):
    return len * w


def area_t(b, h):
    return 0.5 * b * h


main()

# a = input("Enter your name: ")
#
# def greet(a):
#    print("Hello there,", a, "!!")
#
# greet(a)
