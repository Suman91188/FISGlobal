import json
import urllib.request


class Test_api_test:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

    def test_api_001(self):
        # 1.	Send the GET request  and storing response
        req = urllib.request.Request(self.url, headers=self.hdr)
        readdata = urllib.request.urlopen(req)
        json_data = readdata.read()
        data = json.loads(json_data)

        # printing response in console
        print(data['bpi'])

        # 2.	Verify the response contains
        # a.	There are 3 BPIs
        # i.	USD
        # ii.	GBP
        # iii.	EUR
        assert ['USD', 'GBP', 'EUR'] == list(data['bpi'].keys())
        assert len(data['bpi']) == 3

        # b.	The GBP ‘description’ equals ‘British Pound Sterling’.
        assert data['bpi']['GBP']['description'] == 'British Pound Sterling'

