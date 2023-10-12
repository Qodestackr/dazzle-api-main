#--------------------- Dazzle HR Django Backend Makefile ---------------------#
SHELL := /bin/bash
MANAGE_PY = ./manage.py
FRONTEND_PATH = ../clientfrontend

# export PYTHONPATH := path
# export DJANGO_SETTINGS_MODULE := ./core/settings.py

RESET = \033[0m
CENTER_TEXT = \033[H
COLOR_TITLE = \033[1;5;33m #37m
COLOR_INFO = \033[1;32m
COLOR_COMMAND = \033[1;36m
CYAN = \033[1;3;36m
RED ?= \033[0;31m
BLACK = \033[0;30m


define print_command
	@echo -e "$(COLOR_TITLE)---------------------------------------------------------------$(RESET)"
	@echo -e "$(CYAN) Welcome to Dazzle HR API $(RESET)"

	@echo -e "$(COLOR_INFO)$1$(RESET)"
	@echo -e "$(COLOR_TITLE)---------------------------------------------------------------$(RESET)"
endef


runserver:
	$(call print_command, "----- Creating database migration files -----")
	python $(MANAGE_PY) runserver


migrations:
	$(call print_command, "----- Creating database migration files -----")
	python $(MANAGE_PY) makemigrations

migrate:
	$(call print_command, "----- Running database migrations -----")
	python $(MANAGE_PY) migrate

superuser:
	$(call print_command, "----- Creating a superuser -----")
	python $(MANAGE_PY) createsuperuser

collectstatic:
	$(call print_command, "----- Collecting static files -----")
	python $(MANAGE_PY) collectstatic

test:
	$(call print_command, "----- Running Django tests -----")
	python $(MANAGE_PY) test

help:
	@echo -e "$(COLOR_INFO)----- Dazzle HR Django Backend Makefile commands -----$(RESET)"
	@echo -e "$(COLOR_COMMAND)make runserver$(RESET)     - Start the Django dev server."
	@echo -e "$(COLOR_COMMAND)make migrations$(RESET)     - Create database migration files."
	@echo -e "$(COLOR_COMMAND)make migrate$(RESET)       - Run database migrations."
	@echo -e "$(COLOR_COMMAND)make superuser$(RESET) - Create a superuser for the Django project."
	@echo -e "$(COLOR_COMMAND)make collectstatic$(RESET) - Collect static files for production use."
	@echo -e "$(COLOR_COMMAND)make test$(RESET)          - Run Django tests."
	@echo -e "$(COLOR_COMMAND)make help$(RESET)          - Show the help message."

.PHONY: runserver migrate migrations createsuperuser collectstatic test help