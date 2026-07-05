from datetime import datetime
from math import floor
from pathlib import Path

from options import Options
from file_organizer import FileOrganizer

fo = FileOrganizer()
fo.organize(Path("test_dir"), Options.OrganizationTypes.Size, Options.SizeUnits.KB)