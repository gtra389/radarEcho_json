
# coding: utf-8

# In[4]:


import requests
import json
import os 


# In[15]:


CWB_URL  = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/"
DATA_ID  = "O-A0059-001"   # 雷達整合回波資料
# DATA_ID  = "O-A0002-001" # 自動雨量站-雨量觀測資料
FOMAT    = "JSON"
AUTH_KEY = "CWB-F5271F70-2019-4E04-B488-555603C41B5A"
pnt_url = CWB_URL + '{}?Authorization={}&format={}'.format(DATA_ID, AUTH_KEY, FOMAT)

r = requests.get(pnt_url)
if r.status_code != 200:
    print('r.status_code: {}'.format(r.status_code))
else:
    print("Successfully loading.")
data = r.json()   

radarTime = data['cwbopendata']['dataset']['datasetInfo']['parameterSet']['parameter'][2]['parameterValue'][0:17]
radarTime = radarTime.replace(":", "")

save_fid = "radar_{}.txt".format(radarTime)
fidList = os.listdir()

if save_fid not in fidList:
    with io.open(save_fid, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, sort_keys = False, indent=4)
        
    statinfo = os.stat(save_fid)
    fidSize  = statinfo.st_size/1000 # Unit in KB
    
    if fidSize < 10:
        os.remove(save_fid)    
else:
    print("The file is exist.")

