# API-Django-Project

# 熱門文章 API

專案使用 Django 3.2，並部署在 Docker 使用 Python 3.7，資料庫 MariaDB 

## 系統需求
- Docker
- Docker Compose

## 設置步驟

### 將專案clone:
```bash
git clone https://github.com/jeff0914/API-Django-Project.git
cd API-Django-Project/docker
```

### 啟動 Docker:
```bash
docker-compose up -d
```
將會建立和啟動所有必要的容器（Django, MariaDB)

### 執行資料庫遷移:
```bash
docker-compose exec web python manage.py migrate
```

### 建立使用者:
```bash
docker-compose exec web python manage.py createsuperuser
```
按照提示輸入使用者名稱、電子郵件和密碼。

### 取得 JWT token:
透過 api/token-auth/ endpoint 並提供使用者名稱和密碼以獲得 JWT token。此 token 之後可用於存取文章API。

### 使用 API
一旦環境設置完成，您就可以透過以下的 endpoints 使用 API：

GET /api/articles/ - 取得所有文章
POST /api/articles/ - 新增文章
GET /api/articles/<id>/ - 取得特定文章
PUT /api/articles/<id>/ - 修改特定文章
DELETE /api/articles/<id>/ - 刪除特定文章

### 資料來源
[DailyView](https://dailyview.tw/)

### License
MIT license
