import shutil

# Caminho da pasta que você quer zipar
folder_to_zip = "../data"

# Nome do arquivo zip final (sem .zip)
output_filename = "data_files"

# Cria o zip
shutil.make_archive(output_filename, 'zip', folder_to_zip)

print("ZIP criado com sucesso:", output_filename + ".zip")
