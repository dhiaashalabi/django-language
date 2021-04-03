
# provice a list of language which your site support
LANGUAGE_CODE = "ar"
# اللغات الموجودة معنا في النظام
LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
]

TIME_ZONE = 'UTC'
USE_I18N = True
# List where django shold look into for django.po
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
    #local هو عبارة عن الملف الذي يحتوي ar/LC_MESSAGES/django.po
]

USE_L10N = True

USE_TZ = True
