import random

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
    kolory = [
        color(255, 0, 0),
        color(0, 255, 0),
        color(0, 0, 255),
        color(0, 255, 255),
        color(255, 0, 255),
        color(255, 255, 0), 
    ]
    return random.choice(kolory)

def mousePressed():
    kolor_kulki = randomowy_kolor()
    strzala_kulka.color = kolor_kulki

def setup():
    global strzala_kulka
    size(800, 600)
    kolor_kulki = randomowy_kolor()
    strzala_kulka = Kulki(400, 550, 50, kolor_kulki)


def draw():
    global strzala_kulka
    strzala_kulka.display()
    
setup()
