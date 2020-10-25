driving = input('請問是否開過車?')
if drivinf != '有' and driving != '沒有'
	print('只能輸入有或沒有')
	raise SystemExit
	
age = input('輸入你的年齡:')
age = int(age)
if driving == '有':
	if age >=18:
		print('你通過測驗了')
	else:
		print('違法開車喔')
elif driving == "沒有":
	if age>= 18:
		print(' 去考駕照喔')
	else:
		print('很好，滿18就可以考照了喔')
else:
	print('請輸入 有 或 沒有 ')