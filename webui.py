import logging

logging.getLogger("xformers").addFilter(lambda record: "A mathing Triton is not available" not in record.getMessage())

from modules.shared import cmd_opts

def webui():
    print('webui')

if __name__ == "__main__":
    print(__name__)
    print(cmd_opts)
    webui()

