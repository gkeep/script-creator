version = 2024.3.1

build_linux:
	pyinstaller --onefile src/main.py --name script_creator_$(version).bin

build_linux_docker: build_linux
	mv dist/script_creator_$(version).bin /app/builds

build_linux_cli_docker:
	pyinstaller --onefile src/constructor.py --name script_creator_cli.bin
	mv dist/script_creator_cli.bin /app/builds

build_windows:
	pyinstaller --noconsole --onefile src/main.py --name script_creator_$(version).exe
