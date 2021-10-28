# 環境設定
1. 確認Raspberry Pi與行動裝置已進行藍牙配對
## 行動裝置
1. 確認行動裝置藍牙顯示名稱長度適中
2. 使用BLE Tool執行Advertise
3. 修改第一個characteristic value為想要的值
## Raspberry Pi
### 請在Terminal執行以下指令以安裝所需套件
1. sudo apt install python-pip
2. sudo apt install libglib2.0-dev
3. sudo pip install bluepy
### 請在Terminal執行以下指令以執行主程式
#### 請先確認Terminal所在目錄是否與BLE.py所在目錄相同
1. sudo python3 BLE.py
# 開始使用
1. 請依照Raspberry Pi畫面顯示內容進行相關操作
2. 觀察Raspberry Pi、行動裝置所顯示的資訊
