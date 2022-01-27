from collections import Counter
#from collections import defaultdic

l = [1,2,3,4,5,6]

print(Counter(l))

p = "palabra"

print(Counter(p))

animales = ["gato","perro","gato","pajaro","gato"]

print(Counter(animales))


c = Counter(animales)
print(c.most_common(1))

numeros = [10,20,30,40,10,20,10,30]
n = Counter(numeros)
print(n.items())
print(n.keys())
print(n.values())
print(sum(n.values()))
print(list(n))
print(dict(n))
print(set(n))
