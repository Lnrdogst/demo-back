def calculate() -> float:
    pass

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa numero 1: "))
        num2 = float(input("Ingresa numero 2: "))
        resul = multiplicar(num1, num2)
        print(f"{num1} x {num2} = {resul}")
    except ValueError:
        print("Debes ingresar valores numericos.")
