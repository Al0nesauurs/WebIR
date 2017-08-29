import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from craig.items import CraigItem

class MySpider(CrawlSpider):
    name = "craig"
    allowed_domains = [        
        "ku.ac.th",


        ]
    # The URLs to start with
    start_urls = [
        "http://lib.ku.ac.th/web/",
        ]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    # Method for parsing items
    def parse_items(self, response):
        f = open('HTML', 'a')
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = CraigItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                f.write(link.url + ' \n')
                #item['count'] = c
                items.append(item)
        f.close()
        # Return all the found items
        return items