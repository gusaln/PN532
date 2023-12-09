import json

VERSION = "1.0.0"

ADAPTERS = ["hsu", "i2c", "spi", "swhsu"]

core_lib_data = {
    "$schema": "https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/schema/library.json",
    "name": "PN532",
    "description": "This is a library for the PN532 to use NFC technology.",
    "keywords": "communication,nfc,pn532",
    "version": VERSION,
    "repository": {
        "type": "git",
        "url": "https://github.com/gusaln/PN532.git"
    },
    "authors": [
        {
            "name": "Gustavo Lopez",
            "email": "git.gustavolopez.xyz@gmail.com",
            "maintainer": True
        }
    ],
    "frameworks": "*",
    "platforms": "*",
    "dependencies": [
        {
            "name": "NDEF",
            "version": "https://github.com/don/NDEF#1.1.0"
        }
    ],
    "build": {
        "srcDir": "."
    }
}

with open("PN532/library.json", "w") as fp:
    print("Writing core library file")
    json.dump(core_lib_data, fp, indent=2)

for adapter in ADAPTERS:
    adapter_lib_data = dict(**core_lib_data)
    adapter_lib_data["name"]="PN532_{0}".format(adapter.upper())
    adapter_lib_data["description"]="This is a library for the PN532 to use NFC technology through {0}.".format(adapter.upper())
    adapter_lib_data["keywords"]="communication,nfc,pn532,pn532_{0},{0}".format(adapter)

    adapter_lib_data["dependencies"]=[]

    with open("PN532_{}/library.json".format(adapter.upper()), "w") as fp:
        print("Writing {} adapter library file".format(adapter))
        json.dump(adapter_lib_data, fp, indent=2)