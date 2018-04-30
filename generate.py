import random
import time
from solr import Solr

ONE_BILLION = 1000000000
HUNDRED_MILLION = 100000000
TEN_MILLION = 10000000
ONE_MILLION = 1000000
HUNDRED_THOUSAND = 100000
ONE_THOUSAND = 1000
TEN = 10

NUMBER_OF_DOCS = ONE_MILLION

SOLR_URL = "http://localhost:8983/solr/"
SOLR_CORE = "payloads"
ID_KEY = "id"
CLASSIFICATIONS_KEY = "classifications_dpf"
AWESOME_NUMBER_KEY = "awesome_number"
keys = [ID_KEY, CLASSIFICATIONS_KEY]

classes = [
    "first_classifier:class_one",
    "first_classifier:class_two",
    "first_classifier:class_three",
    "first_classifier:class_four",
    "second_classifier:class_one",
    "second_classifier:class_two"
]

solr = Solr("{0}{1}".format(SOLR_URL, SOLR_CORE))


def create_doc(j):
    return {
        ID_KEY: "document.{0}".format(str(j)),
        CLASSIFICATIONS_KEY: list(("{0}|{1}".format(str(j), str(round(random.uniform(0, 1), 2))) for j in classes)),
        AWESOME_NUMBER_KEY: round(random.uniform(0, 1), 2)
    }


def add_to_solr(docs):
    solr.add_many(docs, commit=True)


def get_chunk_time_log(chunk_size, chunk_start_time, local_time, start_time):
    return "{0} docs, diff {1} seconds, total {2} seconds" \
        .format(chunk_size, (local_time - chunk_start_time), (local_time - start_time))


def chunk_ready(chunk_size):
    return chunk_size != 0 and (chunk_size == NUMBER_OF_DOCS
                                or (NUMBER_OF_DOCS / 100 < 100 and chunk_size % 100 == 0)
                                or (chunk_size % (NUMBER_OF_DOCS / 100) == 0))


def process_chunk(chunk_size, docs, chunk_start_time, start_time):
    local_time = time.time()
    print(get_chunk_time_log(chunk_size, chunk_start_time, local_time, start_time))
    add_to_solr(docs)
    return [], time.time()


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
