version = "2023.11.0"

build_linux:
	pyinstaller --onefile src/main.py --name script_creator_$(version).bin

build_windows:
	pyinstaller --noconsole --onefile src/main.py --name script_creator_$(version).exe