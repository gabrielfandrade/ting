import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()

    files = [
        {
            'nome_do_arquivo': 'teste1.txt',
            'qtd_linhas': 3,
            'linhas_do_arquivo': [
                'linha1',
                'linha2',
                'linha3',
            ],
        },
        {
            'nome_do_arquivo': 'teste2.txt',
            'qtd_linhas': 5,
            'linhas_do_arquivo': [
                'linha1',
                'linha2',
                'linha3',
                'linha4',
                'linha5',
            ],
        },
        {
            'nome_do_arquivo': 'teste3.txt',
            'qtd_linhas': 4,
            'linhas_do_arquivo': [
                'linha1',
                'linha2',
                'linha3',
                'linha4',
            ],
        },
    ]

    for file in files:
        queue.enqueue(file)

    assert len(queue) == 3
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 2

    dequeue_file = queue.dequeue()

    assert dequeue_file == files[0]

    search_file = queue.search(1)

    assert search_file == files[1]

    with pytest.raises(IndexError):
        queue.search(2)
