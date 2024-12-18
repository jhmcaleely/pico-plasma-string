from PIO_WS2812B_NeoPixel import set_LED, refresh_LEDs, NUM_LEDS
import random
import time

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

while True:
    no_pixels_updated = random.randint(1, 5)
    for _ in range(no_pixels_updated):
        pixel = random.randint(0, NUM_LEDS-1)
        r, g, b = random_color()
        set_LED(pixel, r, g, b)
    pixel_off = random.randint(0, NUM_LEDS-1)
    set_LED(pixel_off, 0, 0, 0)
    refresh_LEDs()
    sleeptime = random.randint(1, 3);
    time.sleep(0.1* sleeptime)