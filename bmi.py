#BMI值計算公式： BMI = 體重(公斤)/體重(公尺)平方

weight = float(input('請輸入體重(kg)：'))
height = float(input('請輸入身高(cm)：'))

height = height / 100

bmi = weight / height**2

if(bmi < 18.5):
	level = '體重過輕'
elif(bmi >= 18.5 and bmi < 24):
	level = '體重正常'
elif(bmi >= 24 and bmi < 27):
	level = '過重'
elif(bmi >= 27 and bmi < 30):
	level = '輕度肥胖'
elif(bmi >= 30 and bmi < 35):
	level = '中度肥胖'
elif(bmi >= 35):
	level = '重度肥胖'

print('您的BMI值為 =', bmi, level)

