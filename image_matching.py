from urllib.request import urlopen
import re

print("Script started!")

web_urls = ['https://www.geeksforgeeks.org/', 'http://olympus.realpython.org/profiles/aphrodite']
search_tags = ["ndi", "6-min", "aphrodite"]
img_tags = [""]
for url in web_urls:

	page = urlopen(url)

	html = page.read()
	html = html.decode("utf-8")

	img_tags.extend(re.findall("<img.*>", html, re.IGNORECASE))


for img in img_tags:
	flag = False

	img_src = re.search('src*([^\s]+)', img, re.IGNORECASE)
	if(img_src is not None):
		img_src = img_src.group(0)

	img_alt = re.search('alt.*"', img, re.IGNORECASE)
	if(img_alt is not None):
		img_alt = img_alt.group(0)

	for search_tag in search_tags:
		if(img_src is not None and search_tag in img_src):
			flag = True
			break
		if(img_alt is not None and search_tag in img_alt):
			flag = True
			break

	if(flag is True):
		print(img_src[4:])


