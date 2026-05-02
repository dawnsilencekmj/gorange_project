# RAS Web Starter (FastAPI + React Atomic Design)

사내 템플릿과 유사한 구조로 만든 기초 프로젝트입니다.

## 실행
### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
현재는 구조 스켈레톤 중심이며, 사내 React 템플릿에 파일 병합해서 사용하세요.

## 주요 페이지
1. Home Dashboard
2. Category Analytics
3. Data Explorer
4. Playground


## iPad에서 확인
빠르게 접속 확인하려면 `docs/RUN_ON_IPAD.md` 체크리스트를 따라하세요.


### Frontend (Vite)
```bash
cd frontend
npm install
npm run dev
```

- 기본 URL: `http://localhost:5173`
- API 기본 URL: `http://localhost:8000/api/v1`
