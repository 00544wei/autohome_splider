# __*__ coding: utf-8 __*__

from scrapy import cmdline

cmdline.execute('scrapy crawl autohome_splider -o autohome.json'.split())