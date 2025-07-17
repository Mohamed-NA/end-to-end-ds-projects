import os, shutil, platform, datetime

source = r"D:\ettbtm\Work\konecta\Internship"
target = r"D:\ettbtm\Work\konecta\Internship\hands-on\automation"
extensions = {item.split('.')[-1] for item in os.listdir(source) if os.path.isfile(os.path.join(source, item))}

def copy_by_date(source, target, exts = extensions):

    def get_folder(year, month):
        """
        Gets the folders name that is supposed to be with that timestamp
        """
        month_map = {
            1: "01 Jan", 2: "02 Feb", 3: "03 Mar", 4: "04 Apr",
            5: "05 May", 6: "06 Jun", 7: "07 Jul", 8: "08 Aug",
            9: "09 Sep", 10: "10 Oct", 11: "11 Nov", 12: "12 Dec"
        }
        return f"{year}/{month_map.get(month, 'Unknown')}"
        
    def get_creation_date(path_to_file):
        """
        Get creation date (or fallback to last access time)
        """
        if platform.system() == 'Windows':
            timestamp = os.path.getatime(path_to_file)
        
        else:
            stat = os.stat(path_to_file)
            try:
                timestamp = stat.st_birthtime
            except AttributeError:
                #This means we are probably on linux. So we settle 
                #for last modified date
                timestamp = stat.st_atime
        #Formatting timestapm to match our desired timestamp
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.strftime("%d/%m/%Y, %H:%M:%S"), dt.year, dt.month

    def do_copy():
        files = os.listdir(source)
        for file in files:
            source_file_path = os.path.join(source, file)
            if os.path.isfile(source_file_path):
                # Get date info for each file individually
                _, year, month = get_creation_date(source_file_path)
                
                # Build folder path based on date
                folder = get_folder(year, month)
                target_folder = os.path.join(target, folder)
                
                # Ensure the target folder exists
                os.makedirs(target_folder, exist_ok=True)

                # Set target file path (inside the correct folder)
                target_file_path = os.path.join(target_folder, file)
                
                if not os.path.exists(target_file_path):
                    shutil.copy2(source_file_path, target_file_path)
                    print(f"Copied file: {file} ➝ {target_folder}")
                else:
                    print(f"File already exists: {file}")
                    
    do_copy()
    

def copy_by_ext(source, target):
    
    def create_folder(target ,file_extension):
        """
        Creates a folder for said file extension if not existing in path
        """
        target_folder_path = os.path.join(target, file_extension)
        os.makedirs(target_folder_path, exist_ok=True)
        return target_folder_path
    
    def do_copy():
        """
        #Excutes the copy action
        """
        files = os.listdir(source)
        
        for file in files:
            source_file_path = os.path.join(source, file) 
            
            if os.path.isfile(source_file_path):
                file_extension = file.split('.')[-1]
                
                target_folfer_path = create_folder(target, file_extension)
                target_file_path = os.path.join(target_folfer_path, file)
                
                if not os.path.exists(target_file_path):
                    shutil.copy2(source_file_path, target_file_path)
                    print(f"Copied: {file} → {file_extension}/")
                else:
                    print(f"Skipped (already exists): {file}")
            else: 
                continue
                    
    do_copy()

#copy_by_date(source, target)
copy_by_ext(source, target)