def mapper(lista, listb):
  assert len(lista) == len(listb)
  listc = []
  for i in range(len(listb)):
    listc.append([lista[i],listb[i]])
  return listc

def demapper(listc):
  lista = []
  listb = []
  for i in listc:
    lista.append(i[0])
    listb.append(i[1])
  return lista, listb
