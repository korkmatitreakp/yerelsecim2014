from scrapy.spider import Spider
from scrapy.selector import Selector
from korkmatitre.items import OyItem
import unicodedata

urls = []
ankara_start = 205407
ankara_end = 217637

party_ids = {"dsp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl00$tbPartiOy_1_1",
            "dyp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl01$tbPartiOy_1_1",
            "turkp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl02$tbPartiOy_1_1",
            "hkp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl03$tbPartiOy_1_1",
            "bbp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl04$tbPartiOy_1_1",
            "akp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl05$tbPartiOy_1_1",
            "yp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl06$tbPartiOy_1_1",
            "dp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl07$tbPartiOy_1_1",
            "mp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl08$tbPartiOy_1_1",
            "sp":"TabContainer$TabPanel1$rptPartiler_1_1$ctl09$tbPartiOy_1_1",
            "hop":"TabContainer$TabPanel1$rptPartiler_1_2$ctl00$tbPartiOy_1_2",
            "ldp":"TabContainer$TabPanel1$rptPartiler_1_2$ctl01$tbPartiOy_1_2",
            "btp":"TabContainer$TabPanel1$rptPartiler_1_2$ctl02$tbPartiOy_1_2",
            "hdp":"TabContainer$TabPanel1$rptPartiler_1_2$ctl03$tbPartiOy_1_2",
            "chp":"TabContainer$TabPanel1$rptPartiler_1_2$ctl04$tbPartiOy_1_2",
            "hep":"TabContainer$TabPanel1$rptPartiler_1_2$ctl05$tbPartiOy_1_2",
            "mhp":"TabContainer$TabPanel1$rptPartiler_1_2$ctl06$tbPartiOy_1_2",}
for i in xrange(ankara_start, ankara_end):
	urls.append("http://sts.chp.org.tr/SonucDetay.aspx?sid=%i" % i)

def cleanUnicode(txt):
	return unicodedata.normalize('NFKD', txt).encode('ascii','ignore').strip()
	
def getVoteCounts(sel, party_name):
    xpath = "//input[@name='" + party_ids.get(party_name) + "']/@value"
    value = sel.xpath(xpath).extract()
    if len(value) == 0:
    	return 0
    else:
    	return int(cleanUnicode(value[0]))
    	
def getFieldValue(sel, name):
    xpath = "//input[@name='" + name + "']/@value"
    value = sel.xpath(xpath).extract()
    if len(value) == 0:
    	return 0
    else:
    	return int(cleanUnicode(value[0]))
    
class OySpider(Spider):
    name = "oy"
    allowed_domains = ["sts.chp.org.tr/"]
    start_urls = urls

    def parse(self, response):
    	sel = Selector(response)
    	il_ilce_sandik = sel.xpath('//span[@id="TabContainer_TabPanel1_lblOzetIlIlce1"]/text()').extract()[0]
    	il, ilce, sandik = [cleanUnicode(x) for x in il_ilce_sandik.split("/")]
    	alan = cleanUnicode(sel.xpath('//span[@id="TabContainer_TabPanel1_lblOzetSandikAlani1"]/text()').extract()[0])
    	dsp_oy = getVoteCounts(sel, "dsp")
    	dyp_oy = getVoteCounts(sel, "dyp")
    	turkp_oy = getVoteCounts(sel, "turkp")
    	hkp_oy = getVoteCounts(sel, "hkp")
    	bbp_oy = getVoteCounts(sel, "bbp")
    	akp_oy = getVoteCounts(sel, "akp")
    	yp_oy = getVoteCounts(sel, "yp")
    	dp_oy = getVoteCounts(sel, "dp")
    	mp_oy = getVoteCounts(sel, "mp")
    	sp_oy = getVoteCounts(sel, "sp")
    	hop_oy = getVoteCounts(sel, "hop")
    	ldp_oy = getVoteCounts(sel, "ldp")
    	btp_oy = getVoteCounts(sel, "btp")
    	hdp_oy = getVoteCounts(sel, "hdp")
    	chp_oy = getVoteCounts(sel, "chp")
    	hep_oy = getVoteCounts(sel, "hep")
    	mhp_oy = getVoteCounts(sel, "mhp")
    	
    	
    	timestamp=cleanUnicode(sel.xpath('//span[@id="TabContainer_TabPanel1_lblData1"]/text()').extract()[0])
    	timestamp_split = timestamp.split(" ")

    	date_value = timestamp_split[0]
    	time_value = timestamp_split[2]

    	kayitli_secmen = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetKayitliSecmenSayisi1")
        oy_kullanan_kayitli_secmen = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetOyKullananKayitliSecmenSayisi1")
        kanun_geregi_oy_kullanan = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetKanunGeregiOyKullananSayisi1")
        kullanilan_toplam_oy = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetKullanilanToplamOy1")
        itirazsiz_gecerli_oy = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetItirazsizGecerliOySayisi1")
        itirazli_gecerli_oy = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetItirazliGecerliOySayisi1")
        gecerli_oy = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetGecerliOySayisi1")
        gecersiz_oy = getFieldValue(sel, "TabContainer$TabPanel1$tbOzetGecersizOySayisi1")
    	
    	yield OyItem(il=il,
    	ilce=ilce,
    	sandik=sandik,
    	alan=alan,
    	dsp_oy=dsp_oy,
    	dyp_oy=dyp_oy,
    	turkp_oy=turkp_oy,
    	hkp_oy=hkp_oy,
    	bbp_oy=bbp_oy,
    	akp_oy=akp_oy,
    	yp_oy=yp_oy,
    	dp_oy=dp_oy,
    	mp_oy=mp_oy,
    	sp_oy=sp_oy,
    	hop_oy=hop_oy,
    	ldp_oy=ldp_oy,
    	btp_oy=btp_oy,
    	hdp_oy=hdp_oy,
    	chp_oy=chp_oy,
    	hep_oy=hep_oy,
    	mhp_oy=mhp_oy,
    	date_value=date_value,
    	time_value=time_value,
    	kayitli_secmen=kayitli_secmen,
    	oy_kullanan_kayitli_secmen=oy_kullanan_kayitli_secmen,
    	kanun_geregi_oy_kullanan=kanun_geregi_oy_kullanan,
    	kullanilan_toplam_oy=kullanilan_toplam_oy,
    	itirazsiz_gecerli_oy=itirazsiz_gecerli_oy,
    	itirazli_gecerli_oy=itirazli_gecerli_oy,
    	gecerli_oy=gecerli_oy,
    	gecersiz_oy=gecersiz_oy,
        url=response.url
    	)
    	
    	
    	
    	
    	# filename = response.url.split("sid=")[1] + ".html"
		# open(filename, 'wb').write(response.body)
		
