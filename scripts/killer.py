import subprocess

scripts = ["scraper.py", "storage.py", "analytics.py", "visualization.py", "test.py"]

for script in scripts:
    subprocess.run(
        ["taskkill", "/F", "/IM", "python.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
