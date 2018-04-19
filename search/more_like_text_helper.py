import elasticsearch

from django.conf import settings

from regulations.models import Regulation

def clean_text(text):
    text = text.lower()
    cleaned_text = []
    for word in text.split(' '):
        if len(word) > 2:
            cleaned_text.append(word)
    return ' '.join(cleaned_text)

def more_like_text(text):
    conn = elasticsearch.Elasticsearch(
        settings.HAYSTACK_CONNECTIONS['default']['URL'],
        )

    mlt_query = {
        'query': {
            "dis_max": {
                "queries": [
                    {
                        'more_like_this': {
                            'fields': ['title', 'text'],
                            'like_text': clean_text(text),
                            'min_term_freq': 1,
                            'min_doc_freq': 2,
                            'max_query_terms': 30,
                            'min_word_length': 3,
                        }
                    },
                    {
                        'more_like_this': {
                            'fields': ['text'],
                            'like_text': " ".join(text.split(' ')[:50]),
                            'min_term_freq': 1,
                            'min_doc_freq': 1,
                            'boost': 40,

                        }
                    }
                ]
            }
        },
        "highlight" : {
              "pre_tags": ["<mark>"],
              "post_tags": ["</mark>"],
                "fields" : {
                    "text" : {"fragment_size" : 150, "number_of_fragments" : 1},
                    "title" : {"fragment_size" : 150, "number_of_fragments" : 1},

                }
            }
    }

    res = conn.search(
        body=mlt_query,
        index=settings.HAYSTACK_CONNECTIONS['default']['INDEX_NAME'],
    )
    for hit in res.get('hits', {}).get('hits', []):
        if hit['_id'].startswith('regulations.regulation.'):
            model = Regulation.objects.get(pk=hit['_id'].split('.')[-1])
            hit['model'] = model
    return res
