# ---------------
# COMMON
# ---------------

# python_version
def get_python_version():
    return '3.6.3'

# lock
lock_file_dir = ''
lock_file_name = 'sample.lock'

# log
log_config_file_name = 'log_config.ini'

# ssh
ssh_port = 22

# apps
bin_dir = 'bin'
src_dir = 'SAMPLE_PROJECT'
exec_user = 'ikuhiro'


CONSTANTS = {
    'DEFAULT': {
        'lock': {
            'FILE_DIR': lock_file_dir,
            'FILE_NAME': lock_file_name
        },
        'log': {
            'config_file_name': log_config_file_name
        },
        'ssh': {
            'USER_NAME': 'sample_user',
            'PASSWORD': 'sample_pass',
            'PORT': ssh_port
        },
        'apps': {
            'BIN_DIR': bin_dir,
            'SRC_DIR': src_dir,
            'EXEC_USER': exec_user
        },
    },
    'DEV': {

    },
    'PRODUCTION': {

    }
}
