szukana = ['A','A','B']
tekst = []
with open('palindromy.txt', 'r') as file:
    for litera in file.read().replace('\n',''):
       tekst.append(litera)

def szukaj(szukana,tekst):
    m = len(szukana)
    n = len(tekst)

    for x in range(0,n):
        licznik = 0
        i = 0
        if tekst[x]==szukana[0]:
            for i in range(1,m):
                if tekst[x+i] == szukana[0+i]:
                    licznik += 1
                else:
                    break
        if licznik == m - 1:
            print(x)

szukaj(szukana,tekst)