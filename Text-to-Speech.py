from gtts import gTTS
import os
tts = gTTS(text="Hello. Join telegram channel @OpenCV_olc", lang='en')
tts.save("out.mp3")
  
os.system("out.mp3")
