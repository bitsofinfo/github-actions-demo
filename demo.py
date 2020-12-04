from jinja2 import Template
import sys

def main():
    args = sys.argv[1:]
    print(Template("arg1={{arg1}}").render({"arg1":args[0]}))

if __name__ == "__main__":
    main()