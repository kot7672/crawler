from uspider import USpider
from downloader import load_links_from_json
from text_extractor import extract
from sqlite3 import connect


class DownloadSpider(USpider):
    file = None
    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls.extend(load_links_from_json(self.file))

    def parse(self, response):
        text = extract(response.body)
        if self.extract_text == "db":
            conn = connect(f"{self.name}.db")
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT OR REPLACE INTO texts (url, extracted_text) 
            VALUES ('{response.url}', '{text.replace("'", '"')}')
            """)
            self.conn.commit()
        yield {response.url: text}
