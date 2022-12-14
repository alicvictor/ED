# Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário

def printInverse(str)->str:
  if str == '':
    return
  else:
    printInverse(str[1:])
    print(str[0], end='')

printInverse('cila')

'''
str           return                            print
'cila'        printInverse('cila'[1:])          'alic'
'ila'         printInverse('ila'[1:])           'ali'     ↑
'la'          printInverse('la'[1:])            'al'      ↑
'a'           printInverse('a'[1:])             'a'       ↑
''             
'''




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