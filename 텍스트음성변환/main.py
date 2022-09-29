# pip install playsound==1.2.2  재생이 안 될 때
from gtts import gTTS  # 텍스트를 음성으로 변환
from playsound import playsound  # mp3파일 파이썬으로 재생하기 위한 라이브러리

# 텍스트를 음성으로 변환
file_path = 'Mydata.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()
# text = "안녕하세요. 파이썬입니다."
# tts = gTTS(text=text, lang='ko')
tts = gTTS(text=read_file, lang='ko')
mp = (".\mp3\schoolsong.mp3")
tts.save(mp)

# mp3파일 파이썬으로 재생하기 위한 라이브러리
playsound(mp)
