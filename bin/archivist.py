from lxml.etree import parse
import time

doc = parse("/Users/ianbicking/Downloads/ianbickingablog.wordpress.2013-03-29 (1).xml")
channel = doc.getroot()[0]
items = channel.findall("item")

for item in items:
    title = item.find("title").text.strip()
    link = item.find("link").text.strip()
    date = item.find("pubDate").text.strip().split("+")[0].strip()
    date = time.strptime(date, "%a, %d %b %Y %H:%M:%S")
    date = time.strftime("%B %Y", date)
    print ('<li><a href="%(link)s">%(title)s</a> (%(date)s)</li>'
           % dict(
            link=link, title=title, date=date))
