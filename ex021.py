from pygame import init, mixer, event

init()
mixer.music.load('ocean.mp3')
mixer.music.play()
event.wait()
