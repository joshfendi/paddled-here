dev:
	source backend/venv/bin/activate && cd backend && uvicorn app.main:app --reload
