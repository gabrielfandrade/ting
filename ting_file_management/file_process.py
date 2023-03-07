import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    if not any(p['nome_do_arquivo'] == path_file for p in instance._queue):
        file_dict = dict()

        lines = txt_importer(path_file)

        file_dict['nome_do_arquivo'] = path_file
        file_dict['qtd_linhas'] = len(lines)
        file_dict['linhas_do_arquivo'] = lines

        instance.enqueue(file_dict)

        print(file_dict)


def remove(instance: Queue):
    if len(instance) > 0:
        file = instance.dequeue()

        path_file = file['nome_do_arquivo']

        print(f'Arquivo {path_file} removido com sucesso')
    else:
        print('Não há elementos')


def file_metadata(instance: Queue, position: int):
    try:
        file = instance.search(position)

        print(file)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
