import random
def caniques():
  PotA = ["YA", "YA", "YA", "YA", "YA", "GA", "GA", "GA", "GA", "GA", "GA", "GA", "GA"]
  PotB = ["YB", "YB", "GA", "GA", "GA", "GA", "GA", "GA"]
  
  M1 = random.randint(0, 12) 
  M2 = random.randint(0, 12)
  while(M1 == M2):
    M2 = randint(0, 12)

  PotB += PotA[M1]
  PotB += PotA[M2]

  M3 = random.randint(0, 9)
  return(PotB[M3])

def simulation(n):
  i = int(n)
  counter = 0
  while(i > 0):
    if(caniques() == "YA"):
      counter += 1
    i -= 1
  return(counter)

print(simulation(10))
