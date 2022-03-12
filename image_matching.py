from urllib.request import urlopen
import re

web_urls = ['https://www.geeksforgeeks.org/', 'http://olympus.realpython.org/profiles/aphrodite', 'https://stackoverflow.com/users/1490552/adem-%c3%96zta%c5%9f']
search_tags = ["ndi", "6-min", "aphrodite", "imgur"]
img_tags = [""]

for url in web_urls:	#loop to open the URLs and obtain only img tags from the html

	page = urlopen(url)

	html = page.read()
	html = html.decode("utf-8")

	img_tags.extend(re.findall("<img.*>", html, re.IGNORECASE)) #adds all img tags of all websites to this list, regex used to find img tags


for img in img_tags:
	flag = False

	img_src = re.search('src*([^\s]+)', img, re.IGNORECASE)	#obtain only the src part from the img tag
	if(img_src is not None):
		img_src = img_src.group(0)

	img_alt = re.search('alt.*"', img, re.IGNORECASE)		#obtain only the alt part from the img tag
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
		print(img_src[4:])		#remove the "src=" part before printing


