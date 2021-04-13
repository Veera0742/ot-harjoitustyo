class OpseRepository():
    def __init__(self, file_path):
        self.file_path=file_path

    def add_user(self, username:str, password:str):


opse_Repository = OpseRepository(OPSE_FILE_PATH)
