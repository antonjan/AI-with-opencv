from gtts import gTTS
#import os
#import vlc
import subprocess
result = subprocess.run(['ls', '-l'])
tts = gTTS(text="Hello. This is anton speeking what do you want to do today", lang='en')
tts.save("out.mp3")
result = subprocess.run(['ffplay','out.mp3'])

#p = vlc.MediaPlayer("out.mp3")
#p.play()
#os.system(ffplay "out.mp3")
