from django.core.exceptions import ValidationError

from petstagram_last.core.utils import megabytes_to_bytes


def validate_file_less_than_5mb(fileobj):
    filesize=fileobj.file.size
    megabyte_limit=5.0
    if filesize>megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Максималният размер на файла може да е {megabyte_limit}')
        # raise ValidationError(f'Max file size is {megabyte_limit}MB')