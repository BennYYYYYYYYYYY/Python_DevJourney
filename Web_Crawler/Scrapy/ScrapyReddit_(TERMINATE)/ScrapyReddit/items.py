# Item 是 Scrapy 中的核心數據容器，用來存放爬取的數據。
# 它的作用類似於 Python dict，但提供了更清晰的結構化數據表達。
# Item 中的每個字段(Field)都可以自定義格式或驗證規則，這樣可以確保數據的一致性，並減少在 Pipeline 中處理數據的難度。
# Scrapy 的 Item 是一個輕量級的模型層，它只定義結構，並不負責具體數據的操作或儲存。 
# Item 會檢查欄位名稱，如果剛剛沒有定義該欄位，則會出現錯誤


'''
Scrapy 的爬蟲會從網站上把資料撈下來，但為了讓數據「乾淨整齊」。
我們需要事先規劃一個模板，來定義「我要抓的資料有哪些欄位」。這個模板就是 Item。
'''

import scrapy


class RedditItem(scrapy.Item): # scrapy.Item 是一個用於數據定義的基類，所有自定義的 Item 都需要繼承它。
	# Field 本質是一個空容器，不會直接對數據進行處理。
	subreddit = scrapy.Field() # 存放 Reddit 貼文所屬的版塊名稱，例如：r/Python、r/EsgInvesting 
	link = scrapy.Field() 
	title = scrapy.Field()  
	date = scrapy.Field() # 貼文的發佈日期 
    # name = scrapy.Field(serializer=str) # Field可以設定「格式化規則
    # price = scrapy.Field(default='N/A') # 也可以設定字段未賦值時使用的默認值

'''
抓下來的數據就可以這樣操作：
item = ScrapyredditItem()  
item['id'] = '54'
item['name'] = 'iPhone 14'  
item['price'] = '$999' 
item['stock'] = 'In Stock'  
item['url'] = 'https://example.com/iphone14'  

'''

# Item 會限制只能存定義的那些欄位。如果試圖塞一個沒有定義的欄位，Scrapy 會直接報錯，防止抓到不應該抓的東西。
'''
item['undefined_field'] = 'test'  # KeyError，因為此欄位沒定義
'''

'''
使用 Item 的完整流程：
1. 定義 Item 在 item.py 中定義欄位，告訴 Scrapy 你要抓什麼。
2. 填充數據在爬蟲的 parse 方法裡，創建 Item，把抓到的數據塞進去。(spider)
3. 傳遞到 Pipeline Scrapy 會自動把 Item 傳給 Pipeline，你可以在那裡進一步處理數據（清洗、儲存）。
'''