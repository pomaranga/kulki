def start_screen():
    background(0)  

    # tytuł gry
    textSize(80)
    fill(255)
    textAlign(CENTER)
    text("Kulki", width/2, height/2 - 150)

    # krótka instrukcja gry
    textSize(24)
    text("Instrukcja:", width/2, height/2 - 60)
    text(" Strzelaj w kulki, ktore sa tego samego koloru co twoja. ", width/2, height/2)
    text(" Pozbadz sie wszystkich aby wygrac.", width/2, height/2 + 50)

    # przycisk "start"
    button_width = 150
    button_height = 50
    button_x = width/2 - button_width/2 + 75
    button_y = height/2 + 200
    rectMode(CENTER)
    fill(0, 255, 0)  
    rect(button_x, button_y, button_width, button_height)
    fill(255)
    textSize(24)
    text("Start", button_x, button_y + 8)    

import random

kolory = [
        color(255, 0, 0),
        color(0, 255, 0),
        color(0, 0, 255),
        color(0, 255, 255),
        color(255, 0, 255),
        color(255, 255, 0), 
    ]


'''
wartosci kolorow:
   red =  -65536
   green = -16711936
   darkblue = -16776961
   lightblue = -16711681
   pink = -65281
   yellow = -256
'''


pociski = []
nastepny_kolor = None


class Kulki:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
    def display(self):
        stroke(255, 255, 255)
        strokeWeight(2)  
        smooth() 
        fill(self.color)
        ellipse(self.x, self.y, self.radius, self.radius) 
    
def randomowy_kolor():
    return random.choice(kolory)
# Natalia_A
def licz_wynik(wynik):
    wynik = wynik + 1
    return wynik


def generuj_kulki():
    global kulka, kuleczki, lista_kolorow, losowy_kolor
    kuleczki = []
    lista_kolorow = []
    liczba_kolumn = 15
    liczba_rzedow = 5
    
    rozmiar_kulki = 50
    margines = rozmiar_kulki
    szerokosc_rzedu = width - 2 * margines
    odstep_miedzy_kulkami = szerokosc_rzedu / (liczba_kolumn - 1)
    przesuniecie = odstep_miedzy_kulkami / 2
    
    for rzad in range(liczba_rzedow):
        for kolumna in range(liczba_kolumn - rzad % 2):
            x = kolumna * odstep_miedzy_kulkami + rzad % 2 * przesuniecie + margines
            y = rzad * odstep_miedzy_kulkami + margines
            losowy_kolor = randomowy_kolor()
            kulka = Kulki(x, y, rozmiar_kulki, losowy_kolor)
            lista_kolorow.append(kulka.color)
            kuleczki.append(kulka)
    return kuleczki

class Pocisk(Kulki):
    def __init__(self, x, y, radius, color, target_x, target_y):
        Kulki.__init__(self, x, y, radius, color)
        self.speed = 10  # predkosc pocisku, mozna zmienic jesli trzeba 
        dx = target_x - x # Adrian - oblicza różnicę w pozycji x między celem (miejsce, do którego chcemy skierować pocisk) a obecną pozycją pocisku
        dy = target_y - y # to samo co powyżej, ale dla osi y
        mag = sqrt(dx*dx + dy*dy) # oblicza długość wektora od obecnej pozycji pocisku do celu
        self.vx = self.speed * dx / mag # oblicza składową x prędkości pocisku
        self.vy = self.speed * dy / mag # to samo tylko dla y
    
    def move(self): 
        self.x += self.vx
        self.y += self.vy
        
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.vx *= -1  #odbijanie posicku od ścianki (prawa i lewa) 
    
    def wylecial(self): # sprawdzenie czy pocisk wylecial poza ekran
        return 
        (
            self.y + self.radius < 0 or
            self.x - self.radius > width or
            self.x + self.radius < 0 or
            self.y - self.radius > height
        )
    

def mousePressed():
    global strzala_kulka, nastepny_kolor, pocisk_tymczasowy
    color = strzala_kulka.color  # Pobieramy kolor z kulki na dole zeby pocisk mial ten sam kolor
    pocisk_tymczasowy = Pocisk(strzala_kulka.x, strzala_kulka.y, strzala_kulka.radius, color, mouseX, mouseY)
    pociski.append(pocisk_tymczasowy)
    strzala_kulka.color = nastepny_kolor  
    nastepny_kolor = randomowy_kolor()
    print 'kolor nowego pocisku:', strzala_kulka.color
'''
def sprawdz_kolizje(kuleczki, pociski): #Miłosz, ale trzeba jeszcze poprawić jak coś
    for kula in kuleczki:
        for pocisk in pociski:
            distance = dist(kula.x, kula.y, pocisk.x, pocisk.y)
            if distance <= kula.radius / 2 + pocisk.radius / 2:
                kuleczki.remove(kula)
                pociski.remove(pocisk)
                break
'''
def setup():
    global strzala_kulka, strzalka, kulki_na_gorze, nastepny_kolor, przypisanie_kolorow, wynik
    # Natalia_A
    wynik = 0 #N
    global text_size #1N
    text_size = 40 #2N
    textSize(text_size) #3N
    size(800, 600)
    kolor_kulki = randomowy_kolor()
    nastepny_kolor = randomowy_kolor()
    strzala_kulka = Kulki(400, 550, 50, kolor_kulki)
    strzalka = loadImage("strzalka.png")
    kulki_na_gorze = generuj_kulki()
    print 'kolor pocisku:', strzala_kulka.color

    przypisanie_kolorow = [
        {kulki_na_gorze[-1]: lista_kolorow[-1], kulki_na_gorze[-2]: lista_kolorow[-2], kulki_na_gorze[-3]: lista_kolorow[-3],
        kulki_na_gorze[-4]: lista_kolorow[-4], kulki_na_gorze[-5]: lista_kolorow[-5], kulki_na_gorze[-6]: lista_kolorow[-6],
        kulki_na_gorze[-7]: lista_kolorow[-7], kulki_na_gorze[-8]: lista_kolorow[-8], kulki_na_gorze[-9]: lista_kolorow[-9],
        kulki_na_gorze[-10]: lista_kolorow[-10], kulki_na_gorze[-11]: lista_kolorow[-11], kulki_na_gorze[-12]: lista_kolorow[-12],
        kulki_na_gorze[-13]: lista_kolorow[-13], kulki_na_gorze[-14]: lista_kolorow[-14], kulki_na_gorze[-15]: lista_kolorow[-15]}
        ]   #itd.


def dodanie_kulki(kuleczki, pociski):
    global wynik
    nowe_kuleczki = []
    for kula in kuleczki:
        for pocisk in pociski:
            distance = dist(kula.x, kula.y, pocisk.x, pocisk.y)
            if distance <= kula.radius / 2 + pocisk.radius / 2:
                if (przypisanie_kolorow[-1][kula]) == pocisk_tymczasowy.color:
                    kuleczki.remove(kula)
                    # Natalia_A 
                    wynik = licz_wynik(wynik) # dodaje punkt kiedy zbijają się kulki (N)
                if (przypisanie_kolorow[-1][kula]) != pocisk_tymczasowy.color: 
                    kuleczki.append(pocisk)
            if distance <= kula.radius:
                if kula not in nowe_kuleczki:
                    nowe_kuleczki.append(kula)
                if distance !=0:
                    pocisk.x=kula.x+kula.radius/2
                    pocisk.y=kula.y+kula.radius
                nowa_kula = Kulki(pocisk.x, pocisk.y, pocisk.radius, pocisk.color) # Tworzenie nowej kuleczki na podstawie pocisku
                nowe_kuleczki.append(nowa_kula)
                #print 'kolor celu', (przypisanie_kolorow[-1][kula])
                #print 'kolor wystrzelonej kulki', pocisk_tymczasowy.color
                pociski.remove(pocisk)
            
                break
'''        else:
            nowe_kuleczki.append(kula)
    kuleczki[:] = nowe_kuleczki          '''     #dodalam ''', aby dzialalo przypisanie_kolorow

def draw():
    global strzala_kulka, strzalka, kulki_na_gorze, nastepny_kolor
    background(200)
    for kula in kulki_na_gorze:
        kula.display()
        
    for p in pociski:
        p.move()
        p.display()
        if p.wylecial():
            pociski.remove(p)

    dodanie_kulki(kulki_na_gorze, pociski)  # Dodanie pocisku do kuleczek
    strzala_kulka.display()
    #sprawdz_kolizje(kulki_na_gorze, pociski)  # Sprawdzenie kolizji kulki-pociski
    
    
    # Natalia_A - Licznik punktów
    fill(255) # kolor tekstu
    textAlign(RIGHT, BOTTOM) # pozycja wyświetlania wyniku
    text("Score: " + str(wynik), width, height) # wyświetlanie wyniku
    
    # Adrian - Pokazanie koloru nastepnej kulki
    fill(nastepny_kolor)
    ellipse(50, height - 50, strzala_kulka.radius, strzala_kulka.radius)
    
    #Konrad - dodanie strzalki
    kierunek = PVector(mouseX - strzala_kulka.x, mouseY - strzala_kulka.y) #tworzy wektor ktory okresla roznice miedzy pozycja myszki a kulki
    kierunek.normalize() #skaluje wektor
    pushMatrix()
    translate(strzala_kulka.x, strzala_kulka.y) #przesuwa "srodek" do pozycji kulki
    rotate(kierunek.heading())  # Obrót strzalki w kierunku wektora
    translate(60, 3) #zmiana punktu obrotu obrazka
    imageMode(CENTER)
    image(strzalka, 0, 0)
    popMatrix()
    
