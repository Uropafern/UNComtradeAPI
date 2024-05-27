# UNComtradeAPI
This is UNComtrade Semiconductor Industry for NXPO used only.
## สิ่งที่ต้องทำก่อนรันโค้ด
- ติดตั้ง Python
  - Download https://www.python.org/downloads/
  - ตรวจสอบการติดตั้งใน Command prompt
  ```
  python --version
  ```
- ติดตั้ง pip (ถ้าไม่มี; pip เป็นเครื่องมือสำหรับการติดตั้งและจัดการแพ็คเกจใน Python)
  ```
  python -m ensurepip --upgrade
  ```
- ติดตั้ง Pandas ลงใน Command prompt
  ```
  pip install pandas
  ```
- ติดตั้ง UN Comtrade API Package (อ่านเต็มๆได้ที่:https://github.com/uncomtrade/comtradeapicall)
  - ที่มา:https://github.com/uncomtrade/comtradeapicall
```
pip install comtradeapicall
```
```
mydf = comtradeapicall.getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS', period='2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023',
                                    reporterCode=None, cmdCode='8534,8541,854110,854121,854129,854130,854140,854150,854160,854190,8542,854231,854232,854233,854239,854290,854141,854142,854143,854149,854151,854159', flowCode='M,X',
                                    partnerCode='0', partner2Code='0', customsCode='C00', motCode='0', format_output='JSON',
                                    aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
```
