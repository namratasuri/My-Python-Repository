
fib_sequence=[]

def print_Fibonacci(fib_length):
    fib_sequence=[0 for x in range(0,fib_length)]
    fib_sequence[0] = 1
    fib_sequence[1] = 1
    print(fib_sequence[0])
    print(fib_sequence[1])
    for i in range(2, fib_length):
        fib_sequence[i] = fib_sequence[i-1]+fib_sequence[i-2]
        # sum = fib_sequence[i]
        print(fib_sequence[i])



def main():
    fib_length = int(input("Please enter till what count you want the fibonacci sequence printed"))
    print_Fibonacci(fib_length)



if __name__ == "__main__":
    main()