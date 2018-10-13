from configparser import ConfigParser

def get_ini():
    config = ConfigParser()
    config.read('bkp.ini')
    backup_params = config['backup']
    source_dirs = [x.strip() for x in backup_params['source'].split(',;:')]
    dest_dirs   = [x.strip() for x in backup_params['dest'].split(',;:')]
    return {'source_dirs': source_dirs,
            'dest_dirs'  : dest_dirs}



