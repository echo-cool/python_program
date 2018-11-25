import requests
from bs4 import BeautifulSoup
import csv
csvFile3 = open('bi.csv', 'w', newline='')
writer2 = csv.writer(csvFile3)

global target
target = ["http://www.yuying.org.cn/yuying/html/main/col104/column_104_1.html",]
def get(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text.encode('utf-8'), "html.parser")
	for i in soup.find_all("a"):
		if i.get("target") == "_blank" :
			print(i.string)
			print("http://www.yuying.org.cn"+i.get("href"))
			target.append("http://www.yuying.org.cn"+i.get("href"))
			writer2.writerow([i.string,"http://www.yuying.org.cn"+i.get("href")])


for i in target:
	try:
		get(i)
	except:
		print("ERROR")