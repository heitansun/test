import re
import requests

responses = requests.get('https://www.baidu.com')
print(responses.text)
