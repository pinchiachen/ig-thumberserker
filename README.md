# ig-thumberserker｜哀居狂讚士

## TL;DR
> ***讚爆你想讚爆的人***


## How to use
### Step 1. Install chromedriver
- 下載相對應你目前 **Chrome** 瀏覽器版本的 **chromedriver**
- 將 **chromedriver** 丟入 `/usr/local/bin`

### Step 1.5 (Optional) Build virtual environment
- `python3 -m venv .venv`
- `source .vanv/bin/active`
  
### Step 2. `pip install -r requirement.txt`

### Step 3. `target.py` & `secret.py`
```python
## target.py
TARGET_ACCOUNT = 'YOUR_TARGET_ACCOUNT'

def get_target_account():
    return TARGET_ACCOUNT
```

```python
## secret.py
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

def get_account():
    return USERNAME, PASSWORD
```

### Step 4. Set `SCROLL_PAGE`
- `SCROLL_PAGE` 用來控制你要滑幾頁

### Step 5. `python3 main.py`
- 開始你的表演


## Note
- 目前只適用繁體中文版 IG
- 沒檢查是否按過愛心，所以點讚過的會把讚收回來


## TODO

### 判斷是否點過愛心
- 點愛心 a.k.a ***狂讚士***
  - 適用剛認識新朋友，刷存在感
- 把愛心全部收回來 a.k.a ***倒讚幫***
  - 適用跟朋友絕交，不讓對方貼文多任何一個愛心，一個都不能
