import serial
import threading

# Configure the serial port
serial_port = "COM3"  # Replace "COM3" with the appropriate COM port for your Pico
baud_rate = 9600  # Match this with the baud rate in your MicroPython script

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Function to continuously read from the serial port in a separate thread
def serial_reader():
    while not exit_event.is_set():
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(line)
        except UnicodeDecodeError:
            # Handle UnicodeDecodeError if non-UTF-8 data is received
            pass

try:
    # Create an event to signal the thread to exit
    exit_event = threading.Event()

    # Create and start the serial reader thread
    serial_thread = threading.Thread(target=serial_reader)
    serial_thread.start()

    # Wait for KeyboardInterrupt
    while True:
        pass  # Keep the main thread running until KeyboardInterrupt

except KeyboardInterrupt:
    pass  # Handle KeyboardInterrupt outside the main loop

finally:
    # Signal the serial reader thread to exit
    exit_event.set()

    # Wait for the serial reader thread to finish
    serial_thread.join()

    # Close the serial port before exiting
    ser.close()
    print("Serial port closed.")
