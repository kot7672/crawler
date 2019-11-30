from download_spider import DownloadSpider


class MSUDownloadSpider(DownloadSpider):
    name = "msuspider"
    extract_text = "db"
    file = "msuresult.json"
    download_delay = 1
