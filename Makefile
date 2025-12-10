.PHONY: install_local fmt clean

install_local:
	python3 -m pip install . --break-system-packages

fmt:
	ruff format

clean: fmt
	find . -type d -name ".ruff_cache" | xargs rm -rf
	find . -type d -name "__pycache__" | xargs rm -rf
	rm odc_sdk_generated.env