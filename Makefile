health:
	poetry run ruff format api_automation
	ruff check --fix
	poetry run mypy --ignore-missing-imports --install-types --non-interactive --package api_automation
