# Script-creator

An application to create `bash` scripts from SQL scripts to execute them on machines running
`PostgresSQL` inside/outside a `docker` container.

## Why?

Because you need an easy to use and a polished solution for a mundane task.
Plus your error rate will be much lower, because all `bash` parts of the final script have been thoroughly tested.

## Installation

Download latest release from [Releases](https://github.com/gkeep/script-creator/releases/latest) page.

## Development

1. Clone the repo:
    `git clone https://github.com/gkeep/script-creator`
2. Create a `virtualenv`
    `python3 -m virtualenv venv`
3. Initialize the Python virtual environment
    `source venv/bin/activate` (command may differ depending on your OS and shell)
4. Install python requirements
    `pip install -r requirements.txt` (use `requirements_win.txt` on Windows)

Now you can build the application binary or run it from your IDE of choice.

Building the binary (Linux & Windows)
    `make build_linux` or `make build_windows`, depending on your OS


TODO: add screenshots
