from random import randint
from time import sleep
from PIO_WS2812B_NeoPixel import set_LED, refresh_LEDs
import array

chase = randint(0, 50)
chase2 = randint(0, 50)
chase3 = randint(0, 50)

pixels = list(range(50))



def pixel(n, r, g, b):
    pixels[n] = (r, g, b)
    

def display_pixels():
    for i in range(len(pixels)):
        r, g, b = pixels[i]
        set_LED(i, r, g, b)
    refresh_LEDs()


while True:
    for i in range(50):
        pixel(i, 0, 0, 0)
    
    for i in range(50):
        
        if i == chase:
            pixel(i,          0, 0, 255)
            pixel((i+1) % 50, 0, 0, 32)
            pixel((i-1) % 50, 0, 0, 32)
            pixel((i-2) % 50, 0, 0, 4)
            
        elif i == chase2:
            pixel(i,          255, 0, 0)
            pixel((i+1) % 50, 32,  0, 0)
            pixel((i-1) % 50, 32,  0, 0)
            pixel((i-2) % 50, 4,  0, 0)
            
        elif i == chase3:
            pixel(i,          0, 255, 0)
            pixel((i-1) % 50, 0, 32,  0)
            pixel((i+1) % 50, 0, 32,  0)
            pixel((i+2) % 50, 0, 4,  0)
        
        if chase == chase3 == i:
            pixel(i, 255, 255, 0)
            pixel((i + 2) % 50, 4, 4, 0)
            pixel((i + 1) % 50, 255, 255, 0)
            pixel((i - 1) % 50, 255, 255, 0)
            pixel((i - 2) % 50, 4, 4, 0)
            display_pixels()
            sleep(0.5)
            
    display_pixels()
    
    chase = (chase + 1) % 50
    chase2 = (chase2 + randint(-1, 1)) % 50
    chase3 = (chase3 - 1) % 50
    sleep(0.1)
