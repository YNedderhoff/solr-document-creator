from solrcloudpy.connection import SolrConnection

from configs import SOLR_COLLECTION, SOLR_DOMAIN

SOLR = SolrConnection(SOLR_DOMAIN, version="7.2.1")


def add_to_solr(docs):
    SOLR[SOLR_COLLECTION].add(docs)
    SOLR[SOLR_COLLECTION].commit()
