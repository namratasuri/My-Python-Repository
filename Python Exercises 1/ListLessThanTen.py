# This exercise was taken from https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    input_number = int(input("Please enter the number: "))
    b = [i for i in a if i < input_number]
    print (b)

if __name__ == "__main__":
    main()