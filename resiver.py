from telethon.tl.types import UpdateShortMessage, PeerUser
from speaker import speaker

class resiver:

  def __init__(self, client):
    self.client = client
    self.client.add_update_handler(self.callback)
    self.voice = speaker('ru')

  def callback(self, update):
    if isinstance(update, UpdateShortMessage) and not update.out:
      user = self.client.get_entity(update.user_id)
      self.voice.say('Сообщение от ' + user.first_name + ': ' + update.message)