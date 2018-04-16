# Taiwo Kareem
# 05/04/2018 04:09 AM

import sys
import requests
import re
import time
import os
import json
from urllib.parse import urljoin  # Python3

if len(sys.argv) != 2:
	sys.exit('Usage: python %s "<config_filename>"' % __file__)


config_file = sys.argv[1]
config = {}

if os.path.isfile(config_file):
	with open(config_file) as f:
		try:
			config = json.load(f)
		except json.decoder.JSONDecodeError as err:
			sys.exit("ERROR: Invalid json data in file. %s" % err)

else:
	sys.exit("Config file: '%s' not found" % config_file)


URL = config.get("domain")
filename = config.get("output_filename")
URL_REGEX = config.get("path_regex")
KEYWORD_REGEX = config.get("keyword_regex")

AUTH = config.get("login")
s = requests.Session()
	

s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:27.0) Gecko/20100101 Firefox/27.0',
})


if AUTH and AUTH != "username:password":
	AUTH = tuple(AUTH.split(":"))
	s.auth = AUTH
	s.post(URL, auth=AUTH)


opened=[]
visited=[]
hits=0
mode="w"
MATCHES = []


if os.path.isfile(filename):
	with open(filename) as f:
		visited = f.read().split("\n")
		mode = "a"

with open(filename, mode) as f:
	def process(url, visited=visited, hits=hits, s=s):
		LINKS = []

		page_crawled = False
		for pages in opened:
			if pages == url:
				page_crawled = True

		if page_crawled == False:
			opened.append(url)

			text = s.get(url).text
			
			for link in re.findall(r'href="(.*?)"', text):
				link = urljoin(url, link).split("#")[0]#.split("?")[0]

				LINKS.append(link.lower())

			for link in list(set(LINKS)):
				if link.startswith(URL):
					if link not in visited:
						if re.search(URL_REGEX, link, re.I):

							source = s.get(link).text
							# ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)
							matches = set(re.findall(r"{0}".format(KEYWORD_REGEX), source, re.I))

							if matches:
								hits += 1
								print("\n[%s] (%s/%s) -> %s" % (len(matches), hits, len(visited), link))

							else:
								matches = []
								
							for email in matches:
								if email not in MATCHES:
									print(email.lower())
									f.write(email.lower() + "\n")
									f.flush()
									MATCHES.append(email)
							
						try:
							visited.append(link)
						except:
							time.sleep(3)
					else:
						print(".", end="", flush=True)

					try:
						process(link, hits=hits)
					except Exception as e:
						time.sleep(3)
						print("\n--", e)

	try:
		process(URL, hits=hits)
	except Exception as e:
		print(e)
		time.sleep(3)
