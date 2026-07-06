from enum import Enum


class Options(Enum):
    class OrganizationTypes(Enum):
        cDate = "cDate"
        mDate = "mDate"
        Size = "size"
        Extension = "extension"

    class TimeUnits(Enum):
        Day = "d"
        Year = "y"

    class SizeUnits(Enum):
        KB = "KB"
        MB = "MB"
        GB = "GB"
        TB = "TB"