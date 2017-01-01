# -*- coding: utf-8 -*-


from sitemap import SiteMapRoot, SiteMap
from datetime import datetime
from datetime import date
import os
from pytrends.request import TrendReq

def generate_sitemap():
    google_username = "yourgmail@gmail.com"
    google_password = "yourgmailpassword"
    path = ""
    # connect to Google
    pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
    sitemap = SiteMap()
    country_payload = {'date' : 'today', 'geo': 'US'}
    hottrends = pytrend.hottrends(country_payload)
    for key,value in hottrends.items():
         for item in value:
            sitemap.append("http://www.mydomain.com/search/" + item + "/home", datetime.now(), "daily", 0.9)
            sitemap.append("http://www.mydomain.com/search/" + item + "/web", datetime.now(), "daily", 0.9)
            sitemap.append("http://www.mydomain.com/search/" + item + "/images", datetime.now(), "daily", 0.9)
            sitemap.append("http://www.mydomain.com/search/" + item + "/videos", datetime.now(), "daily", 0.9)
            sitemap.append("http://www.mydomain.com/search/" + item + "/news", datetime.now(), "hourly", 0.9)
            sitemap.append("http://www.mydomain.com/search/" + item + "/articles", datetime.now(), "daily", 0.9)


    xml_string = sitemap.to_string
    sitemap_root = SiteMapRoot("http://www.mydomain.com", "/var/www/mydomain-sites/mydomain.com/angular/trends_sitemap.xml", True)
    today = datetime.today().strftime('%Y-%m-%d')
    filename = today +".xml.gz"
    sitemap_root.append(filename, xml_string)
    sitemap_root.save_xml()
    os.rename("/var/www/mydomain-sites/mydomain.com/trends-sitemap/"+filename , "/var/www/mydomain-sites/mydomain.com/angular/"+filename)





if __name__ == "__main__":
    generate_sitemap()




