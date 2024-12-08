from Alcohol_Total_Game import total_game

tg = total_game()

#비용 계산
tg.Receipt()

#취한 정도 파악 게임
# (음성파일은 반드시 웨이브 파일로 업로드 해야합니다.)
# ex) pronunciation.wav
#pronunciationApp(Sample).wav 파일 업로드
tg.PronunciationApp()


#사진 벌칙 게임
#GroupPhotoAnalyzerApp(Sample).jpg 파일 업로드
tg.GroupPhotoAnalyzerApp()

#사진 기반 인물 퀴즈
images = [
    {"image": "IGJ.jpg", "answer": "Person 1"},
    {"image": "hanyang.jpg", "answer": "Person 2"}
]
tg.GuesseGameApp(images)

#룰렛 벌칙 게임
tg.RoulettGame(['벌칙1','벌칙2','벌칙3'])
