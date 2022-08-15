import zipfile
with zipfile.ZipFile("zipfile.zip","r") as zip_ref:
    zip_ref.extractall("G:\Python-Program")