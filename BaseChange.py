import string

digits = "0123456789ABCDEF"

def NtoS(n):
  num = []
  for d in n:
    num.append(str(digits.index(d)))
  return(num)


def _Bto10(n, N, b, i):
  newN = N
  newI = i
  
  newN.append(n[newI]*b + n[newI + 1])
  if(newI < len(n)):
    newI += 1
    return(_Bto10(n, newN, b, newI))
    
    
  
def _10toB(n, b):

def baseChange(n, b1, b2):
  i = 0
  num_out = 0
  
  for d in n:
    if(d not in digits):
      return("Please, enter a number in a base up to hexadecimal.")
    if(digits.index(d) > b1):
      return("The number is on a higher base.")

  while(i < len(n)):




  import string

digits = "0123456789ABCDEF"


def _Bto10(n, N, b, i):
  newN = N
  newI = i
  
  newN.append(str(int(n[i])*b + int(n[(i + 1)])))
  if(i < len(n)):
    newI += 1
    return(_Bto10(n, newN, b, newI))
    
#print(_Bto10(["5","2","3"], [], 6, 0))
n = ["5","2","3"]
print(n.append[()])
