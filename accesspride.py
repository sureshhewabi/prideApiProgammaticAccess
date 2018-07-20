#!/usr/bin/env python3

# ---------------------------------------------
# Author: Suresh Hewapathirana
# Usage: python3 downloadPrideFiles.py
# Prerequisite: Python3
# ---------------------------------------------

import requests
import json
import os
from subprocess import call

BASE_URL = 'https://www.ebi.ac.uk/pride/ws/archive/'
PROJECT_FILE_LIST = '/file/list/project/'
PROJECT_LIST = '/project/list'


def downloadFilesByFTP(link, output_dir):
    """
    Downloads the given file in Aspera or FTP mode
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    call(["curl", "--silent", link, "-o", output_dir])


def downloadFilesByAspera(link, output_dir, aspera_program):
    """
    Downloads the given file in Aspera or FTP mode
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    call(["ascp", "-TQ", "-l200m", "-P", "33001", "-i", aspera_program, link, output_dir])


def retrieveFiles(project_accession):
    """
    Get the list of file in the submission and filter out the files that are interested
    """

    target = BASE_URL + PROJECT_FILE_LIST + project_accession
    response = requests.get(target)
    result = json.loads(response.content)
    return result['list']


def retrieveProjectList():
    """
    Get the list of file in the submission and filter out the files that are interested
    """

    target = BASE_URL + PROJECT_LIST + "?show=100"
    response = requests.get(target)
    result = json.loads(response.content)
    return result['list']


def filterFiles(files, file_types, file_resources, file_extensions):
    selected_files = []
    for file in files:
        if file['fileType'] in file_types and file['fileSource'] in file_resources and file['fileName'].lower().endswith(tuple(file_extensions)):
            selected_files.append(file)
    return selected_files


def extractGzippedFiles(output_dir):
    """
    Extract all the GZ compressed files(with .gz extension) in the output directory
    """
    call(["gunzip", output_dir + "/"])

def printProjectFiles(project_files):
    for project_file in project_files:
        # for testing purpose
        if(project_file["fileType"] == "PEAK" or project_file["fileType"] == "RESULT"):
            print("%s\t%s" % (project_file["fileType"], project_file['asperaDownloadLink']))