import math

# Exercícios introdutórios sobre a linguagem Python.

# Exercício 3 do guia da primeira aula prática.
# Apresente resultados experimentais com o funcionamento de cada uma das funções.



#(a) Função que apresenta todos os números múltiplos de quatro, contidos no intervalo definido por left e right, inclusivamente.

def multiplos_de_quatro(left, right):
    for i in range(left, right+1):
        if i % 4 == 0:
            print(i)

def multiplos_de_quatro1(left, right):
    while left <= right:
        if left % 4 == 0:
            print(left)
        left += 1

print("multiplos", multiplos_de_quatro1(1, 20)) #4 , 8 , 12 , 16 , 20

#(b) Função que determina o máximo divisor comum entre dois números inteiros a e b.

def mdc(a, b):
    while b != 0:
        a, b = b, a % b # a virgula dá assign de valores
    return a

def mdc1(a, b):
    x = a
    y = b
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

def mdc2(a, b):
    return math.gcd(a, b)

print("mdc", mdc(10, 5)) #5

#(c) Função que apresenta os primeiros N termos da progressão geométrica de primeiro termo u e razão r. Os valores de N,
#u e r são passados como parâmetro.

def progressao_geometrica(N, u, r):
    value = u
    for i in range(N):
        print(value)
        value *= r

progressao_geometrica(3, 2, 3) #2 , 6 , 18
print("prog geo")


#(d) Função que calcula o número de combinações C(n, k) = n! / k!(n−k)!

def combinacao(n, k):
    def fatorial(n):
        if n == 0:
            return 1
        else:
            return n * fatorial(n-1)
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def combinacao1(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print("combinacao", combinacao(2, 2)) # 1

#(e) Função que determina os valores mínimo e máximo, de um vetor v passado como parâmetro.

def min_max(v):
    minimo = v[0]
    maximo = v[0]
    for i in v:
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i
    return minimo, maximo

def min_max1(v):
    return v.min(), v.max()

v = [1, 2, 3, 4, 5]
print("min_max", min_max(v)) #1 , 5