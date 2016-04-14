目前104公司資料: 1361 筆 (329全)
目前新資資料 : 49710 筆 (三家新資網)
比對結果 : 1361*49710 = 67655310
impact >= 0.5 : 4615645 筆   ( impact = sum([1 0 0 1])/ len([1 0 0 1]) )

======================================
使用到的四個 py檔:
clean_companyName-v2.ipynb 
    output 104_company.txt, sal_company.txt, 裡面存放清理過後104公司名稱和新資網的公司名稱, 符號括號等等都被拿掉
CuttingOff.py
    用jieba把被比較的新資公司名稱切詞, 以空格分隔, 存在 cutting_company.txt
Match2-v2.py
    讀取cutting_company.txt, 用正規表示式比對104正確公司名稱，存成 [1 0 1 0] 的變數寫在 match_bool.txt
impact.py
    用比對過後的[0 1 1 0] 計算impact, 超過自行給訂impact_threshold, 即會印出 [ 104公司名稱 薪資網資料 ] 寫在 match.txt
    