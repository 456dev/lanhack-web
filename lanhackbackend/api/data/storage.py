import json
import datetime


class Storage:
    def __init__(self) -> None:
        pass

    def init(self):
        print("Initializing storage")
        try:
            with open("api/data/uids.json", "r") as f:
                # if file is blank, write init json
                if f.read() == "":
                    self.__write_init_json()
        except:
            # file does not exist, create it and write init json
            self.__write_init_json()

    def push_uid(self, uid: str):
        try:
            # load json data
            with open("api/data/uids.json", "r") as f:
                data = json.load(f)
            # append new uid
            item = {"uid": uid, "timestamp": str(datetime.datetime.now())}
            data["uids"].append(item)
            # write new uid to file
            with open("api/data/uids.json", "w") as f:
                json.dump(data, f)
            return True
        except:
            return False

    def get_uids(self):
        with open("api/data/uids.json", "r") as f:
            data = json.load(f)
        return data

    def __write_init_json(self):
        with open("api/data/uids.json", "w") as f:
            json.dump({"uids": []}, f)


storage = Storage()
