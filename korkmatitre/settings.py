# Scrapy settings for korkmatitre project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'korkmatitre'

SPIDER_MODULES = ['korkmatitre.spiders']
NEWSPIDER_MODULE = 'korkmatitre.spiders'

LOG_LEVEL='INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'korkmatitre (+http://www.yourdomain.com)'
