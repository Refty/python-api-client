from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class AddSearchSynonym(Request):
    """
    Adds a new synonym for the [Search items](https://docs.recombee.com/api.html#search-items).
    
    When the `term` is used in the search query, the `synonym` is also used for the full-text search.
    Unless `oneWay=true`, it works also in the opposite way (`synonym` -> `term`).
    
    An example of a synonym can be `science fiction` for the term `sci-fi`.
    
    Required parameters:
    
    :param term: A word to which the `synonym` is specified.
    
    :param synonym: A word that should be considered equal to the `term` by the full-text search engine.
    
    
    Optional parameters:
    
    :param one_way: If set to `true`, only `term` -> `synonym` is considered. If set to `false`, also `synonym` -> `term` works.
    
    
    Default: `false`.
    
    

    """

    def __init__(self, term, synonym, one_way=DEFAULT):
        self.term = term
        self.synonym = synonym
        self.one_way = one_way
        self.timeout = 10000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/synonyms/items/" % ()

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['term'] = self.term
        p['synonym'] = self.synonym
        if self.one_way is not DEFAULT:
            p['oneWay'] = self.one_way
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
