#BMI值計算公式： BMI = 體重(公斤)/體重(公尺)平方

weight = float(input('請輸入體重：'))
height = float(input('請輸入身高：'))

bmi = weight / height**2
print('BMI =', bmi)