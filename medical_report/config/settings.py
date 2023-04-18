# -*- coding: utf-8 -*-
# @Organization  : Novogene
# @Author        : Charlin(7900)
# @Time          : 2023/4/17 18:14
# @Function      :

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 日志配置
LOGGING_LEVEL = 'DEBUG'

#


# 路径配置
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# 邮件配置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mt-op@novogene.com'
EMAIL_HOST_PASSWORD = 'Novo1234'

# 数据库路径
DATABASES_PATH = "/TJPROJ6/PG/pipeline/databases/WES_disease"

