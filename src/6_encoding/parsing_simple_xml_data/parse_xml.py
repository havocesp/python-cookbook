from urllib.request import urlopen
import defusedxml.ElementTree

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = defusedxml.ElementTree.parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()
