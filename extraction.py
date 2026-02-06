import zipfile


# with zipfile.ZipFile("unzip_me_for_instructions.zip", "r") as zip_ref:
#     zip_ref.extractall("extracted_folder")

# print("Files extracted!")

with open("/Users/kokumar/Desktop/python practice/extracted_folder/extracted_content/Instructions.txt", "r") as file:
    print(file.read())
   
