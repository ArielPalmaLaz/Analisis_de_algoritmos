import math
#Código para nlog(n)
def minimo_n(nlogn):
    left = 1
    right = 1
    
    while right * math.log(right, 2) < nlogn:
        right *= 2
        
    while left < right:
        mid = (left + right) // 2
        if mid * math.log(mid, 2) < nlogn:
            left = mid + 1
        else:
            right = mid
    return left

nlogn= 1000000

result = minimo_n(nlogn)

print("Valor mínimo de n cuando(n lg n)>= {}: {}".format(nlogn, result - 1))

#Código para n!

n = 1
while math.factorial(n) < 1000000:
    n += 1

print("Valor minimo de n para n!:", n - 1)

def calcular_microsegundos_en_segundo():
    # Calcular n dado que log_2(n) = 106
    n = 2**(10**6)

    # Calcular cuántos microsegundos hay en 1 segundo
    microsegundos_en_segundo = 10**6

    return n, microsegundos_en_segundo

# Llamar a la función para realizar los cálculos
n_value, microsegundos_value = calcular_microsegundos_en_segundo()

# Convertir los valores a notación científica si exceden los 5 dígitos
n_formatted = "{:e}".format(n_value) if len(str(n_value)) > 5 else str(n_value)
microsegundos_formatted = "{:e}".format(microsegundos_value) if len(str(microsegundos_value)) > 5 else str(microsegundos_value)

# Imprimir los resultados con notación científica si es necesario
print(f"El valor de n tal que log_2(n) = 106 es: {n_formatted}")
print(f"Microsegundos en 1 segundo: {microsegundos_formatted}")