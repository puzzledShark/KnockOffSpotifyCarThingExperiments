import serial
import time

# Configure the serial port
serial_port = "COM3"  # Replace with the appropriate COM port for your device
baud_rate = 9600  # Match this with the baud rate used by your Pico board

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    # Initialize counter
    counter = 0


    while counter < 10:
        # Send message to Pico board
        message = "Hello, Pico #{}\n".format(counter)
        ser.write(message.encode())
        print("Sent to Pico:", message)

        # Receive response from Pico board
        response = ser.readline().decode().strip()
        print("Received from Pico:", response)

        # Increment counter
        counter += 1

except serial.SerialException as e:
    print("Serial port error:", e)

finally:
    # Close the serial port
    ser.close()
