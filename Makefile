default:
	@echo "'make ui'" to compile ui templates to py modules
	@echo "'make lint'" to run flake8 checks


#
# pep8 check section
#

.PHONY: lint
lint:
	flake8 --config=flake8.cfg fenril/


#
# UI template section
#

PYUIC = pyuic5
UI_DIR = templates
PY_DIR = fenril/ui
UI_TEMPLATES = $(wildcard $(UI_DIR)/*.ui)
PY_TEMPLATES = $(patsubst $(UI_DIR)/%.ui,$(PY_DIR)/%.py,$(UI_TEMPLATES))

.PHONY: ui
ui: $(PY_TEMPLATES)

$(PY_DIR)/%.py: $(UI_DIR)/%.ui
	$(PYUIC) $^ -o $@
