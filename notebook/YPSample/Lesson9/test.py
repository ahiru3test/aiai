
def remove_evenindex(ln):
  i=0
  ln2=[]
  
  for s in ln:
    if(i%2!=0):
      ln2.append(s)
    i+=1

  return ln2

print(remove_evenindex(["a","b","c","d","e"]))
print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])
