'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
 n < 2
return False
for i in range(n, n//2+1):
  if n % i == 0:
    return False
 return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  n = 1
  for i in lst:
    n = n * i
  return n 
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x != y:
    if x > y:
      x = x - y
    else: 
      y = y - x
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while y != 0:
    r = x % y
    x = y
    y = r
  return x
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
