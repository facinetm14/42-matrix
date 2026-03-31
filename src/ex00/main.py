
from Vector import Vector
from Matrix import Matrix

def main():
  
  print(f"{'=' * 30}")
  print (f"{' ' * 10} VECTORS {' ' * 10}")
  print(f"{'=' * 30}")
  
  v1 = Vector[int]([1, 3])
  v2 = Vector[int]([4, 3])
  k = 2
  
  print (f"{'-' * 10} Add {'-' * 10}")
  print(f"{v1} + {v2} = {v1.add(v2)}")
  print(f"{'' * 30}")
  
  print (f"{'-' * 10} Sub {'-' * 10}")
  print(f"{v1} - {v2} = {v1.sub(v2)}")
  print(f"{'' * 30}")
  
  print (f"{'-' * 10} Scl {'-' * 10}")
  print(f"{k} * {v1} = {v1.scl(k)}")
  print(f"{'' * 30}")
  
  
  print(f"{'=' * 30}")
  print (f"{' ' * 10} MATRIX {' ' * 10}")
  print(f"{'=' * 30}")
  
  m1 = Matrix([v1])
  m2 = Matrix([v2])
  
  v3 = Vector[int]([1, 2])
  v4 = Vector[int]([4, 6])
  
  m3 = Matrix([v1, v2])
  m4 = Matrix([v3, v4])
  
  
  print (f"{'-' * 10} Add {'-' * 10}")
  print(f"{m1} + {m2} = {m1.add(m2)}")
  print(f"{m3} + {m4} = {m3.add(m4)}")
  print(f"{'' * 30}")
  
  
  print (f"{'-' * 10} Sub {'-' * 10}")
  print(f"{m1} - {m2} = {m1.sub(m2)}")
  print(f"{m3} - {m4} = {m3.sub(m4)}")
  print(f"{'' * 30}")
  
  
  print (f"{'-' * 10} Scl {'-' * 10}")
  print(f"{k} * {m1} = {m1.scl(k)}")
  print(f"{k} * {m3} = {m3.scl(k)}")
  print(f"{'' * 30}")
  
  
if __name__== "__main__":
  main()