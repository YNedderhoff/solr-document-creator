QUERY_ALL = "q=*:*"
FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD = "fq={!frange%20l=0.7}payload(classifications_dpf,first_classifier:class_one)"
FILTERQUERY_AWESOME_NUMBER_ABOVE_THRESHOLD = "fq=awesome_number:%5B0.7+TO+1.0%5D"
FILTERQUERY_BY_AWESOME_MULTI_FIELD = "fq=awesome_multi_field:%22first_classifier:class_three%22"
FILTERQUERY_BY_CLASSIFICATIONS_FIELD = "fq=classifications_dpf:%22first_classifier:class_three%22"
FL_SINGLE_FIELD = "fl=id,class_one:payload(classifications_dpf,first_classifier:class_one)"
SORT_BY_AWESOME_STRING = "sort=awesome_string+desc"
SORT_BY_AWESOME_NUMBER = "sort=awesome_string+desc"
SORT_BY_ONE_PAYLOAD = "sort=payload(classifications_dpf,first_classifier:class_one)+desc"
SORT_BY_TWO_PAYLOADS = "sort=payload(classifications_dpf,first_classifier:class_one)+desc,payload(classifications_dpf,first_classifier:class_two)+asc"
FACET_QUERY_PAYLOADS = "facet.query=classifications_dpf:first_classifier\:class_one&facet=on"
FACET_QUERY_MULTI_FIELD = "facet.query=awesome_multi_field:first_classifier\:class_one&facet=on"
RESPONSE_FORMAT = "wt=json"
INDENT_ON = "indent=on"

non_payload_queries = [
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, FILTERQUERY_BY_AWESOME_MULTI_FIELD, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, FACET_QUERY_MULTI_FIELD, RESPONSE_FORMAT, INDENT_ON)
]

payload_queries = [
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, FILTERQUERY_BY_CLASSIFICATIONS_FIELD, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, FACET_QUERY_PAYLOADS, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}&{4}".format(QUERY_ALL, FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD, FL_SINGLE_FIELD, RESPONSE_FORMAT,
                                 INDENT_ON),
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, SORT_BY_ONE_PAYLOAD, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}".format(QUERY_ALL, SORT_BY_TWO_PAYLOADS, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}&{4}".format(QUERY_ALL, FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD, SORT_BY_ONE_PAYLOAD, RESPONSE_FORMAT,
                                 INDENT_ON),
    "{0}&{1}&{2}&{3}&{4}".format(QUERY_ALL, FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD, SORT_BY_TWO_PAYLOADS, RESPONSE_FORMAT,
                                 INDENT_ON),
    "{0}&{1}&{2}&{3}&{4}".format(QUERY_ALL, SORT_BY_TWO_PAYLOADS, FL_SINGLE_FIELD, RESPONSE_FORMAT, INDENT_ON),
    "{0}&{1}&{2}&{3}&{4}&{5}".format(QUERY_ALL, FILTERQUERY_PAYLOAD_ABOVE_THRESHOLD, SORT_BY_TWO_PAYLOADS,
                                     FL_SINGLE_FIELD, RESPONSE_FORMAT, INDENT_ON)
]
