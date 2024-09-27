def pertence_fibonacci(numero):
    
    fib_a = 0
    fib_b = 1

    if numero == fib_a or numero == fib_b:
        return True
      
    while fib_b < numero:
        fib_a, fib_b = fib_b, fib_a + fib_b 
    
    return fib_b == numero


numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")