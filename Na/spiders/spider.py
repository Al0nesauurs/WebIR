import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from Na.items import NaItem

class MySpider(CrawlSpider):
    name = "SpiderNa"
    allowed_domains = [        
        "ku.ac.th",


        ]
    # The URLs to start with
    start_urls = [
        "https://ocs.ku.ac.th"
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
    current_url = ''
    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
            yield scrapy.Request(url+"robots.txt", callback=self.parse2)
    def parse2(self, response):
        if response.status == 200:
            items = []
            self.logger.info("Visited %s", response.url)
            item = NaItem()
            item['url'] = response.url
            item['html'] = response.body
            items.append(item)
            return items
    # Method for parsing items
    def parse3(self):
        yield scrapy.Request(self.current_url+"robots.txt", callback=self.parse2)

    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = True
            chkrob = link.url.split("//")[-1].split("/")
            self.current_url =chkrob[0]
            self.parse3()
            chkrob = ''
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = NaItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                item['url'] = response.url
                item['html'] = response.body
                #item['count'] = c
                items.append(item)
        # Return all the found items
        return items