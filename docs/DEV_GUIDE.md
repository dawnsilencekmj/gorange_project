# 개발 가이드 라인

## 차트 API 추가
1. `backend/app/api/v1/endpoints/dashboard.py`에 endpoint 추가
2. `backend/app/services/stock_service.py`에 집계 로직 추가
3. `frontend/src/features/dashboard/api.ts`에 호출 함수 추가
4. `frontend/src/pages/Home`에서 차트 컴포넌트 연결

## 필터 연동
- 전역 상태(store)에서 선택 필터를 관리하고 모든 차트 API 호출에 동일 query를 전달한다.

## 파일 역할
- endpoints: HTTP 입출력
- services: 비즈니스 로직
- repositories: 데이터 접근
- components atoms~templates: UI 재사용 구조
