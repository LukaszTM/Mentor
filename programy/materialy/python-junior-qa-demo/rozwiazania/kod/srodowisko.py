import importlib.util
import sys

print("Python:", sys.version_info.major, sys.version_info.minor)
for nazwa in ["pytest", "requests", "selenium", "flask"]:
    jest = importlib.util.find_spec(nazwa) is not None
    print(nazwa, "OK" if jest else "BRAK")
