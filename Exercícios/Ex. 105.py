def notas(*n,sit=False):
  Max=max(n)
  Min=min(n)
  Tam=len(n)
  Media=round(sum(n)/Tam,1)
  boletim={'Maior nota':Max,'Menor nota':Min,'Quantidade de notas': Tam,'Média das notas': Media}
  if sit==True:
    if boletim['Média das notas']<6:
      boletim['Situação']='RUIM'
    else:
      boletim['Situação'] = 'BOA'
    return boletim
  else:
    return boletim


resp=notas(2,10,9,1,0,10,sit=True)
print(resp)