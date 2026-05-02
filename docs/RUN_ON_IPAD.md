# iPad에서 실제 화면 확인하기 (1분 체크리스트)

## 0) 사전 확인
- [ ] Codex/개발 플랫폼이 **포트 프리뷰 URL** 또는 **외부 접속 URL** 제공
- [ ] `backend/requirements.txt` 설치 가능

## 1) 백엔드 실행
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 2) API 동작 확인
브라우저에서 아래 URL 확인
- `/health`
- `/api/v1/dashboard/kpi`
- `/api/v1/dashboard/timeseries`

예시:
- `https://<preview-url>/health`
- `https://<preview-url>/api/v1/dashboard/kpi`

## 3) iPad에서 확인
- [ ] iPad Safari에서 위 URL 열기
- [ ] JSON 응답이 보이면 서버 접근 성공

## 4) 안될 때 점검
- [ ] FastAPI 로그에 요청 흔적이 있는지 확인
- [ ] 포트 번호(8000) 맞는지 확인
- [ ] 플랫폼의 공개 URL이 해당 포트와 연결되어 있는지 확인

## 5) 다음 단계
현재 frontend는 스켈레톤입니다. 실제 UI 확인은 React 템플릿 빌드/실행 후 프리뷰 URL 연결이 필요합니다.
