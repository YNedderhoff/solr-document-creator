import time
import requests

from configs import SOLR_DOMAIN, SOLR_COLLECTION
from modules.queries import non_payload_queries, payload_queries

BASIC_SELECT_REQUEST_URL = "http://{0}/solr/{1}/select?".format(SOLR_DOMAIN, SOLR_COLLECTION)
EXECUTIONS_PER_QUERY = 10
OUTFILE_MESSAGE = "Calculating the average execution times of {0} requests per query\n".format(EXECUTIONS_PER_QUERY)


def measure(query, number_of_executions, f):
    successful_queries = 0
    non_successful_queries = 0
    sum_of_times = 0.0
    first_time = 0.0
    full_request = "{0}{1}".format(BASIC_SELECT_REQUEST_URL, query)
    for i in range(0, number_of_executions):
        start_time = time.time()
        response = requests.request("GET", full_request)
        if response.status_code is 200:
            successful_queries += 1
            execution_time = time.time() - start_time
            sum_of_times += execution_time
            if i == 0:
                first_time = execution_time
        else:
            non_successful_queries += 1
    print("{0} ({1} successful, {2} non-successful)\n".format(query, successful_queries, non_successful_queries))
    f.write("{0} ({1} successful, {2} non-successful)\n".format(query, successful_queries, non_successful_queries))
    f.write(
        "\t{0}\tseconds (first)\n\t{1}\tseconds (average)\n".format(first_time, sum_of_times / EXECUTIONS_PER_QUERY))


def run():
    with open('outfile_non_payloads', 'a') as f:
        f.write(OUTFILE_MESSAGE + "\n##### non-payload queries #####\n")
        for query in non_payload_queries:
            measure(query, EXECUTIONS_PER_QUERY, f)
    with open('outfile_payloads', 'a') as f:
        f.write(OUTFILE_MESSAGE + "\n##### payload queries #####\n")
        for query in payload_queries:
            measure(query, EXECUTIONS_PER_QUERY, f)


if __name__ == '__main__':
    run()
