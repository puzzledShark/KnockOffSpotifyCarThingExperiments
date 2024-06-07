import serial
from serialReader import SerialReader
import time
import yaml
from foobarControllerV2 import FoobarController

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

def main():
    foobarController = FoobarController()

    # Configure UART via USB CDC using pyserial
    uart = serial.Serial(config['COMport'], baudrate=115200, timeout=1)

    # Create and start the UART thread
    uart_thread = SerialReader(uart, foobarController)
    uart_thread.start()

    try:
        while True:
            time.sleep(1)  # Keep the main thread running
    except KeyboardInterrupt:
        pass

    uart_thread.stop()
    uart_thread.join()

    uart.close()
    print("UART thread has been stopped and joined.")

if __name__ == "__main__":
    main()
