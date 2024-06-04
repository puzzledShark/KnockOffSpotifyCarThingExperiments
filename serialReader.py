import threading
import time
import serial

#This simply waits on msgs from the serial device and does things with it
class SerialReader(threading.Thread):
    
    
    def __init__(self, uart, foobarController):
        super().__init__()
        self.uart = uart
        self.running = True
        self.foobarController = foobarController

    def run(self):
        while self.running:
            if self.uart.in_waiting > 0:
                data = self.uart.readline().strip()
                #print("Received from device:", data.decode())
                self.commandHandler(data.decode())
                
    def commandHandler(self, command):
        print("(" , command , ")")
        if(command == "Play"):
            print("play")
            self.foobarController.playpause()
        elif(command == "Next"):
            print("Next")
            self.foobarController.next()
        elif(command == "Previous"):
            print("Previous")
            self.foobarController.previous()
        elif(command == "VolumeUp"):
            print("Up")
            self.foobarController.volumeUp()
        elif(command == "VolumeDown"):
            print("Dn")
            self.foobarController.volumeDown()


    def stop(self):
        self.running = False
