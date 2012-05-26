BOT_NAME = 'camisas'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['camisas.spiders']
NEWSPIDER_MODULE = 'camisas.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['camisas.pipelines.CamisasPipeline']
