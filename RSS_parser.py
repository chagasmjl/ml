import feedparser
https://pythonhosted.org/feedparser/
python_wiki_rss_url = "https://spectrum.ieee.org/rss/robotics/fulltext/"

feed = feedparser.parse( python_wiki_rss_url )
print(feed[ "channel" ][ "description" ])
for item in feed["items"]:

    print("--> " , item["title"], item["published"], item[ "link" ] )
    print(" *** " , item["summary"])
    print(item["content"])
    print("*******************************************************")