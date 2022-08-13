from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def main():
    environment = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"), trim_blocks=True
    )
    template = environment.get_template("hello.j2")
    print(template.render(name="world"))


if __name__ == "__main__":
    main()
