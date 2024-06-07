import requests
import socket


class FoobarController:
    def __init__(self, foorbarURL='localhost') -> None:
        self.url = foorbarURL
        self.volumeIncrement = 5
        self.recipient_address = self.url
        self.recipient_port = 12345
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def sendCommand(self, command):
        self.sender_socket.sendto(command.encode(), (self.recipient_address, self.recipient_port))

    def playpause(self):
        self.sendCommand("Play")
        return True
    
    def next(self):
        self.sendCommand("Next")
        return True
    
    def previous(self):
        self.sendCommand("Previous")
        return True
    
    def nextRandom(self):
        self.sendCommand("NextRandom")
        return True
    
    def volumeUp(self):
        self.sendCommand("VolumeUp")
        return True
    
    def volumeDown(self):
        self.sendCommand("VolumeDown")
        return True
    
    def volumeSet(self, set):
        self.sendCommand("VolumeSet:", set)
        return True

    #Needs fix
    def getAlbumArt(self):
        self.state = self.foobarRemote.state()
        url = 'http://' + self.url + ':8888/' + self.state['albumArt']
        try:
            # Send a GET request to the image URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Open a file in binary-write mode
                with open('albumArt', 'wb') as file:
                    # Write the contents of the response to the file
                    file.write(response.content)
                print("Image successfully downloaded album art")
            else:
                print(f"Failed to retrieve image. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return self.foobarRemote.state()

