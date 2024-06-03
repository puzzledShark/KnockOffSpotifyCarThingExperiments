import machine
import utime

# Define the UART
uart = machine.UART(0, baudrate=9600, tx=0, rx=1)

# Define pins for the encoder
clk_pin = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
dt_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)

# Define pins for the buttons
BLUE_BUTTON_PIN = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
RED_BUTTON_PIN = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
YELLOW_BUTTON_PIN = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
GREEN_BUTTON_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
ENCODER_BUTTON_PIN = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Initial states
last_clk = clk_pin.value()
counter = 0
button_pressed = 0

# Dictionary to store last button press time
last_press_time = {
    BLUE_BUTTON_PIN: 0,
    RED_BUTTON_PIN: 0,
    YELLOW_BUTTON_PIN: 0,
    GREEN_BUTTON_PIN: 0,
    ENCODER_BUTTON_PIN: 0
}

def rotary_changed(pin):
    global last_clk, counter
    current_clk = clk_pin.value()
    current_dt = dt_pin.value()
    if current_clk != last_clk:  # Only count changes
        if current_dt != current_clk:
            counter += 1
            uart.write("VolumeUp".encode())
        else:
            counter -= 1
            uart.write("VolumeDown".encode())
        print("Counter:", counter)
        #uart.write("Counter:" + str(counter) + '\n')
    last_clk = current_clk
    
# Attach interrupts
clk_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=rotary_changed)

# Function to handle button presses with debounce
def handle_button_press(pin):
    global button_pressed
    current_time = utime.ticks_ms()
    if current_time - last_press_time[pin] > 400:  # Debounce time: 200ms
        last_press_time[pin] = current_time
        if pin == BLUE_BUTTON_PIN:
            button_name = "Blue Button"
        elif pin == RED_BUTTON_PIN:
            button_name = "Red Button"
        elif pin == YELLOW_BUTTON_PIN:
            button_name = "Yellow Button"
        elif pin == GREEN_BUTTON_PIN:
            button_name = "Green Button"
        elif pin == ENCODER_BUTTON_PIN:
            button_name = "Encoder Button"
        else:
            button_name = "Unknown Button"
        
        button_pressed += 1
        #print(f"{button_name} pressed ", button_pressed)
        #uart.write(f"{button_name}")
        uart.write("Hello, PC #{}\n".format(button_pressed).encode())
        utime.sleep(0.1)

# Attach interrupts for each button pin
BLUE_BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_button_press)
RED_BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_button_press)
YELLOW_BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_button_press)
GREEN_BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_button_press)
ENCODER_BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=handle_button_press)

# Main loop
while True:
    utime.sleep(0.1)