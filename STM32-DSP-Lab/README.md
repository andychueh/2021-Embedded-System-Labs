# 預先設定
## 環境檢查
1. 確認電腦已安裝Mbed Studio
## STM32
1. 在Mbed Studio使用新增一個Empty Program，並可自訂名稱
2. 將參考連結Import至此Program的Library
3. 將網頁上的檔案放入或取代此Program的檔案
4. 修改此Program的targets.jsons內的printf_lib將其值修改為std("printf_lib": "std")
5. 使用Build Program將程式載入至STM32開發板
# 開始使用
1. 執行STM32的Program
2. 在Mbed Studio內將輸出結果儲存為檔案
3. 使用MATLAB及網頁上的數據分析用檔案進行數據分析
# 參考
1. https://os.mbed.com/teams/mbed-official/code/mbed-dsp
2. https://os.mbed.com/teams/ST/code/DISCO_L475VG_IOT01-Sensors-BSP/
