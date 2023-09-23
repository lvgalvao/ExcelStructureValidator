kill:
	kill -9 $(shell lsof -t -i :8000)