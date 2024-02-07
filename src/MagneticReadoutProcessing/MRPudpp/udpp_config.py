import os
from pathlib import Path


class UDPPConfig(object):
    _instance = None

    PIPELINES_FOLDER: str = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))
    TMP_FOLDER: str = str(Path(PIPELINES_FOLDER).joinpath("generated/"))
    STATIC_FOLDER: str = str(Path(str(os.path.dirname(__file__))).joinpath("static"))
    TEMPLATE_FOLDER: str = str(Path(str(os.path.dirname(__file__))).joinpath("templates"))


    def __init__(self):
        pass



    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UDPPConfig, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


    @staticmethod
    def set_base_folder(_base_folder: str):

        if len(_base_folder) <= 0:
            return

        if not _base_folder.endswith("/"):
            _base_folder += "/"

        UDPPConfig.set_pipeline_folder(str(Path(str(os.path.dirname(_base_folder))).joinpath("pipelines/")))
        UDPPConfig.set_tmp_folder(str(Path(str(os.path.dirname(_base_folder))).joinpath("generated/")))


    @staticmethod
    def set_pipeline_folder(_pipeline_folder: str):
        if len(_pipeline_folder) <= 0:
            return

        Path(_pipeline_folder).mkdir(parents=True, exist_ok=True)
        UDPPConfig().PIPELINES_FOLDER = _pipeline_folder
    @staticmethod
    def set_tmp_folder(_tmp_folder: str):
        if len(_tmp_folder) <= 0:
            return

        Path(_tmp_folder).mkdir(parents=True, exist_ok=True)
        UDPPConfig().TMP_FOLDER = _tmp_folder
    @staticmethod
    def get_pipeline_folder() -> str:
        return UDPPConfig().PIPELINES_FOLDER

    @staticmethod
    def get_tmp_folder() -> str:
        return UDPPConfig().TMP_FOLDER

    @staticmethod
    def get_static_folder() -> str:
        return UDPPConfig().STATIC_FOLDER

    @staticmethod
    def get_template_folder() -> str:
        return UDPPConfig().TEMPLATE_FOLDER





