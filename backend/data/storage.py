import json
import datetime
import os
import pathlib
from typing import Optional, Literal, Union

# path to data file containing uids
DATA_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = DATA_PATH + "/uids.json"


class Storage:
    def __init__(self) -> None:
        pass

    def init(self):
        try:
            with open(FILE_PATH, "r") as f:
                # if file is blank, write init json
                if f.read() == "":
                    self.__write_init_json()
        except:
            # file does not exist, create it and write init json
            self.__write_init_json()

    def push_uid(self, uid: str):
        try:
            # load json data
            if not pathlib.Path(FILE_PATH).is_file():
                self.__write_init_json()

            with open(FILE_PATH, "r") as f:
                data = json.load(f)

            # append new uid to data
            # timestamp in ISO format
            item = {
                "uid": uid,
                "timestamp": datetime.datetime.now().isoformat(),
            }
            data["uids"].append(item)

            # write new uid to file
            with open(FILE_PATH, "w") as f:
                json.dump(data, f)

            return (True, item)
        except Exception as e:
            return (False, e)

    def get_uids(self) -> json:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)["uids"]
        return data

    def clear_uids(self) -> bool:
        path = pathlib.Path(FILE_PATH)
        if path.exists():
            path.unlink()
            return True
        else:
            return False

    # util to write init json
    def __write_init_json(self):
        with open(FILE_PATH, "w") as f:
            json.dump({"uids": []}, f)


storage = Storage()
