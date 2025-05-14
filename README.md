# 🛠 Small Full Stack 프로젝트 (React + FastAPI + SQLite)

## 📦 프로젝트 아키텍처



---

## ⚙️ 설치 및 실행 방법

### ✅ 프론트엔드 (React)

1. **Node.js 설치**

   [Node.js 공식 홈페이지](https://nodejs.org/)에서 Node.js를 설치하세요.

2. **React 프로젝트 생성**

   ```bash
   npx create-react-app your-folder-name
   cd your-folder-name
   npm start
  '''


  ✅ 백엔드 (FastAPI)
1. 가상 환경 설정 (선택 사항)

'''bash
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
'''

2. 필수패키지 설치
'''bash
pip install fastapi pydantic uvicorn sqlalchemy
'''

3. 서버 실행
'''bash
uvicorn main:app --reload

'''

🔒 CORS 설정
React 프론트엔드와 FastAPI 백엔드가 다른 도메인/포트에서 실행되므로 CORS(Cross-Origin Resource Sharing) 설정이 필요합니다.

'''python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",  # React 개발 서버 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''

```
project-root/
│
├── backend/
│   ├── main.py
│   └── ...
│
├── frontend/
│   └── (create-react-app으로 생성된 폴더)
│
└── README.md
```
