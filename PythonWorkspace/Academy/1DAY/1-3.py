menu = {'짜장면':5000,'짬뽕':6000,'볶음밥':7000}
total = 0

while(True):
	foodSel = input("주문할 음식:")
	num = int(input("몇개주문:"))
	sel = input("다른메뉴주문:")
	total = total+menu[foodSel] * num
	if(sel != "yes"):
		print("주문 총합액은:%d"%total)
		break
	

