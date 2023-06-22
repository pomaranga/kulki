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

class Pocisk(Kulki):
    def __init__(self, x, y, radius, color):
        Kulki.__init__(self, x, y, radius, color)
        self.speed = 5  # predkosc pocisku, mozna zmienic jesli trzeba
    
    def move(self): # na razie tylko w górę leci
        self.y -= self.speed
    
    def wylecial(self): # sprawdzenie czy pocisk wylecial poza ekran
        return 
        (
            self.y + self.radius < 0 or
            self.x - self.radius > width or
            self.x + self.radius < 0 or
            self.y - self.radius > height
        )
    

def mousePressed():
    global strzala_kulka
    color = strzala_kulka.color  # Pobieramy kolor z kulki na dole zeby pocisk mial ten sam kolor
    pocisk_tymczasowy = Pocisk(strzala_kulka.x, strzala_kulka.y, strzala_kulka.radius, color)
    pociski.append(pocisk_tymczasowy)
    strzala_kulka.color = randomowy_kolor()  # Zmiana koloru kulki na dole

def setup():
    global strzala_kulka
    size(800, 600)
    kolor_kulki = randomowy_kolor()
    strzala_kulka = Kulki(400, 550, 50, kolor_kulki)

def draw():
    global strzala_kulka
    background(200)
        
    for p in pociski:
        p.move()
        p.display()
        if p.wylecial():
            pociski.remove(p)
    
    strzala_kulka.display()
