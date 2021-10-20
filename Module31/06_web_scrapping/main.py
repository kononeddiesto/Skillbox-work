import requests
import re


req_page = requests.get('http://www.columbia.edu/~fdc/sample.html')
full_text = req_page.text
title_pattern = r'<h3 .*?>(.*?)</h3>'
req_list = re.findall(title_pattern, full_text)
new_list = list(req_list)
print(new_list)
