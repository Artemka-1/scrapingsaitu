import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.quotes_file = open('quotes.json', 'w', encoding='utf-8')
        self.authors_file = open('authors.json', 'w', encoding='utf-8')
        self.authors_seen = set()
        self.quotes = []
        self.authors = []

    def close_spider(self, spider):
        json.dump(self.quotes, self.quotes_file, ensure_ascii=False, indent=4)
        json.dump(self.authors, self.authors_file, ensure_ascii=False, indent=4)
        self.quotes_file.close()
        self.authors_file.close()

    def process_item(self, item, spider):
        if isinstance(item, dict) or 'text' in item:  # QuoteItem
            self.quotes.append(dict(item))
        elif isinstance(item, dict) or 'name' in item:  # AuthorItem
            if item['name'] not in self.authors_seen:
                self.authors_seen.add(item['name'])
                self.authors.append(dict(item))
        return item
