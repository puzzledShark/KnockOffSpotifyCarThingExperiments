from machine import Pin, UART
import utime

# Rotary encoder pins
clk = Pin(4, Pin.IN)
dt = Pin(5, Pin.IN)


play_but = Pin(12, Pin.IN, Pin.PULL_UP)
next_but = Pin(0, Pin.IN, Pin.PULL_UP)
previous_but = Pin(13, Pin.IN, Pin.PULL_UP)

# UART setup
uart = UART(0, baudrate=115200, tx=Pin(1), rx=Pin(3))

# Rotary encoder state variables
counter = 0
last_state = 0

def rotary_encoder_callback(pin):
    global counter, last_state

    clk_state = clk.value()
    dt_state = dt.value()

    if clk_state != last_state:
        if dt_state != clk_state:
            counter += 1
            uart.write("VolumeUp")
        else:
            counter -= 1
            uart.write("VolumeDown")
        #uart.write("Counter: {}\n".format(counter))
    
    last_state = clk_state


# Attach interrupts for rotary encoder pins
clk.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_encoder_callback)
dt.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=rotary_encoder_callback)


# Main loop
while True:
        # Read button states
    if play_but.value() == 0:
        # Button 1 is pressed
        # Perform button 1 action
        uart.write("Play")
        utime.sleep_ms(200)  # Optional debounce delay

    if next_but.value() == 0:
        # Button 2 is pressed
        # Perform button 2 action
        uart.write("Next")
        utime.sleep_ms(200)  # Optional debounce delay

    if previous_but.value() == 0:
        # Button 3 is pressed
        # Perform button 3 action
        uart.write("Previous")
        utime.sleep_ms(200)  # Optional debounce delay
    utime.sleep_ms(1)  # Sleep to reduce CPU usage
