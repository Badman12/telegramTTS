from pygame import mixer
from gtts import gTTS
from threading import Thread
import os
import uuid
import time

class speaker:

  queue = []
  inPlay = False

  def __init__(self, lng):
    self.lng = lng

  def say(self, text):
    trackname = 'tmp/' + str(uuid.uuid4()) + '.mp3'
    info = {'name': trackname, 'play': False}
    tts = gTTS(text=text, lang=self.lng)
    tts.save(trackname)
    self.queue.append(info)
    if not self.inPlay:
      thread = Thread(target=self.speak)
      thread.start()

  def speak(self):
    self.inPlay = True
    for track in self.queue:
      mixer.init()
      mixer.music.load(track['name'])
      mixer.music.play()

      while mixer.music.get_busy():
        time.sleep(1)

      os.remove(track['name'])
      self.queue.remove(track)
    
    if (len(self.queue) > 0):
      self.speak()

    self.inPlay = False

