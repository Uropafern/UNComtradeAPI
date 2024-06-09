# UNComtradeAPI
This is UNComtrade Semiconductor Industry for NXPO used only.
## 1. สิ่งที่ต้องมีก่อนรันโค้ด
- มี Subscription Keys
  - สมัครสมาชิกผ่านทางเว็บไซต์ UNComtrade ก่อน https://comtradeplus.un.org/
  - ทำการ Log-in
  - ขอ **UNComtrade free trial 15 วัน** เพื่อทำการดาวน์โหลดตาม[ลิงค์](https://comtradeplus.un.org/MyComtrade/TrialRequest)
  - หลังจากได้อีเมล์ตอบกลับจากทาง UNComtrade แล้ว ขอ **API Subscription Keys**  ([วิธีเต็มพร้อมรูป](https://uncomtrade.org/docs/api-subscription-keys/))
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
- ติดตั้ง pip (เป็นเครื่องมือสำหรับการติดตั้งและจัดการแพ็คเกจใน Python) [ที่มา](https://phoenixnap.com/kb/install-pip-windows)
  ```
  python -m ensurepip --upgrade
  ```
- ติดตั้ง Pandas ลงใน Command prompt
  ```
  pip install pandas
  ```
- ติดตั้ง urllib3
  ```
  pip install urllib3
  ```
- ติดตั้ง UN Comtrade API Package (ที่มา:https://github.com/uncomtrade/comtradeapicall)
  ```
  pip install comtradeapicall
  ```
## 2. ทำความเข้าใจโค้ดเรียกAPI และปรับปรุงโค้ด
  - ในโค้ดที่ให้ไปจะมีช่องให้กรอก subscription_key ซึ่งต้องไป copy Primary key ใน https://comtradedeveloper.un.org/profile มาวางทับใน ช่องให้กรอก subscription_key แทน
    ```
    subscription_key = '<YOUR KEY>'
    ```
   **Example:**
   
    ```
    subscription_key = 'abcsdffhhjgj(Primary key ที่copyมา)'
    ```
 - ต่อมากล่องโค้ดด้านล่างคือการเรียกตัว API มา ในกรณีที่อยากแก้ไขเพิ่ม อย่างเช่น มีการอัปเดตปี 2024, 2025, 2026, ... ถ้าต้องการปี 2013-2026 ให้เพิ่มปีหลัง period โดย**ห้าม**มีช่อง spacebar เว้นเด็ดขาด
  ```
  mydf = comtradeapicall.getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS', period='2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023',
                                      reporterCode=None, cmdCode='8534,8541,854110,854121,854129,854130,854140,854150,854160,854190,8542,854231,854232,854233,854239,854290,854141,854142,854143,854149,854151,854159', flowCode='M,X',
                                      partnerCode='0', partner2Code='0', customsCode='C00', motCode='0', format_output='JSON',
                                      aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
  ```
  **Result:**
  ```
  mydf = comtradeapicall.getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS', period='2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026',
                                      reporterCode=None, cmdCode='8534,8541,854110,854121,854129,854130,854140,854150,854160,854190,8542,854231,854232,854233,854239,854290,854141,854142,854143,854149,854151,854159', flowCode='M,X',
                                      partnerCode='0', partner2Code='0', customsCode='C00', motCode='0', format_output='JSON',
                                      aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
  ```
  **Selection Criteria** เป็นเงื่อนไขในการqueryพร้อมคำอธิบาย [UNComtrade Database](https://comtradeplus.un.org/TradeFlow?Frequency=A&Flows=X&CommodityCodes=TOTAL&Partners=0&Reporters=all&period=2023&AggregateBy=none&BreakdownMode=plus)
   - typeCode(str) : Product type. Goods (C) or Services (S) -> **'C'**
   - freqCode(str) : The time interval at which observations occur. Annual (A) or Monthly (M) ; ดูเป็นรายปี -> **'A'**
   - clCode(str) : Indicates the product classification used and which version (HS, SITC) ; ใช้ HS Code ในการจำแนก -> **'HS'**
   - period(str) : Combination of year and month (for monthly), year for (annual) ; เลือกปีที่สนใจถ้าเอาปีเดียวก็ใส่ปีเดียวถ้าเอาหลายปีก็ใส่เลขทุกปีมีลูกน้ำคั่น**ห้าม**มีช่อง spacebarเว้น
   - reporterCode(str) : The country or geographic area to which the measured statistical phenomenon relates ; เนื่องจากต้องการ**ทุก**ประเทศจึงใช้ **None**
   - cmdCode(str) : Product code in conjunction with classification code ; เป็นรหัส HS Code ซึ่งเลขที่ขึ้นต้นด้วย 8534, 8541, 8542 จะเป็นรหัสที่มีความเกี่ยวข้องกับสารกึ่งตัวนำ
   - flowCode(str) : Trade flow or sub-flow (exports, re-exports, imports, re-imports, etc.) ; สนใจแค่ Import(รหัส M),Export(รหัส X) -> **'M,X'**
   - partnerCode(str) : The primary partner country or geographic area for the respective trade flow  ; เนื่องจากประเทศนึงก็จะมีคู่ค้าอันดับ 1 แต่เราสนใจ World ซึ่งเป็นภาพรวมจึงใช้รหัส **'0'**
   - partner2Code(str) : A secondary partner country or geographic area for the respective trade flow ; เนื่องจากประเทศนึงก็จะมีคู่ค้าอันดับ 2 แต่เราสนใจ World ซึ่งเป็นภาพรวมจึงใช้รหัส **'0'**
   - customsCode(str) : Customs or statistical procedure ; สนใจภาพรวม TOTAL จึงใช้รหัส **'C00'**
   - motCode(str) : The mode of transport used when goods enter or leave the economic territory of a country ; สนใจภาพรวม TOTAL จึงใช้รหัส **'0'**
## 3. หลังจากกดรัน Python เสร็จแล้ว
  - ได้ข้อมูลมา3ไฟล์ คือ 'UNTradeforVis.csv','GlobalUNTrade.csv', 'perbycountry.csv' และ'AnnualIncome60to65.csv' ให้แยกการนำเข้าข้อมูลใน PowerBI โดยนำข้อมูล 'UNTradeforVis.csv','GlobalUNTrade.csv' และ'perbycountry.csv' นำเข้าอีกไฟล์หนึ่ง และนำเข้าข้อมูล 'AnnualIncome60to65.csv'อีกไฟล์หนึ่ง แล้วทำการเพิ่ม New Column ในหน้า Table view โดยใช้ DAX ดังนี้
  - Table **perbycountry** สร้าง Column Percentage ของมูลค่านำเข้าหรือส่งออกประเทศนั้นเมื่อเทียบกับโลกตามรายปี
    ```
    Percentage = 
    VAR CurrentYear = 'perbycountry'[Year]
    VAR GlobalValue = 
        IF(
            'perbycountry'[FlowDesc] = "Import",
            CALCULATE(
                SELECTEDVALUE('GlobalUNTrade'[GlobalImport]),
                'GlobalUNTrade'[Year] = CurrentYear
            ),
            CALCULATE(
                SELECTEDVALUE('GlobalUNTrade'[GlobalExport]),
                'GlobalUNTrade'[Year] = CurrentYear
            )
        )
    RETURN
        DIVIDE('perbycountry'[Value], GlobalValue)
    ```
  - Table **UNTradeforVis** สร้าง Column Type และ TradeBalanceByType ตามลำดับ
    ```
    Type = SWITCH (
        TRUE (),
        LEFT('UNTradeforVis'[CmdCode], 4) = "8534", "Print Circuit Board",
        LEFT('UNTradeforVis'[CmdCode], 4) = "8541", "Diodes, transistors and similar semi-conductor devices",
        LEFT('UNTradeforVis'[CmdCode], 4) = "8542", "Integrated Circuit & Parts",
        BLANK ()
    )
    ```

    ```
    TradeBalanceByType = 
      VAR CurrentType = 'UNTradeforVis'[Type]
      VAR CurrentCountry = 'UNTradeforVis'[Country1]
      VAR CurrentYear = 'UNTradeforVis'[Year]
      VAR TotalExport = 
          CALCULATE(
              SUM('UNTradeforVis'[PrimaryValue]),
              'UNTradeforVis'[FlowDesc] = "Export",
              'UNTradeforVis'[Type] = CurrentType,
              'UNTradeforVis'[Country1] = CurrentCountry,
              'UNTradeforVis'[Year] = CurrentYear
          )
      VAR TotalImport = 
          CALCULATE(
              SUM('UNTradeforVis'[PrimaryValue]),
              'UNTradeforVis'[FlowDesc] = "Import",
              'UNTradeforVis'[Type] = CurrentType,
              'UNTradeforVis'[Country1] = CurrentCountry,
              'UNTradeforVis'[Year] = CurrentYear
          )
      RETURN
          TotalExport - TotalImport
    ```
- Table **AnnualIncome60to65** สร้าง Column IncomeCategory
  ```
  IncomeCategory = 
    IF (
        AnnualIncome60to65[รายได้] < 500000000,
        "< 500 million",
        IF (
            AnnualIncome60to65[รายได้] >= 500000000 && AnnualIncome60to65[รายได้] <= 1000000000,
            "500-1000 million",
            "> 1000 million")
      )
  ```
