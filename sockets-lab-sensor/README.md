# 預先設定
## 環境檢查
1. 確認電腦已安裝Mbed Studio、Python 3
## STM32
1. 在Mbed Studio使用mbed-os-example-sockets新增一個Program，並可自訂名稱
2. 將所使用之STM32開發板的Driver新增至此Program的Library
3. 下載網頁上的main.cpp，並替代此Program的main.cpp(檔案位於此Program的source資料夾)
4. 修改此Program的mbed_app.json以設定STM32開發板的Wi-Fi連線功能
5. 修改此Program的targets.jsons(檔案位於此Program的mbed-os資料夾)內的printf_lib將其值修改為std("printf_lib": "std")
6. 使用Build Program將程式載入至STM32開發板
## Server
1. 確認Python已安裝所需的套件(請參考Socket Lab Test Server.py所使用的套件)
2. 確認電腦之防火牆可讓Python接收資料

# 開始使用
1. 使用Python執行Socket Lab Test Server.py以開啟Server
2. 在Mbed Studio內執行Run Program
3. 確認STM32開發板是否成功傳送資料並確認Server是否成功接收資料
