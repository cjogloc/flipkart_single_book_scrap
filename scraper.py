import scraperwiki           
import lxml.html           

url = "http://www.flipkart.com/fundamentals-digital-circuits-2-e-english-2nd/p/itmdx5gwz4xzmtbf?pid=9788120336797&sid=bks&query=9788120336797&q=9788120336797"
html = scraperwiki.scrape(url)
authors =''
root = lxml.html.fromstring(html)

for el in root.cssselect("div.nprod-specs div span"):
    if el.text == "Author:" :
        el = el.getparent()
        for authorel in el.cssselect("a"):
            authors += authorel.text + ", "

for el in root.cssselect("div.prices img"):
    if el.attrib['itemprop']=="price":
        mrprice=el.attrib['content']
        fkprice=el.attrib['content']

for tr in root.cssselect("div#productSpecs tr"):
    if tr.cssselect("td"):
        tds = tr.cssselect("td")
        if tds[0].text_content()=="Publisher":
            publisher = tds[1].text_content()
        elif tds[0].text_content()=="Publication Year":
            publication_year = tds[1].text_content()
        elif tds[0].text_content()=="ISBN-13":
            isbn_13 = tds[1].text_content()
        elif tds[0].text_content()=="ISBN-10":
            isbn_10 = tds[1].text_content()
        elif tds[0].text_content()=="Language":
            language = tds[1].text_content()
        elif tds[0].text_content()=="Edition":
            edition = tds[1].text_content()
        elif tds[0].text_content()=="Binding":
            binding = tds[1].text_content()
        elif tds[0].text_content()=="Number of Pages":
            no_of_pages = tds[1].text_content()
        elif tds[0].text_content()=="Book Type":
            book_type = tds[1].text_content()

    
for el in root.cssselect("div.imgWrapper img"):
    img_url = el.attrib['data-src']
    print img_url


data = {
            'url':url,
            'img_url':img_url,
          
            'mrp':mrprice,
            'fkprice':fkprice,
            'authors':authors,
            'publisher':publisher,
            'publication_year':publication_year,
            'isbn-13':isbn_13,
            'isbn-10':isbn_10,
            'language':language,
            'edition':edition,
            'binding':binding,
            'no_of_pages':no_of_pages,
            'book_type':book_type
       }
print data

scraperwiki.sqlite.save(['url'],data)
