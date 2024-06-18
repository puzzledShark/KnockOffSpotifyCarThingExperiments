import threading
import time
import serial
from pykakasi import kakasi
import pillowFunctions
from serialReader import SerialReader


example_data_array = [
        [
            "キラッ！満開スマイル (U149 Version)",
            "THE IDOLM@STER CINDERELLA GIRLS U149 (04) オリジナル CD",
            "Playing",
            "25",
            "4:19",
            "1:14"
        ],
        [
            "Test Song",
            "Test Album",
            "Stopped",
            "40",
            "2:33",
            "2:14"
        ],
        [
            "Test Song1",
            "Test Album1",
            "Stopped1",
            "75",
            "2:33",
            "2:14"
        ]
        ]
musicIterator = iter(example_data_array)
example_album_art = ['testimage.jpg', 'testimage2.jpg', 'converted.png']


iterator = iter(example_album_art)

def japanese_to_romaji(text):
    # Create kakasi instance
    k = kakasi()

    # Set parameters for conversion
    k.setMode('H', 'a')  # Hiragana to romaji
    k.setMode('K', 'a')  # Katakana to romaji
    k.setMode('J', 'a')  # Kanji to romaji

    # Create converter
    conv = k.getConverter()

    # Convert text
    result = conv.do(text)

    return result


class SerialSender(threading.Thread):
    def __init__(self, uart, foobarController):
        super().__init__()
        self.uart = uart
        self.foobarController = foobarController
        self.running = True
        # Define the array data (placeholders for demonstration)

    def run(self):
        while self.running:
            self.send_array(next(musicIterator))
            self.send_albumart(next(iterator))
            time.sleep(2)

    def send_array(self, array):
        self.uart.write("A\n".encode('utf-8'))
        time.sleep(0.1)
        for item in array:
            self.uart.write(japanese_to_romaji(item).encode('utf-8'))  # Send each item followed by newline
            self.uart.write("\n".encode('utf-8'))
            time.sleep(0.1)  # Delay between sending each item
        
        print("Array sent successfully.")

    #This is a temporary solution, its not ideal
    def send_albumart(self, image):

        imageSize = (60, 51)
        processedImage = pillowFunctions.processImage(image, imageSize)

        # Alert arduino to get ready to process Image
        uart.write("I\n".encode('utf-8'))
        time.sleep(0.4)

        # Send Size of data
        data_length = len(processedImage)
        print(">Data Length:",data_length)
        uart.write(f"{data_length}".encode('utf-8'))
        time.sleep(1)

        # Send image data
        uart.write(processedImage)

    def stop(self):
        print("Stopping Sender")
        self.running = False

if __name__ == "__main__":
    serial_port = 'COM4'  # Update with your Arduino serial port
    uart = serial.Serial(serial_port, 115200, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize

    # reads serial and just prints out commands to console
    uart_thread = SerialReader(uart, "")
    uart_thread.start()
    time.sleep(2)

    sender = SerialSender(uart, 'NULL')
    sender.start()

    try:
        while True:
            time.sleep(1)  # Main thread sleep
    except KeyboardInterrupt:
        sender.stop()
        sender.join()

    uart.close()
    print("Serial communication stopped.")



