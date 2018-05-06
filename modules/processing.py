import time

from configs import NUMBER_OF_DOCS, NUMBER_OF_CHUNKS
from modules.helpers.solr_connector import add_to_solr


def get_chunk_time_log(chunk_size, chunk_start_time, local_time, start_time):
    return "{0} docs, diff {1} seconds, total {2} seconds" \
        .format(chunk_size, (local_time - chunk_start_time), (local_time - start_time))


def chunk_ready(chunk_size):
    return chunk_size != 0 and (chunk_size == NUMBER_OF_DOCS or (
            NUMBER_OF_DOCS / NUMBER_OF_CHUNKS < NUMBER_OF_CHUNKS and chunk_size % NUMBER_OF_CHUNKS == 0)
                                or (chunk_size % (NUMBER_OF_DOCS / NUMBER_OF_CHUNKS) == 0))


def process_chunk(chunk_size, docs, chunk_start_time, start_time):
    local_time = time.time()
    print(get_chunk_time_log(chunk_size, chunk_start_time, local_time, start_time))
    add_to_solr(docs)
    return [], time.time()
