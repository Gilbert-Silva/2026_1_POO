try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ZeroDivisionError:
    print("Deu erro de divisão por zero")    
except Exception as erro:
    print(erro, type(erro))
finally:
    print("Sempre é feito")
        