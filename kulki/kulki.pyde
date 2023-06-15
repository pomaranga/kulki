import random  #karolina

def randomowy_kolor():
    kolory = [
        color(255, 0, 0),
        color(0, 255, 0),
        color(0, 0, 255), 
    ]
    return random.choice(kolory)

def setup():
    size(800, 600)
    kolor_kulki = randomowy_kolor()
    fill(kolor_kulki)

def draw():
    ellipse(width/2, height-45, 45, 45)
    stroke(255, 255, 255)
    strokeWeight(2)  
    smooth()    

def mousePressed():  #to jest tymczasowe, potem można to zmienić na jakiś inny warunek
    kolor_kulki = randomowy_kolor()
    fill(kolor_kulki)
