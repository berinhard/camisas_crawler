BOT_NAME = 'camiseteria'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['camiseteria.spiders']
NEWSPIDER_MODULE = 'camiseteria.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['camiseteria.pipelines.CamiseteriaPipeline']
