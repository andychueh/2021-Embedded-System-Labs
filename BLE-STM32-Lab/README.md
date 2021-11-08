# 預先設定
## 環境檢查
1. 確認電腦已安裝Mbed Studio
## STM32
1. 在Mbed Studio使用mbed-os-example-ble-Button新增一個Program，並可自訂名稱
2. 下載網頁上STM32資料夾內的所有檔案並放置於此Program的source資料夾(可清除source資料夾的原始檔案)
3. 刪除此Program的TARGET_CORDIO_BLUENRG資料夾以避免發生錯誤
4. 使用Build Program將程式載入至STM32開發板
## Raspberry Pi
### 請在Terminal執行以下指令以安裝所需套件
1. sudo apt install python-pip
2. sudo apt install libglib2.0-dev
3. sudo pip install bluepy
### 請在Terminal執行以下指令以執行主程式
#### 請先確認Terminal所在目錄是否與BLE_New.py所在目錄相同
#### 請先確認BLE_New.py的所連線之裝置位址是否與STM32之裝置位址相同
1. sudo python3 BLE_New.py
# 開始使用
1. 請依照Raspberry Pi畫面顯示內容進行相關操作
2. 透過按下STM32的按鈕以觀察Raspberry Pi顯示之資訊所發生的改變

# 參考
1. https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Button/
2. https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/
