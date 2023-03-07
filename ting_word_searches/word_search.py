from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    results = []

    for file in instance._queue:
        ocorrencias = []

        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                line_dict = {
                    'linha': index + 1
                }

                ocorrencias.append(line_dict)

        if ocorrencias:
            result = {
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': ocorrencias
            }

            results.append(result)

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
