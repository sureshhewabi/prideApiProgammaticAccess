#!/usr/bin/env python3

#---------------------------------------------
# Author: Suresh Hewapathirana
# Usage: python3 downloadPrideFiles.py
# Prerequisite: Python3
#---------------------------------------------

import requests
import json
from subprocess import call

base_uri = 'https://www.ebi.ac.uk/pride/ws/archive/'

def downloadFiles(download_mode, link):
    """
    Downloads the given file in Aspera or FTP mode
    """

    if download_mode == 'aspera':
        call(["ascp", "-TQ", "-l200m", "-P", "33001", "-i", aspera_program, link, output_dir])
    else:
        call(["curl", "--silent", link])
        return

def retrieveFiles(project_accession):
    """
    Get the list of file in the submission and filter out the files that are interested
    """

    print ("------------------ Downloading " + project_accession + "------------------")
    path = '/file/list/project/'
    target = base_uri + path + project_accession
    print ("Requesting :" + target)
    response = requests.get(target)

    selected_file_types = ['RESULT', 'PEAK']
    selected_file_resources = ['SUBMITTED']

    # Parse JSON
    result = json.loads(response.content)
    for file in result['list']:
        if(file['fileType'] in selected_file_types and file['fileSource'] in selected_file_resources):
            link = file['asperaDownloadLink'] if download_mode == 'aspera' else file['downloadLink']
            downloadFiles(download_mode, link)

def extractGzippedFiles():
    """
    Extract all the GZ compressed files(with .gz extension) in the output directory
    """
    call(["gunzip", output_dir + "*.gz"])
