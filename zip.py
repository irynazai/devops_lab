import argparse
import logging
import zipfile
import os
import errno
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


class Error(Exception):
    pass


def check_exist_folder(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
            logger.info('Create %s', path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                logger.error('Directory %s can\'t be created', path)
                raise


def archive(current_path, destination):
    dest = destination.with_name(destination.name + '.zip')
    if dest == current_path:
        raise Error(f'input: {dest} equal output.')
    elif dest.exists():
        raise Error(f'input: {dest} is exists.')
    logger.info('Write %s', dest)

    with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_STORED) as zipf:
        for f in _iteration(current_path):
            with f.open('rb') as b:
                data = b.read()
            p = str(f.relative_to(current_path.parent))
            logger.info('Add %s', p)
            zipf.writestr(p, data)


def _iteration(file):
    if file.is_file():
        yield file
    elif file.is_dir():
        yield from (t for t in file.rglob('*') if t.is_file())


def unzip(file, path):
    check_exist_folder(path)
    with zipfile.ZipFile(file, 'r', compression=zipfile.ZIP_STORED) as zipf:
        try:
            zipf.extractall(path)
            logger.info('Unzipped to %s', path)
        except KeyError:
            logger.error('Can\'t unzipped to %s', path)


def rmdir(dir):
    try:
        shutil.rmtree(dir)
    except OSError as e:
        logger.error(f'Error: {dir} : {e.strerror}')


# Deletes all subdirectories if there is no __init__.py file in the current directory.
def delete_dir_without_initfile(path):
    for dirpath, dirnames, files in os.walk(path):
        if dirpath != path:
            count = 0
            for file_name in files:
                if file_name == '__init__.py':
                    count += 1
            if count == 0:
                rmdir(dirpath)
                logger.info('Directory without __init__.py was deleted %s', path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('zip', help="Name/s of zip file/s separated by space", type=Path, nargs='+')
    args = parser.parse_args()
    temp_path = '/tmp'

    for z in args.zip:
        try:
            unzip(z, temp_path)
        except Error as e:
            logger.warning(f'{e} skipped.')

        unzip_path = temp_path + '/' + str(z.with_name(z.name))[:-4]
        delete_dir_without_initfile(temp_path + '/' + str(z.with_name(z.name))[:-4])

    for p in args.zip:
        unzip_path = temp_path + '/' + str(p.with_name(p.name))[:-4]
        try:
            archive(Path(unzip_path), p)
        except Error as e:
            logger.warning(f'{e} skipped.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
