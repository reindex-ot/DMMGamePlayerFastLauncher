import os
from pathlib import Path

import requests
from static.config import UrlConfig
from windows_pathlib import WindowsPathlib


class Dump:
    @classmethod
    def dump(cls):
        item = [(k, v) for k, v in Env.__dict__.items() if not k.startswith("__") and not isinstance(v, classmethod)]
        return dict(item)


class Env(Dump):
    VERSION = "v5.0.3"
    RELEASE_VERSION = requests.get(UrlConfig.RELEASE_API).json().get("tag_name", VERSION)

    DEVELOP: bool = os.environ.get("ENV") == "DEVELOP"
    APPDATA: Path = Path(os.getenv("APPDATA", default=""))
    PROGURAM_FILES: Path = Path(os.getenv("PROGRAMFILES", default=""))
    DESKTOP: Path = WindowsPathlib.desktop()

    DEFAULT_DMM_GAME_PLAYER_PROGURAM_FOLDER: Path = PROGURAM_FILES.joinpath("DMMGamePlayer")
    DEFAULT_DMM_GAME_PLAYER_DATA_FOLDER: Path = APPDATA.joinpath("dmmgameplayer5")

    SYSTEM_ROOT = Path(os.getenv("SYSTEMROOT", default=""))
    SYSTEM32 = SYSTEM_ROOT.joinpath("System32")
    SCHTASKS = SYSTEM32.joinpath("schtasks.exe")