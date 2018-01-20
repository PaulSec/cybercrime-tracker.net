Cybercrime-Tracker Python utility
========


This project aims at helping you to interact with [cybercrime-tracker.net](http://cybercrime-tracker.net) website. 

Git clone the repo. 

```bash
git clone https://github.com/PaulSec/cybercrime-tracker.net
```

Install the dependencies.

```bash
pip install -r requirements.txt
```


### Install with pip (from the Github repository): 

```shell
➜  ~ pip install https://github.com/PaulSec/cybercrime-tracker.net/archive/master.zip --user
Collecting https://github.com/PaulSec/cybercrime-tracker.net/archive/master.zip
  Downloading https://github.com/PaulSec/cybercrime-tracker.net/archive/master.zip
Installing collected packages: cybercrimetracker
  Running setup.py install for cybercrimetracker ... done
Successfully installed cybercrimetracker-0.1
```

### Install with pip (from Pypi repository)


```shell
➜  ~ pip install cybercrimetracker --user
Collecting cybercrimetracker
  Using cached cybercrimetracker-0.1.tar.gz
Installing collected packages: cybercrimetracker
  Running setup.py install for cybercrimetracker ... done
Successfully installed cybercrimetracker-0.1
```



Then, you can start interacting with cybercrime-tracker this way: 

```python
from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
import sys
import json

query = ''
if len(sys.argv) > 1:
   query = sys.argv[1]
print(json.dumps(cybercrimeTrackerAPI().search(query), indent=2))
```

The result is an array of dictionary items which looks like this: 

```json 
[
  {
      "url": "mike.rivalserver.com/~wqpjevcp/a/",
      "ip": "191.101.245.101",
      "vt_latest_scan": "https://www.virustotal.com/latest-scan/http://mike.rivalserver.com/~wqpjevcp/a/",
      "vt_ip": "https://www.virustotal.com/en/ip-address/191.101.245.101/information/",
      "date": "12-12-2017",
      "type": "AZORult"
  },
  ....
]
```

License
========

Released under MIT License.