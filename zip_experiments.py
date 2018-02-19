import os
import zipfile
from sbhs_server import settings

# experiments_dir = settings.EXPERIMENT_LOGS_DIR

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root,file))

if __name__ == '__main__':
    if os.path.exists('Experiments.zip'):
        os.remove('Experiments.zip')
    zipf = zipfile.ZipFile('Experiments.zip','w',zipfile.ZIP_DEFLATED)
    zipdir('experiments/',zipf)
    zipf.close()
