import http.client
import time


print("10 min interval")
resp_code = 200
counter = 0
while resp_code == 200:
	con = http.client.HTTPConnection('booking.uz.gov.ua')

	body = "station_id_from=2200001&station_id_till=2200260&station_from=%D0%9A%D0%B8%D0%B5%D0%B2&station_till=%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D0%B5%D1%86-%D0%9F%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9&date_dep=28.10.2016&time_dep=00%3A00&time_dep_till=&another_ec=0&search="

	headers = {
		"Host": "booking.uz.gov.ua",
		"Origin": "http://booking.uz.gov.ua",
		"Content-Type": "application/x-www-form-urlencoded",
		"GV-Ajax": 1,
		"GV-Screen": "1440x900",
		"GV-Referer": "http://booking.uz.gov.ua/ru/",
		"GV-Token": "80da37a32720caec40cee91b2a769a50",
		"Cookie": "_gv_sessid=98nhdfdr48k54r8m1kjlf3v8v2"
	}
	con.request("POST","/ru/purchase/search/",body,headers)
	resp = con.getresponse()
	resp_code = resp.status
	counter += 1
	print(counter, "-", resp_code)
	time.sleep(10*60)