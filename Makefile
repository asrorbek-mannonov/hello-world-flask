up:
	docker compose up -d
restart:
	docker compose down --volumes && docker compose up -d --build
stop:
	docker compose stop
delete:
	docker compose down