from datetime import datetime
from math import floor
from operator import floordiv
from pathlib import Path
from typing import Any

from options import Options


class FileOrganizer:
    islogging: bool
    logs_path: Path

    def __init__(self, islogging: bool = True, logs_path: Path = Path("logs.txt")) -> None:
        self.islogging: bool = islogging
        self.logs_path: Path = logs_path


    def organize(self, path: Path, organization_type: Options.OrganizationTypes, value: Any = None) -> None:
        if not path.exists():
            raise ValueError(f"{path} does not exist.")

        if not isinstance(organization_type, Options.OrganizationTypes):
            raise TypeError(f"Expected: {Options.OrganizationTypes}, got: {type(organization_type)}")


        current_files: list[Path] = [p for p in path.iterdir() if p.is_file()]

        # organize after creation date
        if organization_type == Options.OrganizationTypes.cDate:
            # check if value is valid
            if not isinstance(value, Options.TimeUnits):
                raise TypeError(f"Expected: {Options.TimeUnits}, got: {type(value)}")

            # move current files to the correct folder
            for file in current_files:
                # get creation date of current file
                c_date: datetime = datetime.fromtimestamp(file.stat().st_ctime)

                # organize after creation date by day
                if value == Options.TimeUnits.Day:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{c_date.year:04}-{c_date.day:02}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)


                # organize after creation date by year
                if value == Options.TimeUnits.Year:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{c_date.year:04}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)



        # organize after modification date
        if organization_type == Options.OrganizationTypes.mDate:
            # check if value is valid
            if not isinstance(value, Options.TimeUnits):
                raise TypeError(f"Expected: {Options.TimeUnits}, got: {type(value)}")

            # move current files to the correct folder
            for file in current_files:
                # get modification date of current file
                m_date: datetime = datetime.fromtimestamp(file.stat().st_mtime)

                # organize after modification date by day
                if value == Options.TimeUnits.Day:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{m_date.year:04}-{m_date.day:02}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)

                # organize after modification date by year
                if value == Options.TimeUnits.Year:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{m_date.year:04}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)


        # organize after size
        if organization_type == Options.OrganizationTypes.Size:
            # check if value is valid
            if not isinstance(value, Options.SizeUnits):
                raise TypeError(f"Expected: {Options.SizeUnits}, got: {type(value)}")

            # get max_length for size
            max_length: int = 0
            for file in current_files:
                size: int = file.stat().st_size
                for _ in range(1 if value.value == "KB" else 2 if value.value == "MB" else 3 if value.value == "GB" else 4):
                    size = floor(size / 1024)

                if len(f"{size}" > max_length):
                    max_length = len(f"{size}")


            # move current files to the correct folders
            for file in current_files:
                # get size of the file
                size: int = file.stat().st_size
                for _ in range(1 if value.value == "KB" else 2 if value.value == "MB" else 3 if value.value == "GB" else 4):
                    size = floor(size / 1024)

                # create the correct folder if it doesn't exist
                folder: Path = Path(path, f"{size:0{max_length}} {value.value}")
                if not folder.exists():
                    folder.mkdir()
                    self.log(None, folder)

                # move file to folder
                target_path: Path = Path(folder, file.resolve().parts[-1])
                file.move(target_path)
                self.log(file, target_path)



    def log(self, path_before: Path | None, path_after: Path | None, silent: bool = False) -> None:
        log_message: str = f"{path_before.resolve() if not path_before is None else "\\"} -> {path_after.resolve() if not path_after is None else "\\"}"
        print(log_message)
        with self.logs_path.open("a") as logs:
            logs.write(f"{log_message}\n")


from datetime import datetime
from math import floor
from operator import floordiv
from pathlib import Path
from typing import Any

from options import Options


class FileOrganizer:
    islogging: bool
    logs_path: Path

    def __init__(self, islogging: bool = True, logs_path: Path = Path("logs.txt")) -> None:
        self.islogging: bool = islogging
        self.logs_path: Path = logs_path


    def organize(self, path: Path, organization_type: Options.OrganizationTypes, value: Any = None) -> None:
        if not path.exists():
            raise ValueError(f"{path} does not exist.")

        if not isinstance(organization_type, Options.OrganizationTypes):
            raise TypeError(f"Expected: {Options.OrganizationTypes}, got: {type(organization_type)}")


        current_files: list[Path] = [p for p in path.iterdir() if p.is_file()]

        # organize after creation date
        if organization_type == Options.OrganizationTypes.cDate:
            # check if value is valid
            if not isinstance(value, Options.TimeUnits):
                raise TypeError(f"Expected: {Options.TimeUnits}, got: {type(value)}")

            # move current files to the correct folder
            for file in current_files:
                # get creation date of current file
                c_date: datetime = datetime.fromtimestamp(file.stat().st_ctime)

                # organize after creation date by day
                if value == Options.TimeUnits.Day:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{c_date.year:04}-{c_date.day:02}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)


                # organize after creation date by year
                if value == Options.TimeUnits.Year:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{c_date.year:04}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)



        # organize after modification date
        if organization_type == Options.OrganizationTypes.mDate:
            # check if value is valid
            if not isinstance(value, Options.TimeUnits):
                raise TypeError(f"Expected: {Options.TimeUnits}, got: {type(value)}")

            # move current files to the correct folder
            for file in current_files:
                # get modification date of current file
                m_date: datetime = datetime.fromtimestamp(file.stat().st_mtime)

                # organize after modification date by day
                if value == Options.TimeUnits.Day:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{m_date.year:04}-{m_date.day:02}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)

                # organize after modification date by year
                if value == Options.TimeUnits.Year:
                    # create the correct folder if it doesn't exist
                    folder: Path = Path(path, f"{m_date.year:04}")
                    if not folder.exists():
                        folder.mkdir()
                        self.log(None, folder)

                    # move file to the folder
                    target_path: Path = Path(folder, file.resolve().parts[-1])
                    file.move(target_path)
                    self.log(file, target_path)


        # organize after size
        if organization_type == Options.OrganizationTypes.Size:
            # check if value is valid
            if not isinstance(value, Options.SizeUnits):
                raise TypeError(f"Expected: {Options.SizeUnits}, got: {type(value)}")

            # get max_length for size
            max_length: int = 0
            for file in current_files:
                size: int = file.stat().st_size
                for _ in range(1 if value.value == "KB" else 2 if value.value == "MB" else 3 if value.value == "GB" else 4):
                    size = floor(size / 1024)

                if len(f"{size}" > max_length):
                    max_length = len(f"{size}")


            # move current files to the correct folders
            for file in current_files:
                # get size of the file
                size: int = file.stat().st_size
                for _ in range(1 if value.value == "KB" else 2 if value.value == "MB" else 3 if value.value == "GB" else 4):
                    size = floor(size / 1024)

                # create the correct folder if it doesn't exist
                folder: Path = Path(path, f"{size:0{max_length}} {value.value}")
                if not folder.exists():
                    folder.mkdir()
                    self.log(None, folder)

                # move file to folder
                target_path: Path = Path(folder, file.resolve().parts[-1])
                file.move(target_path)
                self.log(file, target_path)



    def log(self, path_before: Path | None, path_after: Path | None, silent: bool = False) -> None:
        log_message: str = f"{path_before.resolve() if not path_before is None else "\\"} -> {path_after.resolve() if not path_after is None else "\\"}"
        print(log_message)
        with self.logs_path.open("a") as logs:
            logs.write(f"{log_message}\n")