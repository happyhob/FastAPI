# FastAPI + MongoDB CRUD 예제

이 프로젝트는 **FastAPI**와 **MongoDB**를 사용하여 기본적인 CRUD 기능을 구현한 예제입니다. `motor`를 통해 비동기로 MongoDB에 접근하며, 코드 구조를 모듈별로 분리하여 유지보수가 용이하게 설계했습니다.

---

## ✅ 주요 기능

- 비동기 MongoDB 연동 (`motor`)
- Todo 모델 기반 CRUD 구현
- 라우팅, 스키마, 데이터베이스 분리 구조
- 환경 변수 파일을 통한 설정 관리
- Swagger UI를 통한 API 테스트 지원

---

## 📁 프로젝트 구조

```bash
.
├── config
│   ├── database.py           # MongoDB 연결 설정
│   └── deskenv               # 환경 변수 관련 파일 (예: .env 등)
│
├── env                       # (설정 관련 디렉토리로 추정)
│
├── models
│   └── todos.py              # MongoDB 데이터 모델 정의
│
├── routes
│   └── route.py              # FastAPI 라우터 정의
│
├── schema
│   └── schemas.py            # Pydantic 기반 요청/응답 스키마 정의
│
├── main.py                   # FastAPI 애플리케이션 진입점
├── requirements.txt          # 의존성 목록
