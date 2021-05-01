# 2020-05-01 장고 세션 - 이민정 매니저님

- 장고란? 파이썬 기반의 오픈소스 웹 프레임워크   
  - 오픈소스 기반

- 장고 사용하기 전 해야 할 세팅들
  1. Django project 생성
  2. Django App 생성
  3. Django 본격 준비
     1. settings.py
     2. templates,static 폴더 생성
     3. views.py 작성
     4. urls.py 작성

- 가상환경을 만들시 각 가상환경마다 다른 파이썬 버전을 사용할 수 있다.


- 명령어 [WSL-Ubuntu 기준]: 
  - sudo apt-get insatll python3-venv : 파이썬 가상환경 설치시 필요함.
  - python3 -m venv `가상환경이름` : 가상환경이름으로 가상환경 폴더를 만듬
  - source(.으로 대체 가능함) `가상환경이름`/bin/activate : 가상환경 켜기
  - deactivate : 가상환경 종료
  - django-admin startproject `프로젝트이름` : 프로젝트 생성하기
    - 프레임워크이기 때문에 파일구조 및 디렉터리명을 임의로 수정하면 안됨
  - python3 manage.py startapp `앱이름` : 프로젝트 폴더 내에서 실행해야 함
    - 1개의 project 안에 여러개의 app이 있을 수 있다.

- 사용 구조
  - settings.py : startproject 시 다른 기본 코드들(manage,asgi ...etc)을 알고 있지만 새로 만든 app은 모르므로 startapp 후에는 앱 이름을 INSTALLED_APPS에 추가해줘야함
    - INSTALLED_APPS 리스트에 '`앱이름`',을 추가해주기
    - STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)을 추가해주기
  - 앱 폴더 내에 templates,static 폴더 만들기 : mkdir templates static
  - 앱폴더 내의 views.py : `html이름.html`을 렌더해주는 `html이름`(request) 함수를 설정해주기
    - home(request): return render(request,'`html이름.html`)
  - 프로젝트 폴더 내의 urls.py: urlpatterns 리스트 내에 path('', `앱이름`.views.`html이름`, name = `html이름`), 추가해주기
  - 

- 배운 점
  - Python에서도 Trailing Comma를 사용할 수 있다. 딱히 문법적으로 큰 의미는 없지만 이후에 데이터가 추가될 것으로 예상되는 리스트, 튜플 등을 사용할 때 넣어주면 GIT 및 VSCODE 관리상 용이점을 가질 수 있다. [관련링크](https://mingrammer.com/tips-of-using-comma-in-python/)