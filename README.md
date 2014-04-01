yerelsecim2014
==============

Kaynak kodu kendiniz kullanmak isterseniz asagidakileri yapabilirsiniz.
```bash
sudo easy_install scrapy
git clone https://github.com/korkmatitreakp/yerelsecim2014.git
cd yerelsecim2014
scrapy crawl oy -o items.csv -t csv
```

Sonuclari json formatinda gormek istiyorsaniz son satirda sunu yazin:
```bash
scrapy crawl oy -o items.json -t json
```
