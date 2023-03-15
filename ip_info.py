import requests

"""
The API base path is http://ip-api.com/json/{query}
{query} can be a single IPv4/IPv6 address or a domain name.
If you don't supply a query the current IP address will be used
"""

def get_ip_info(ip_address=''):
    url = "http://ip-api.com/json/" + ip_address
    params = {'fields' : 'status,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,proxy,query'}
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.9',
        'Cache-Control' : 'no-cache',
        'Dnt' : '1',
        'Upgrade-Insecure-Requests' : '1',
        'Pragma' : 'no-cache',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        'Referer' : 'https://ip-api.com/',
        "User-Agent" : "Mozilla/5.0"
    }
    page = requests.get(url, headers=headers, params=params)
    response = page.json()
    print(f"{'Fields':25} | {'Values'}")
    print("-"*50)
    for key,value in response.items():
        if value:
            print(f"[+] {key:21} | {value}")
        else:
            print(f"[-] {key:21} | {'N/A'}")
