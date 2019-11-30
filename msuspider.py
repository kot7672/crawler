import uspider


class MSUSpider(uspider.USpider):
    name = "msuspider"
    allowed_domains = ["msu.ru"]
    download_delay = 1
    extract_text = "db"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls.insert(0, "https://msu.ru")
