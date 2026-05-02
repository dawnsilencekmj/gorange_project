# RAS 프로젝트 LLM 인수인계 마스터 프롬프트

아래 내용을 그대로 다른 LLM에 입력하면, 현재 프로젝트와 유사한 결과물을 빠르게 재현할 수 있습니다.

---

## 1) 프로젝트 배경/목표
- 프로젝트명: Recipe Analysis System (RAS) 웹 개발 프로젝트
- 팀 상황: 웹 개발 초심자 3명
- 사내 환경: FastAPI(backend), React(frontend), PostgreSQL, Docker/Jenkins, 데이터 플랫폼(StarRocks/S3)
- 로컬 우회 개발: 사내 데이터 대신 미국 주식 데이터로 구조/로직 검증
- 핵심 목표:
  1. 대/중/소 카테고리별 float 통계 계산
  2. React 4개 페이지 구성
  3. 홈 대시보드 차트별 API 분리
  4. 차트 클릭 기반 교차 필터링(한 차트 선택이 다른 차트에 반영)

---

## 2) 산출물 요구사항
다음 항목을 포함한 풀스택 골격 코드를 생성하라.

### Backend (FastAPI)
- 경로: `backend/app`
- 구조:
  - `main.py` (CORS, `/health`, `/api/v1` 라우팅)
  - `api/v1/api.py`
  - `api/v1/endpoints/{dashboard,categories,explorer,playground}.py`
  - `services/stock_service.py`
  - `repositories/stock_repository.py`
- 데이터 소스:
  - `sample_data/us_stocks_sample.csv` 로드
- API 예시:
  - `/api/v1/dashboard/kpi`
  - `/api/v1/dashboard/timeseries`
  - `/api/v1/categories/stats`
  - `/api/v1/explorer/rows`
  - `/api/v1/playground/rule-demo`

### Frontend (React + Vite)
- 경로: `frontend`
- 필수 파일:
  - `package.json`, `vite.config.ts`, `index.html`, `src/main.tsx`
- Atomic Design 지향 구조:
  - `src/components/{atoms,molecules,organisms,templates}`
- 라우팅:
  - Home, CategoryAnalytics, DataExplorer, Playground (총 4페이지)
- API 연동:
  - Axios client (`src/shared/api/client.ts`)
  - Home은 KPI/Timeseries 호출
  - 나머지 페이지도 각 endpoint 호출 결과 표시

### 문서 (Markdown)
아래 문서를 생성/유지하라.
- `README.md`
- `docs/GLOSSARY.md`
- `docs/DEV_GUIDE.md`
- `docs/REQUEST_HISTORY.md`
- `docs/RUN_ON_IPAD.md`

---

## 3) 개발 원칙
- 코드보다 먼저 폴더 구조를 명확히 만든다.
- API는 endpoint/service/repository 계층 분리.
- React는 페이지/레이아웃/API 호출을 분리.
- 사내 이식성을 위해 환경 의존 로직 최소화.
- 샘플 데이터로 즉시 실행 가능해야 한다.

---

## 4) 실행 가이드 생성 요구
결과물에는 반드시 실행 방법을 포함하라.

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

- Frontend 기본: `http://localhost:5173`
- Backend 기본: `http://localhost:8000`

---

## 5) 최종 산출 형식 요구
LLM 응답은 다음 순서를 따르라.
1. 전체 폴더 트리
2. 핵심 파일 코드
3. 실행 방법
4. 기능 확인 체크리스트
5. 향후 확장(실데이터/DB/인증/배포)

---

## 6) 추가 요청(중요)
- 초심자 관점으로 파일별 역할 설명을 포함하라.
- 차트 교차 필터링 설계(전역 필터 상태 + API 재호출)를 설명하라.
- 향후 사내 데이터 플랫폼(StarRocks/S3)로 교체할 때 변경 지점을 명시하라.

