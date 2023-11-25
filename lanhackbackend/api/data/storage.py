import json
import datetime
import os

# get current working directory
DATA_PATH = os.path.dirname(os.path.realpath(__file__))


class Storage:
    def __init__(self) -> None:
        pass

    def init(self):
        print("Initializing storage")
        try:
            with open(f"{DATA_PATH}/uids.json", "r") as f:
                # if file is blank, write init json
                if f.read() == "":
                    self.__write_init_json()
        except:
            # file does not exist, create it and write init json
            self.__write_init_json()

    def push_uid(self, uid: str):
        try:
            # load json data
            with open(f"{DATA_PATH}/uids.json", "r") as f:
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
            with open(f"{DATA_PATH}/uids.json", "w") as f:
                json.dump(data, f)

            return True
        except:
            return False

    def get_uids(self):
        with open(f"{DATA_PATH}/uids.json", "r") as f:
            data = json.load(f)
        return data

    def __write_init_json(self):
        with open(f"{DATA_PATH}/uids.json", "w") as f:
            json.dump({"uids": []}, f)


storage = Storage()
