from foobarhttp import FoobarRemote
import requests


class FoobarController:

    def __init__(self) -> None:
        self.foobarRemote = FoobarRemote("localhost")
        self.state = self.foobarRemote.state()
        self.volumeIncrement = 5

    def playpause(self):
        self.foobarRemote.cmd("PlayOrPause")
        return self.foobarRemote.state()
    
    def next(self):
        self.foobarRemote.cmd("StartNext")
        return self.foobarRemote.state()
    
    def previous(self):
        self.foobarRemote.cmd("StartPrevious")
        return self.foobarRemote.state()
    
    def nextRandom(self):
        self.foobarRemote.cmd("StartRandom")
        return self.foobarRemote.state()
    
    def volumeUp(self):
        self.state = self.foobarRemote()
        self.foobarRemote.cmd("Volume", int(self.state['volume']) + self.volumeIncrement)
        return self.foobarRemote.state()

    def volumeDown(self):
        self.state = self.foobarRemote()
        self.foobarRemote.cmd("Volume", int(self.state['volume']) - self.volumeIncrement)
        return self.foobarRemote.state()
    
    def volumeSet(self, set):
        self.foobarRemote.cmd("Volume", set)
        return self.foobarRemote.state()

    def getAlbumArt(self):
        self.state = self.foobarRemote.state()
        url = 'http://localhost:8888/' + self.state['albumArt']
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

