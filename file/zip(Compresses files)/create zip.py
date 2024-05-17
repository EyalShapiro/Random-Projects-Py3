from tqdm import tqdm

import zipfile
import sys

# the password list path you want to use
# wordlist = sys.argv[2]
wordlist = 'x.txt'
# the zip file you want to crack its password
zip_file = 't.zip'
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file, 'x')
zip_file.filename()
print('create zip')
zip_file.close()
