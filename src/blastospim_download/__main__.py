import zipfile
import gdown
import os
import tarfile
import requests, io

def main():
    ## Download early model
    r = requests.get("https://blastospim.flatironinstitute.org/html/early_embryo_model.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('.')

    ## Download late model
    r = requests.get("https://blastospim.flatironinstitute.org/html/late_blastocyst_model.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('.')

    ## Download the Test Data
    test_data_url = "https://drive.google.com/uc?id=1nsyIaZQ6HnAWD7YH-jkRBPfoEPfY9urg"
    output_zip = 'toy_data_v1.1.tgz'
    gdown.download(test_data_url, output_zip, quiet=False)
    test_data_file = tarfile.open(output_zip)
    # extracting file
    test_data_file.extractall('.')
    test_data_file.close()
    os.remove(output_zip)



