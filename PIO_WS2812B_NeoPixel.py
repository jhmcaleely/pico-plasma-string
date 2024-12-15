import array, time
from machine import Pin
from rp2 import PIO, StateMachine, asm_pio

# Configure the number of WS2812 LEDs.
NUM_LEDS = 50

# pio deals in 32 bit machine words
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

@asm_pio(sideset_init=PIO.OUT_LOW,
         out_shiftdir=PIO.SHIFT_LEFT,
         autopull=True,
         pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1)				.side(0) [T3 - 1]
    jmp(not_x, "do_zero")	.side(1) [T1 - 1]
    jmp("bitloop")			.side(1) [T2 - 1]
    label("do_zero")
    nop()					.side(0) [T2 - 1]

def set_LED(n, r, g, b):
    ar[n] = (r << 16) + (g << 8) + b

def refresh_LEDs():
    sm.put(ar, 8) # shift 8 bits, as we will ignore 8 of every 32.

# Create a StateMachine with the ws2812 code and output on Pin(15).
# Pin 15 matches Pimoroni Plasma Stick 2040W
sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(15))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)
