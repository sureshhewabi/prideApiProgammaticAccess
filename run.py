import accesspride as pride


# User parameters
output_dir = '/Users/hewapathirana/Downloads/PrideData/'
download_mode = 'aspera'
aspera_program = '/Users/hewapathirana/Applications/AsperaCLI/etc/asperaweb_id_dsa.openssh'
file_types = ['RESULT', 'PEAK']
file_resources = ['SUBMITTED']
file_extensions = [".mzid", ".mzid.gz", ".mgf", ".mgf.gz"]
project_accessions = ["PXD000664"]

projects = pride.retrieveProjectList()
for project in projects:
    if project["submissionType"] == "COMPLETE" and project["numAssays"] <3:
        project_accession = project['accession']
        print ("------------------" + project_accession + "------------------")
        project_files = pride.retrieveFiles(project_accession)
        # pride.printProjectFiles(project_files)
        selected_files = pride.filterFiles(project_files, file_types, file_resources, file_extensions)
        for file in selected_files:
            pride.downloadFilesByAspera(file["asperaDownloadLink"], output_dir + project['accession'], aspera_program)
        pride.extractGzippedFiles(output_dir + project['accession'])
