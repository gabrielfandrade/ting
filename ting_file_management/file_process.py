from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    if not any(_process['nome_do_arquivo'] == path_file for _process in instance._queue):
        process_dict = dict()

        lines = txt_importer(path_file)

        process_dict['nome_do_arquivo'] = path_file
        process_dict['qtd_linhas'] = len(lines)
        process_dict['linhas_do_arquivo'] = lines

        instance.enqueue(process_dict)

        print(process_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
