1. Extract the zip file manually to data/raw/unzipped

2. To setup python env
```
make setup
make clean-data
```
3. Call engine with `make run query="water"`




## How to call search engine functionality

```
python src/main-search-engine.py --query "mine water"
```

the response should look like this (results are ranked), 10 options.

Results are sorted, the first elementh is the one with HIGHEST RANKING SCORE.

```
{ "results" :[{"document_name" : "example.pdf", #string
               "document_path" : "path/to/dir", #string
               "document_type" : "pdf", #string can be "pdf" or "doc" or "docx"
               "ranking score" : 0.232, # float between 0 and 1
               },
            ....(more entries like the first one)...
            ]

}

```

In case of no results, the response will be

```
{ "results" :[]
}

```

