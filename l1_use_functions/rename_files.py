import os
def rename_files():
    #(1) get file names from a folder
    img_path = "/Users/Azumka/workspace/udacity/CPFPython/l1_use_functions/prank"
    file_list = os.listdir(img_path)
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(img_path)
    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + filename)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
