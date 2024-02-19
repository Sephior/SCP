from konlpy.tag import Kkma
import tensorflow as tf

kkma = Kkma()
text = "어느 회사에 근무하는 직원들이 출근하는데 소요되는 시간은 평균이 30분이고 표준편차가 9분인 정규분포를 따른다.\n 무작위로 한 직원을 추출했을 때, 이 직원의 출근시간이 1시간 이상일 확률을 구하라"
nouns = kkma.nouns(text)
pos_tags = kkma.pos(text)

print("명사:", nouns)
print("품사 태깅:", pos_tags)

# 단어 정규분포가 존재하는지 확인
# 
# 이 + ㄴ가 / 구하 / 계산 이라는 단어를 기점으로 목표를 지정
# -> 확률 이라는 단어가 나오면 
# 평균 / 표준편차 / 


# 간단한 모델 디자인
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=32, output_dim=2, input_length=128),
    tf.keras.layers.LSTM(units=64),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # 2는 예측할 클래스의 수
])

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit(pos_tags, [("출근시간", "1시간"), ("평균", "30분"), ("표준편차", "9분")], epochs=10,verbose=2)

predict = model.predict(pos_tags)
# blue predict line, black dots of random data
print(predict)