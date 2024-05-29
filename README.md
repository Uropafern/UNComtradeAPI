# UNComtradeAPI
This is UNComtrade Semiconductor Industry for NXPO used only.
## สิ่งที่ต้องมีก่อนรันโค้ด
- มี Subscription Keys
  - สมัครสมาชิกผ่านทางเว็บไซต์ UNComtrade ก่อน https://comtradeplus.un.org/
  - ทำการ Log-in
  - ขอ **UNComtrade free trial 15 วัน** เพื่อทำการดาวน์โหลดตามลิงค์นี้ https://comtradeplus.un.org/MyComtrade/TrialRequest
  - หลังจากได้อีเมล์ตอบกลับจากทาง UNComtrade แล้ว ขอ **API Subscription Keys**  (วิธีเต็มพร้อมรูป: https://uncomtrade.org/docs/api-subscription-keys/)
    1. ไปที่ลิ้งค์ https://comtradedeveloper.un.org แล้ว Log-in อีเมล์ตามที่สมัครสมาชิกไว้
    2. ไปที่ https://comtradedeveloper.un.org/products เลือก Premium Trial APIs
    3. ตรงหัวข้อ Your subscriptions จะมีช่องให้กรอกข้อมูล ให้ทำการตั้งชื่ออะไรก็ได้แล้วกด Subscribe
    4. รอประมาณครึ่งวันแล้วมาที่ลิงค์ https://comtradedeveloper.un.org/profile จะพบว่ามี Primary key อยู่ให้ทำการกด show ก็จะแสดง Subscription Keys ให้สามารถนำไปใช้ตอนรันโค้ด
- ติดตั้ง Python
  - Download https://www.python.org/downloads/
  - ตรวจสอบการติดตั้งใน Command prompt
  ```
  python --version
  ```
- ติดตั้ง pip (เป็นเครื่องมือสำหรับการติดตั้งและจัดการแพ็คเกจใน Python)
  ```
  python -m ensurepip --upgrade
  ```
- ติดตั้ง Pandas ลงใน Command prompt
  ```
  pip install pandas
  ```
- ติดตั้ง UN Comtrade API Package (ที่มา:https://github.com/uncomtrade/comtradeapicall)
  ```
  pip install comtradeapicall
  ```
## ทำความเข้าใจโค้ดเรียกAPI
  - ในโค้ดที่ให้จะมีช่องให้กรอก subscription_key = '<YOUR KEY>'ซึ่งให้ไป copy Primary key ใน https://comtradedeveloper.un.org/profile มาวางทับใน <YOUR KEY> แทน
  ```
  mydf = comtradeapicall.getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS', period='2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023',
                                      reporterCode=None, cmdCode='8534,8541,854110,854121,854129,854130,854140,854150,854160,854190,8542,854231,854232,854233,854239,854290,854141,854142,854143,854149,854151,854159', flowCode='M,X',
                                      partnerCode='0', partner2Code='0', customsCode='C00', motCode='0', format_output='JSON',
                                      aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
  ```
  **Selection Criteria** [ที่มา](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=X&CommodityCodes=TOTAL&Partners=0&Reporters=all&period=2023&AggregateBy=none&BreakdownMode=plus)
    typeCode(str) : Product type. Goods (C) or Services (S)
    freqCode(str) : The time interval at which observations occur. Annual (A) or Monthly (M)
    clCode(str) : Indicates the product classification used and which version (HS, SITC)
    period(str) : Combination of year and month (for monthly), year for (annual)
    reporterCode(str) : The country or geographic area to which the measured statistical phenomenon relates
    cmdCode(str) : Product code in conjunction with classification code
    flowCode(str) : Trade flow or sub-flow (exports, re-exports, imports, re-imports, etc.)
    partnerCode(str) : The primary partner country or geographic area for the respective trade flow
    partner2Code(str) : A secondary partner country or geographic area for the respective trade flow
    customsCode(str) : Customs or statistical procedure
    motCode(str) : The mode of transport used when goods enter or leave the economic territory of a country
