def pertence_fibonacci(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    
    if num in fib:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
