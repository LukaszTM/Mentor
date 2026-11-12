# -*- mode: python ; coding: utf-8 -*-
# PyInstaller: pyinstaller mentor.spec  →  dist/Mentor.exe (jeden plik, bez konsoli)
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(
    ["mentor.py"],
    pathex=["."],
    binaries=[],
    datas=[
        ("programy/python-junior-qa.json", "programy"),
        ("programy/kadry-i-place.json", "programy"),
        ("programy/szablon-programu.json", "programy"),
        ("programy/FORMAT.md", "programy"),
        ("mentor.ico", "."),
    ],
    hiddenimports=["asystent", "program", "motywy", "wiedza_ogolna", "tkinter", "tkinter.ttk", "tkinter.font", "tkinter.filedialog",
                   "tkinter.messagebox", "tkinter.simpledialog"],
    hookspath=[],
    runtime_hooks=[],
    excludes=["PIL", "numpy", "matplotlib", "pytest", "selenium", "requests", "flask", "pandas"],
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="Mentor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon="mentor.ico",
    version="wersja.txt",
)
