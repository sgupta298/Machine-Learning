import selenium
import matplotlib.pyplot as pl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
wd =webdriver.Chrome()
users=['sgupta298','subhamskm','Parnidadu']
lastupdated=[]
for name in users :
    wd.get('http://www.github.com/'+name+'?tab=repositories')
    last=wd.find_element_by_tag_name('relative-time').text
    data = last.split()
    if "a day" in data:
        lastupdated.append(24)
    elif "days" in data:
        lastupdated.append(int(data[0])*24)
    elif "minute" in data:
        lastupdated.append(int(data[0])/60)
    elif "minutes" in data:
        lastupdated.append(int(data[0])/60)
    elif "seconds" in data:
        lastupdated.append(int(data[0])/3600)
    elif "second" in data:
        lastupdated.append(1/3600)
    elif "hour" in data :
        lastupdated.append(1)
    else:
        lastupdated.append(int(data[0]))
print(lastupdated)
pl.bar(users,lastupdated)
pl.xlabel("Users --->")
pl.ylabel("Last updated time in hours ----->")
pl.grid(color = 'grey')
pl.show()