# Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário

def invertString(str)->str:
  if str == '':
    return
  else:
    invertString(str[1:])
    print(str[0], end='')

invertString('cila')




"""
def invertString2(str)->str:
  if str == '':
    return
  else:
    print(str[-1], end='')
    return invertString2(str[:-1])
print()
invertString2('alic')
"""