import random
def caniques():
  PotA = ["YA", "YA", "YA", "YA", "YA", "GA", "GA", "GA", "GA", "GA", "GA", "GA", "GA"]
  PotB = ["YB", "YB", "GA", "GA", "GA", "GA", "GA", "GA"]
  
  M1 = random.randint(0, 12) 
  M2 = random.randint(0, 12)
  while(M1 == M2):
    M2 = random.randint(0, 12)

  PotB.append(PotA[M1])
  PotB.append(PotA[M2])

  M3 = random.randint(0, 9)
  return(PotB[M3])

def simulation(n):
  i = int(n)
  YA = 0
  GA = 0
  YB = 0
  GB = 0
  while(i > 0):
    if(caniques() == "YA"):
      YA += 1
    if(caniques() == "YB"):
      YB += 1
    if(caniques() == "GA"):
      GA += 1
    if(caniques() == "GB"):
      GB += 1
    i -= 1
  print("YA = " + YA)
  print("YB = " + YB)
  print("GA = " + GA)
  print("GB = " + GB)

simulation(10)
