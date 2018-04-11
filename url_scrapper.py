# Taiwo Kareem
# 05/04/2018 04:09 AM

import sys
import requests
import re
import time
import os

try:
    from urlparse import urljoin  # Python2
except ImportError:
    from urllib.parse import urljoin  # Python3


if len(sys.argv) != 4:
	sys.exit('Usage: python %s "<url>" "<filename>" "<keywords,another>"' % __file__)
else:
	URL = sys.argv[1]
	filename = sys.argv[2]
	keywords = sys.argv[3].split(",")


opened=[]
visited=[]
KEYWORDS=r"|".join(keywords)
hits=0
mode="w"

if os.path.isfile(filename):
	with open(filename) as f:
		visited = f.read().split("\n")
		mode = "a"

with open(filename, mode) as f:
	def process(url, visited=visited, hits=hits):
		LINKS = []

		page_crawled = False
		for pages in opened:
			if pages == url:
				page_crawled = True

		if page_crawled == False:
			opened.append(url)

			text = requests.get(url).text
			
			for link in re.findall(r'href="(.*?)"', text):
				link = urljoin(url, link).split("#")[0]#.split("?")[0]

				LINKS.append(link.lower())

			for link in list(set(LINKS)):
				if link.startswith(URL):
					if link not in visited:
						print(".", end="", flush=True)
						if re.search(KEYWORDS, link, re.I):
							hits += 1
							print()
							print("(%s/%s) -> %s" % (hits, len(visited), link))

							f.write(link + "\n")
							f.flush()
						
						try:
							visited.append(link)
						except:
							time.sleep(3)
					
					try:
						process(link, hits=hits)
					except Exception as e:
						time.sleep(3)
						print("\n--", e)

	try:
		process(URL, hits=hits)
	except Exception as e:
		print(e)
