### **Python script to remove directories from the archive without "__init__.py" file**

#### Description:
*A script that removes from the zip archive all directories that do not have an "__init__.py" file and creates a new archive based on the original one.*

#### Requirements:
*You need to install next packages. Run command:*
- pip install argparse

#### How to use. Run command:
*If zip archive is in the current directory:*
- python <file>.zip (<file2>.zip <file3>.zip ...)

*If zip archive isn't in the current directory:*
- python /path_to_the_file/<file>.zip ...

*The new zip archive will be located in the directory where the original archive is located with name <original_archive_name.zip.*


