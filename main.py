class Ksiazka:
  def __init__(self,tytul,autor):
    self._autor=autor
    self._tytul=tytul


class Egzemplarz:
  def __init__(self,tytul,autor,rok_wydania):
    self._rok_wydania = rok_wydania
    self.tytul= tytul
    self.autor=autor

  @classmethod
  def egz(cls,tytul_egz,autor_egz,rok_wyd):
       cls._rok_wydania=rok_wyd
       cls.tytul=tytul_egz
       cls.autor=autor_egz

class Biblioteka:
  def __init__(self,egzemplarz,czytelnik):
    self._egzemplarz=egzemplarz
    self._czytelnik=czytelnik
  
  def dodaj_egzemplarz_ksiazki(egzemplarz):
      ksiazki=[]
      ksiazki.append(egzemplarz)
      print(ksiazki)

liczba_egzemplarzy=int(input())
egzemplarze_lista=[]

for egzemplarz in range(liczba_egzemplarzy):
  egzemplarze=eval(input())
  egzemplarze_lista.append(egzemplarze)

egzemplarze_lista2=[]
for egzemplarz2 in egzemplarze_lista:   
  egz=egzemplarz2
  tytul_egz=egz[0].strip()
  autor_egz=egz[1].strip()
  rok_egz=egz[2]
  egzemplarze_lista2.append(Egzemplarz(tytul_egz,autor_egz,rok_egz))
 
Lista_aut_tytul = [] 
for o in egzemplarze_lista2:
    if o.tytul not in Lista_aut_tytul :
        Lista_aut_tytul.append([o.tytul,o.autor])

occurrences={}
for i in Lista_aut_tytul:
    if tuple(i) in occurrences:
        occurrences[tuple(i)] += 1
    else:
        occurrences[tuple(i)] = 1

sorted_x = sorted(occurrences.items(), key=lambda kv: kv[1])

for key,value in sorted_x:
    print("('"+key[0]+"','"+key[1]+"',"+str(value)+")")