import simplejson as json

class CamiseteriaPipeline(object):

    def __init__(self):
        self.dict_items = []

    def process_item(self, item, spider):
        self.dict_items.append(dict(item))
        return item

    def close_spider(self, spider):
        json_content = json.dumps(self.dict_items)
        with open('output.json', 'w') as fp:
            fp.write(json_content)
