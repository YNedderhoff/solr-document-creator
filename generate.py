import time

from configs import NUMBER_OF_DOCS
from modules.documents import create_doc
from modules.processing import chunk_ready, process_chunk


def run():
    start_time = time.time()
    chunk_start_time = time.time()
    docs = []

    for i in range(1, NUMBER_OF_DOCS + 1):
        docs.append(create_doc(i))
        if chunk_ready(i):
            docs, chunk_start_time = process_chunk(i, docs, chunk_start_time, start_time)

    print("--- {0} seconds ---".format(time.time() - start_time))


if __name__ == '__main__':
    run()
