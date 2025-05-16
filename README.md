# Jinja2 템플릿
이 프로젝트는 Jinja2 템플릿 엔진의 사용 예시를 작성한 브런치입니다
Jinja2는 Python 기반의 강력한 템플릿 언어로, 웹 페이지(특히 Flask와 함께 사용)나 설정 파일, 이메일 등 다양한 텍스트 기반 출력물을 동적으로 생성할 수 있습니다.

📌 Jinja2란?
Jinja2는 HTML 등 텍스트 파일 내에서 변수 출력, 조건문, 반복문 등을 사용할 수 있도록 해주는 템플릿 언어입니다.
템플릿을 통해 **프레젠테이션 로직(화면 처리)**과 **비즈니스 로직(데이터 처리)**을 분리하여 유지보수성과 확장성을 높일 수 있습니다.

# 설피 라이브러리
```bash
pip install -r requirements.txt
```


🧩 기본 문법
1. 변수 출력
```html
안녕하세요, {{ name }} 님!
```

2. 조건문 (if 문)
```html
{% if user.is_admin %}
  <p>관리자 페이지에 오신 것을 환영합니다.</p>
{% else %}
  <p>일반 사용자 페이지입니다.</p>
{% endif %}

```

3. 반복문 (for 문)
``` html
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}기본 제목{% endblock %}</title>
</head>
<body>
  <header>{% block header %}기본 헤더{% endblock %}</header>
  <main>{% block content %}{% endblock %}</main>
</body>
</html>

```
