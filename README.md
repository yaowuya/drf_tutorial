https://github.com/liaogx/drf-tutorial.git
### 一、修改配置文件`drf_tutorial>settings.py` 
  1. `ALLOWED_HOSTS = ["*"]`

  2. 修改数据库配置文件

  3. 修改语言和时区：

     ```python
     LANGUAGE_CODE = 'zh-hans'
     
     TIME_ZONE = 'Asia/Shanghai'
     ```

4. 添加

   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, "static")
   
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "staticfiles"),
   ]
   ```

### 二、初始化数据库和创建admin账号

````python
python manage.py createsuperuser    admin/123456
python manage.py makemigrations
python manage.py migrate
````

### 三、在setting中增加drf全局配置

```python
# DRF的全局配置
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [  # 解析request.data
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
}
```

在INSTALLED_APPS中新增依赖：

```python
'rest_framework',  # RESTFUL API
'rest_framework.authtoken', #drf 自带token认证
```

### 四、在urls中配置权限路由

```python
path('api-auth/', include('rest_framework.urls')),
```

`xxx/api-auth/login/`

