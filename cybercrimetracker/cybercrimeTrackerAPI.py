"""
This is the (unofficial) Python API for cybercrime-tracker.net website.
Using this code, you can retrieve infected domains, panels and so on.
"""

from bs4 import BeautifulSoup
import requests
import re

class cybercrimeTrackerAPI(object):
    """cybercrimeTracker main handler."""

    def dump(self, query):
        index = 0
        req = requests.get('http://cybercrime-tracker.net/index.php?search={}'.format(query))
        max_offset = max(map(int, re.findall(r's=([0-9]+)', req.content.decode('utf-8'))))
        # max_offset = max(list_res, key=len)
        res = []
        while index < max_offset:
            tmp_results = self.search(query, index)
            for entry in tmp_results:
                if entry not in res:
                    res.append(entry)
            index = index + 40
        tmp_results = self.search(query, max_offset)
        for entry in tmp_results:
            if entry not in res:
                res.append(entry)
        return res

    def search(self, query, offset=0, limit=40):
        """
        Search cybercrime-tracker.net for specific information about panels.

        query -- query to search for
        Return a list of objects, like so:

        {
            "url": "mike.rivalserver.com/~wqpjevcp/a/",
            "ip": "191.101.245.101",
            "vt_latest_scan": "https://www.virustotal.com/latest-scan/http://mike.rivalserver.com/~wqpjevcp/a/",
            "vt_ip": "https://www.virustotal.com/en/ip-address/191.101.245.101/information/",
            "date": "12-12-2017",
            "type": "AZORult"
        }
        """
        results = []

        base_url = "http://cybercrime-tracker.net/index.php?search={}&s={}&m={}".format(query, offset, limit)
        # base_url += domain
        # print(base_url)

        ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        r = requests.get(url=base_url, headers={'User-Agent': ua})

        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            try:
                table = soup.findAll('table', attrs={'class': 'ExploitTable'})[0]
                rows = table.find_all(['tr'])[1:]
                for row in rows:
                    cells = row.find_all('td', limit=5)
                    if cells:
                        tmp = {
                            'date': cells[0].text,
                            'url': cells[1].text,
                            'ip': cells[2].text,
                            'type': cells[3].text,
                            'vt_latest_scan': 'https://www.virustotal.com/latest-scan/http://{}'.format(cells[1].text)
                        }
                        if tmp['ip'] != '':
                            tmp['vt_ip'] = 'https://www.virustotal.com/en/ip-address/{}/information/'.format(tmp['ip'])
                        if tmp not in results:
                            results.append(tmp)
            except Exception as e:
                print(e)
                print("Error retrieving information.")

        return results
