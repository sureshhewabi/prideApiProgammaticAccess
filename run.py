import accesspride as pride


# User parameters
base_uri = 'https://www.ebi.ac.uk:443/pride/ws/archive'
output_dir = '/Users/hewapathirana/Downloads/PrideData'
download_mode = 'aspera'
aspera_program = '/Users/hewapathirana/Applications/AsperaCLI/etc/asperaweb_id_dsa.openssh'

project_accessions = ["PXD000664"]

for project_accession in project_accessions:
    pride.retrieveFiles(project_accession)
