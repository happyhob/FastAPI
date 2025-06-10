# 🛡️ FastAPI 인증 기반 웹 애플리케이션
이 프로젝트는 FastAPI 기반으로 제작된 간단한 사용자 인증 시스템입니다. SQLite 데이터베이스와 SQLAlchemy ORM을 사용하며, JWT 토큰을 활용한 로그인 인증 방식을 포함합니다.

## 📂 프로젝트 구조
├── auth.py          # 사용자 생성, 로그인, 토큰 발급 및 인증 관련 라우터
├── database.py      # 데이터베이스 연결 및 세션 설정
├── main.py          # FastAPI 앱 실행 및 라우터 등록
├── models.py        # SQLAlchemy 사용자 모델 정의
├── note.txt         # 주요 모듈 설명 및 사용 예시

## 🧩 주요 파일 설명
### main.py
- FastAPI 앱을 생성하고 실행하는 메인 파일입니다.
- 인증 라우터(auth.py)를 포함시키며, / 엔드포인트에서 인증 확인 기능을 제공합니다.

### auth.py
사용자 인증 관련 API가 정의된 라우터입니다.

#### 기능:
    - 회원가입 (POST /auth/): 사용자 정보를 받아 DB에 저장
    - 로그인 (POST /auth/token): 유저 인증 및 JWT 토큰 반환
    - 토큰 검증 함수: 인증된 사용자만 접근 가능한 엔드포인트에서 사용 가능

#### 사용 기술:
    - OAuth2PasswordBearer, JWT, passlib(비밀번호 해싱)

### models.py
- 사용자 테이블을 정의하는 SQLAlchemy 모델이 포함되어 있습니다.
```python
class Users(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

```
### database.py
SQLite 데이터베이스를 설정하고 SQLAlchemy 세션을 초기화합니다.
```python
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
```

### note.txt
- 인증 및 보안 관련 사용 모듈 설명이 포함된 문서입니다.

설치 모듈 및 주요 기능 요약:
| 모듈                          | 설명 및 사용 목적                           |
| --------------------------- | ------------------------------------ |
| `python-jose[cryptography]` | JWT 토큰 생성, 검증, 암호화 등 인증 처리           |
| `passlib[bcrypt]`           | 비밀번호 해싱 및 로그인 시 검증 처리                |
| `python-multipart`          | 파일 업로드 및 `multipart/form-data` 요청 처리 |


## 🛠 설치 방법
```bash
pip install fastapi uvicorn pydantic
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
pip install python-multipart

```


## ▶ 실행 방법
```bash
uvicorn main:app --reload
```


## 🔐 주요 기능 요약
- JWT 기반 토큰 인증
- 비밀번호 bcrypt 해싱 처리
- FastAPI 라우터 분리 및 의존성 주입
- SQLite 사용한 경량 데이터베이스 처리


현재 변경된 것이 깃에 올라가는지 확인하는 중입니다.
깃의 이메일과, 이름을 맞춰주었다. 잔디가 심어지는지 확인해보자
