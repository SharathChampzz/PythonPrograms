from selenium import webdriver

repeat = True
driver = webdriver.Chrome("chromedriver.exe") 
driver.get("https://web.whatsapp.com/") 

while repeat:
	try:
		name = input('Enter Target : ')
		msgn = input('Enter msg : ')
		count  = int(input('Enter msg count.. : '))
		title = '//span[@title="' + name + '"]'

		user = driver.find_element_by_xpath(title)
		user.click()

		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
		for i in range(count):
			msg_box.send_keys(msgn)
			btn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
			btn.click()
			print(f'Sent : {i}')
		rep = input('Do you Want to Continue? (yes / no) : ').lower().rstrip()
		if rep == "no":
			repeat = False

	except Exception as e:
		print(e)

print('Done!!')
