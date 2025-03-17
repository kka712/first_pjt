# Django

## 0. setting

- `.gitignore`
- 가상환경 설정
    - `python -m venv venv`
    - `source venv/Scripts/activate`
- `README.md`

## 1. Django 프로젝트

1. django 설치
```shell
pip install django
```
2. 프로젝트 생성
```
django-admin startproject <pjt-name> <path> 
```
### django-admin startproject first_pjt . => .은 현재 위치를 말함

3. 서버실행 (종료 : `ctrl + c`)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```

5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```

