import os
class Config(object):
      def __init__(self):
          self.BotToken     = os.environ.get('7526289167:AAFrnM2xlRL91ptBlX6NxdSJ_N_A0Rqtm04','')
          self.api_id = os.environ.get('20446108','')
          self.api_hash = os.environ.get('025f6661faa3e16c1461f8aa4f4f94ce','')
          self.AdminUsers = str(os.environ.get('alba_gonzales','')).split(',')
          self.ChunkSizeTel = 2000
          
          self.ChunkSize    = 150
          self.ChunkFixed   = 150
          self.FileLimit    = 1024 * 1024 * 150
          self.ExcludeFiles = ['bot.py','Config.py','multiFile.py','requirements.txt','Procfile','__pycache__','.git','.profile.d','.heroku','bot.session','bot.session-journal','output']
          self.ChunkedFileLimit = 1024 * 1024 * 1024
          self.InProcces = False
          #self.BotChannel = '-1001432878672'
          self.current_user_msg = ''
          self.current_chanel_msg = ''
          self.procesing = False
          self.watching = False
          self.watch_message = []
          self.users = []
          self.userindex = 0
          self.parte= 0
          self.total= 0
          self.totalsub= 0

      def setChunkSize(self,chunk : int):
          self.ChunkSize = chunk

      def setChunkSizeTel(self,chunk : int):
          self.ChunkSizeTel = chunk

      def toStr(self):
          return '[Chunk Size]\n' + str(self.ChunkSize) + '\n\n[ChunkSizeTel]\n' + str(self.ChunkSizeTel)

      


