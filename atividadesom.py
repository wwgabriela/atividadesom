import os 
from gtts import gTTS
ptexto="opa, deixa eu gerar esse texto aqui"
tts=gTTS(text=ptexto, lang='pt')
tts.save("audioaula.mp3")
os.system("mpg321   audioaula.mp3")

os.system('start audioaula.mp3')