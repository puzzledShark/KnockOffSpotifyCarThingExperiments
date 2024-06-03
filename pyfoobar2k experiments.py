from foobarhttp import FoobarRemote
import requests

foobarRemote = FoobarRemote("localhost")
state = foobarRemote.state()
print(state)
# Other commands:
# Stop, PlayOrPause, Start, StartNext, StarPrevious, StartRandom
# VolumeLevel
foobarRemote.cmd("StartNext")
foobarRemote.cmd("Volume", int(state['volume']) + 5)
state = foobarRemote.state()
print(state)




def download_image():
    global foobarRemote
    state = foobarRemote.state()
    save_path = "albumArt.jpg"
    url = 'http://localhost:8888/' + state['albumArt']
    try:
        # Send a GET request to the image URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Open a file in binary-write mode
            with open(save_path, 'wb') as file:
                # Write the contents of the response to the file
                file.write(response.content)
            print(f"Image successfully downloaded: {save_path}")
        else:
            print(f"Failed to retrieve image. Status code: {response.status_code}")
            download_image(url, save_path)
    except Exception as e:
        print(f"An error occurred: {e}")


#download_image()

trackTitle = ""
#while(True):
#    state = foobarRemote.state()
#    if(trackTitle != state["title"]):
#        trackTitle = state["title"]
#        print(state)
