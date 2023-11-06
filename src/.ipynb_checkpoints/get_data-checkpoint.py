"""
Download and extract data.
"""
import urllib.request
import zipfile
import os
file = os.path.dirname(os.path.abspath(__file__))


URL = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
# URL = 'https://surfdrive.surf.nl/files/index.php/s/WCPP8WJPrtCbUO5/download'
EXTRACT_DIR = "dataset"

zip_path, _ = urllib.request.urlretrieve(URL)
with zipfile.ZipFile(file + "dataset/smsspamcollection.zip", "r") as f:
    f.extractall(EXTRACT_DIR)
