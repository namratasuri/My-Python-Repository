
def getFibonacci(fib_length):
    if fib_length >= 2:
       return int(getFibonacci(fib_length - 1)) + int(getFibonacci(fib_length - 2))
    else:
        return 1




def main():
    fib_length = int(input("Please enter till which number you want fib sequence printed"))
  #  for x in range (0, fib_length):
   #     print(getFibonacci(x))
    fib_list = [getFibonacci(x) for x in range(0, fib_length)]
    print (*fib_list)


if __name__ == "__main__":
    main()