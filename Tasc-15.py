import logging
import os
import argparse
from collections import namedtuple

logging.basicConfig(
    filename="info.log", filemode="w", encoding="UTF-8", level=logging.INFO
)
logger = logging.getLogger(__name__)


def way_to_directory(directory: str) -> None:
    if not directory or not os.listdir():
        logger.error("Данной дириктории не существует!")
    else:
        inf = namedtuple("DATA", ["name", "extension", "is_directory", "parent_dir"])

        for dir_path, _, file_name in os.walk(directory):
            dir_inf = inf(
                os.path.basename(dir_path), None, True, os.path.dirname(dir_path)
            )

            logger.info(dir_inf)

            for file in file_name:
                file_inf = inf(
                    file.rsplit(".")[0],
                    file.rsplit(".")[1],
                    False,
                    os.path.dirname(dir_path),
                )
                logger.info(file_inf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Folder info",
        description="Info about folder",
        epilog="write log file with folders and files",
    )
    parser.add_argument(
        "directory",
        metavar="patn",
        type=str,
        nargs="?",
        help="Enter tne patn to tne directory",
    )
    path = parser.parse_args()
    way_to_directory(path.directory)
