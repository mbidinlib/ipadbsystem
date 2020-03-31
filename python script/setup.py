
import mysql.connector

from cx_Freeze import setup, Executable
setup(
    name = "shortlist",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os", "PIL", "sys", "tkinter"],
        'include_files': ['IPA_Logo.jpg'],
        'include_msvcr': True,
    }},
    executables = [Executable("shortlist.py",base="Win32GUI")]
    )
