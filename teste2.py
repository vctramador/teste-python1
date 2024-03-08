def fibonacci(n):
  if n <= 1:
    return [0] * n
  else:
    fib_seq = [0, 1]
    while len(fib_seq) < n:
      next_num = fib_seq[-1] + fib_seq[-2]
      fib_seq.append(next_num)
    return fib_seq

def main():

  num = int(input("Digite um número: "))
  fib_seq = fibonacci(num + 1)
  if num in fib_seq:
    print(f"O número {num} pertence à sequência de Fibonacci!")
  else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()
