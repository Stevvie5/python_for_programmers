from html.parser import HTMLParser
import requests
from time import sleep

class MyParser(HTMLParser):
	links = []
	title = ''
	typeIsTitle = False
	
	def __init__(self, url, base):
		super().__init__()
		self.url = url
		self.base = base
	
	def handle_starttag(self, tag, attributes):
		if tag == 'title':
			self.typeIsTitle = True
		elif tag == 'a':
			for attribute in attributes:
				if attribute[0] == 'href' and attribute[1] != None:
					if attribute[1][0] == '/':
						self.links.append(self.url + attribute[1])
					elif self.base in attribute[1]:
						self.links.append(attribute[1])
												
					
	def handle_data(self, data):
		if self.typeIsTitle == True:
			self.title = data
			self.typeIsTitle = False
					
siteMap = {}
def recurse(url):
	parser = MyParser(url, 'nscds.org')
	request = requests.get(url)
	
	requestString = request.text
	parser.feed(requestString)
	
	siteMap[url] = parser.title

	for link in parser.links:
		if link not in siteMap.keys():
			print(link)
			try:
				recurse(link)
			except:
				pass
			
recurse('https://www.nscds.org')
print(siteMap)