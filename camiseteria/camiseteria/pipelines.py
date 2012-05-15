import os
import simplejson as json

from .dbconn import DropboxConnection

class CamiseteriaPipeline(object):

    def __init__(self):
        self.dict_items = []

    def process_item(self, item, spider):
        self.dict_items.append(dict(item))
        return item

    def close_spider(self, spider):
        conn = self._get_dropbox_connection()

        json_content = json.dumps(self.dict_items)
        tmp_file = '/tmp/out.json'
        with open(tmp_file, 'w') as fp:
            fp.write(json_content)

        file_name = '%s.json' % spider.name
        conn.upload_file(tmp_file, '/Public/', file_name)

    def _get_dropbox_connection(self):
        db_user = 'bernardo@yourjetpack.com.br'
        db_pass = os.environ.get('DROPBOX_PASSWD')
        return DropboxConnection(db_user, db_pass)
