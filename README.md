# Sitemap Trends

=======

#### Generate a sitemap with top today Trends get from google trends

Get top today Trends with [PyThrends](https://github.com/zhilevan/pytrends) and generate sitemap according to  today Trends.

**Installation**
First you need install pythrends 

`pip install pytrends`

Then Clone  trends-sitemap repo

```
git clone https://github.com/zhilevan/trends-sitemap.git
cd trends-sitemap
python generate-trends-sitemap.py
```

##### Setup Daily generation

In order to Generate Trends Sitemap Create a cron and set up it daily,
with this method a news sitemap will be created and add to  root ( index) site map.

```
‍‍‍$ crontab -e
```
Then create a cron run everyday on 22:00


```
0 22 * * * python PATH_OF_DIRECTORY/generate-trends-sitemap.py

```

