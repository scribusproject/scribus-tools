# This script will check http://services.scribus.net for broken assets 
import lxml.html


url = "http://services.scribus.net"
doc = lxml.html.parse(url)
# pattern matching for relative urls: <a href="scribus_fonts.xml">
content_parsed  = doc.xpath('href')
# also ignore scribusversions.xml

# Create a scraper class to feed .xml page results to 

# Create a function that mails an admin when a result 404s

