import requests
import time 
from fake_useragent import UserAgent 
url = "https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_1382cecc-04d1-47e8-afd4-0c5ca4080329_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD"

session = requests.session()

headers= {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
'Accept-language':'en-US,en;q=0.9',

'Accept-Encoding':'gzip, deflate, br, zstd',
'connection':'keep-alive',
'Referer':'https://www.flipkart.com/'
}

proxy_auth ='c071936660f5aa2d7156:476cc9733201022f@gw.dataimpulse.com:823'
proxies = {
    'http':f'http://{proxy_auth}',
    'https': f'https://{proxy_auth}'
}

time.sleep(2)

r = session.get(url,proxies=proxies, headers=headers)
print(r.text)


with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)



    
