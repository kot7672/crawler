import json
import sqlite3


def is_internal(link):
    url = extract_link_from_link_object(link)
    if 'type' in link[url]:
        if link[url]['type'] == 'internal':
            return True
    return False


def is_html(link):
    url = extract_link_from_link_object(link)
    if '.' not in url[-5:-1] or url.endswith('.html'):
        return True
    return False


def extract_link_from_link_object(link_object):
    return list(link_object.keys())[0]


def load_links_from_json(filename):
    with open(filename) as f:
        lines = f.readlines()
        text = ''.join(lines)

        links = json.loads(text)

        links_to_download = []

        for link in links:
            if is_internal(link) and is_html(link):
                links_to_download.append(extract_link_from_link_object(link))
        return links_to_download


def load_links_from_db(db, gen=False):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links WHERE type = 'internal'")
    if not gen:
        return [x[0] for x in cursor]
    else:
        yield cursor.fetchone()[0]


if __name__ == "__main__":
