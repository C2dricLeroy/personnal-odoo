COMPOSE = docker compose
ODOO_CONTAINER = odoo
POSTGRES_CONTAINER = odoo-postgres
INIT_MODULES = base, web
DB_NAME = admin
.PHONY: up down restart logs shell build

init:
	@echo "--- Démarrage de la base de données ---"
	docker compose up -d db
	@echo "--- Attente du service PostgreSQL (10s) ---"
	sleep 10
	@echo "--- Installation initiale des modules : $(INIT_MODULES) ---"
	$(COMPOSE_RUN) odoo -c /etc/odoo/odoo.conf -d $(DB_NAME) -i $(MODULES) --stop-after-init
	@echo "--- Lancement de l'environnement complet ---"
	docker compose up -d

## Démarrer les services
start:
	$(COMPOSE) up

update:
	$(COMPOSE) up -d
	$(COMPOSE) exec $(ODOO_CONTAINER) odoo  -u $(MODULE) -d admin --dev=assets --stop-after-init
	$(COMPOSE) down
	$(COMPOSE) up

startd:
	$(COMPOSE) up -d

## Arrêter les services
down:
	$(COMPOSE) down

## Redémarrer Odoo
restart:
	$(COMPOSE) restart $(ODOO_CONTAINER)

## Shell dans le conteneur Odoo
shell:
	$(COMPOSE) exec $(ODOO_CONTAINER) bash

## Rebuild des images (si Dockerfile plus tard)
build:
	$(COMPOSE) build

dump:
	docker compose exec db \
		pg_dump -U odoo -F c postgres > ./db/odoo_$(shell date +%Y%m%d_%H%M).dump

restore_dump:
	@test -n "./db/$(FILE)" || (echo "❌ Usage: make restore_dump FILE=odoo_xxx.dump" && exit 1)
	cat ./db/$(FILE) | docker compose exec -T db \
		pg_restore -U odoo -d postgres --clean --if-exists