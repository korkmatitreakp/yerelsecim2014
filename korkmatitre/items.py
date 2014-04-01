# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class OyItem(Item):
    # define the fields for your item here like:
    il = Field()
    ilce = Field()
    sandik = Field()
    alan = Field()
    date_value = Field()
    time_value = Field()
    kayitli_secmen = Field()
    oy_kullanan_kayitli_secmen = Field()
    kanun_geregi_oy_kullanan = Field()
    kullanilan_toplam_oy = Field()
    itirazsiz_gecerli_oy = Field()
    itirazli_gecerli_oy = Field()
    gecerli_oy = Field()
    gecersiz_oy = Field()
    dsp_oy = Field()
    dyp_oy = Field()
    turkp_oy = Field()
    hkp_oy = Field()
    bbp_oy = Field()
    akp_oy = Field()
    yp_oy = Field()
    dp_oy = Field()
    mp_oy = Field()
    sp_oy = Field()
    hop_oy = Field()
    ldp_oy = Field()
    btp_oy = Field()
    hdp_oy = Field()
    chp_oy = Field()
    hep_oy = Field()
    mhp_oy = Field()
    url = Field()

