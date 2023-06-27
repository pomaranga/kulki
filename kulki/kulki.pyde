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

def generuj_kulki():
    kuleczki = []
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
    global strzala_kulka, nastepny_kolor
    color = strzala_kulka.color  # Pobieramy kolor z kulki na dole zeby pocisk mial ten sam kolor
    pocisk_tymczasowy = Pocisk(strzala_kulka.x, strzala_kulka.y, strzala_kulka.radius, color, mouseX, mouseY)
    pociski.append(pocisk_tymczasowy)
    strzala_kulka.color = nastepny_kolor  
    nastepny_kolor = randomowy_kolor()

def setup():
    global strzala_kulka, strzalka, kulki_na_gorze, nastepny_kolor
    size(800, 600)
    kolor_kulki = randomowy_kolor()
    nastepny_kolor = randomowy_kolor()
    strzala_kulka = Kulki(400, 550, 50, kolor_kulki)
    strzalka = loadImage("strzalka.png")
    kulki_na_gorze = generuj_kulki()
def sprawdz_kolizje(kuleczki, pociski): #Miłosz, ale trzeba jeszcze poprawić jak coś
    for kula in kuleczki:
        for pocisk in pociski:
            distance = dist(kula.x, kula.y, pocisk.x, pocisk.y)
            if distance <= kula.radius / 2 + pocisk.radius / 2:
                kuleczki.remove(kula)
                pociski.remove(pocisk)
                break
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
            
    sprawdz_kolizje(kulki_na_gorze, pociski)  # Sprawdzenie kolizji kulki-pociski
    
    strzala_kulka.display()

    
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
    
    #start_screen() - jak się odkomentuje to wyświetlany jest ekran startowy
