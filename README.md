# 台北市Ubike各站點資訊
提供台北市Ubike各站點即時剩餘車輛數，還有分析一天的使用狀況，讓需要使用的人能夠知道什麼時候去是有車可以使用的。

## 取得資料
可以上台北市政府資料開放平台獲取開放資料  
https://data.taipei/index
這次是使用Ubike的服務  
https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz  
從這裡可以獲取當前各站點資訊及剩餘數量的JSON格式的文字檔，寫一個定時抓取的腳本就可以進行數據分析。
### 獲取各站點資訊
get_ubike_info.py  

![](https://i.imgur.com/uolxggm.png)

### 獲取各站點使用狀況

get_ubike_data.py![](https://i.imgur.com/zPysCF0.png)


## 數據可視化分析
獲取完可用數據後，終究還只是一堆數據，必須把他整理成人能看得懂的格式，可以根據自己的需求把數據分類，再用一些數據可視化的套件繪製成圖表。  
#### 這裡使用的套件是 chart.js  
付上官網 https://www.chartjs.org/

這是抓取的數據是今日的使用狀況來進行分析
就可以看出一天中哪個時段需要補車或是哪個時段去有車輛可以使用。  
![](https://i.imgur.com/Fn4h8V4.png)
