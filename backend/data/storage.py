import json
import datetime
import os
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

    def push_uid(self, uid: str) -> Union[tuple[Literal[True], Literal[None]],tuple[Literal[False], str]]:
        try:
            # load json data
            with open(FILE_PATH, "r") as f:
                data = json.load(f)

            # append new uid to data
            # timestamp in ISO format
            data["uids"].append(
                {
                    "uid": uid,
                    "timestamp": datetime.datetime.now().isoformat(),
                }
            )

            # write new uid to file
            with open(FILE_PATH, "w") as f:
                json.dump(data, f)

            return True, None
        except Exception as e:
            return False, str(e)

    def get_uids(self) -> json:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)["uids"]
        return data

    # util to write init json
    def __write_init_json(self):
        with open(FILE_PATH, "w") as f:
            json.dump({"uids": []}, f)


storage = Storage()
