# -*- coding: utf-8 -*-
# 新北市人口數爬取

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#  新北市政府民政局>>人口統計網站
url = 'https://www.ca.ntpc.gov.tw/home.jsp?id=88f142fb0f4a0762'

# 使用Chrome開啟網頁
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

# 設定選單：1.年分 2.月分
select1 = Select(driver.find_element(By.XPATH,'//*[@id="yyyy"]'))
select2 = Select(driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div[3]/form/div/div[1]/div[2]/select'))


# 抓取93-110年新北市的總人口數
people=[] 
for y in range(93,111):
    select1.select_by_value(str(y))           #年份選單        
    select2.select_by_value('12')             #月份選單
    driver.find_element(By.ID,'send').click() #點擊「查詢」
    p = driver.find_element(By.XPATH,'//*[@id="table"]/tbody/tr[30]/td[7]')
    people.append(p.text)  #擷取的資料放進people 
    driver.back()          #網址變動，必須返回上一頁才能繼續執行

# 關閉Chrome 
sleep(3)
driver.quit()

#%%

import pandas as pd

# 年分
year = []
for i in range(93,111):
    year.append(i)

# 將年分、人口數轉置為DataFrame
ntpc_people = pd.DataFrame({'year':year,'population':people})
print(ntpc_people)

# 匯出成csv檔
ntpc_people.to_csv('新北市人口數.csv',index=False) #不新增索引欄
