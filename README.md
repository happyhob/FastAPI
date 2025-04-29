# PostgreSQL 소개

PostgreSQL은 오픈 소스 객체-관계형 데이터베이스 관리 시스템(RDBMS)입니다. 안정성, 확장성, 표준 준수, 커뮤니티 중심 개발로 널리 사용되며, 강력한 기능과 유연한 확장성을 제공합니다.

---

## 🔑 주요 특징

- **오픈 소스**  
  자유롭게 사용, 수정, 배포 가능하며 기업에서도 라이선스 걱정 없이 사용 가능합니다.

- **객체-관계형 구조**  
  전통적인 관계형 모델에 객체지향 개념을 결합한 형태로 사용자 정의 타입, 상속, 함수 오버로딩 등을 지원합니다.

- **SQL 표준 준수**  
  SQL:2008 대부분을 준수하며, 공통 테이블 표현식(CTE), 윈도우 함수, JSON 데이터 처리 등을 지원합니다.

- **ACID 트랜잭션**  
  PostgreSQL은 원자성, 일관성, 고립성, 지속성(ACID)을 보장하며, MVCC(다중 버전 동시성 제어) 기반의 동시성 처리를 제공합니다.

- **확장성**  
  다양한 프로그래밍 언어(SQL, PL/pgSQL, Python 등)로 저장 함수(Stored Procedure)를 작성할 수 있고, 확장 모듈을 통한 기능 확장이 가능합니다.

- **NoSQL 기능 지원**  
  JSON 및 JSONB를 통한 문서 기반 데이터 저장 및 질의 기능을 제공합니다.

- **다양한 인덱싱 방식**  
  B-Tree, Hash, GIN, GiST 등 다양한 인덱스 방식을 통해 성능을 최적화할 수 있습니다.

---

## 💻 사용 예시

```sql
-- 테이블 생성
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 데이터 삽입
INSERT INTO users (name, email) VALUES ('홍길동', 'hong@example.com');

-- 데이터 조회
SELECT * FROM users WHERE name = '홍길동';


## ⬇️설치방법
[설치사이스](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
원하는 버전 선택 >> 해당 운영체제 선택 >> install

나머지 next 선택하다가 , "Select the locale to be used by the new database dluster."라는 선택에서 korean, Korea 선택했습니다.
이후 모두 next 하다가 " Completing the PostgreSQL Setup Wizard" 런처 빌더 선택 해제하고 finish 하면 됩니다!!

pgAdmin 4 앱 실행시키면 ui로 데이터베이스 확인 가능!
