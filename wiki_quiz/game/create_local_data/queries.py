queries = {
    "capital" :
        """
            SELECT DISTINCT ?country ?capital
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:capital ?capital .
                    ?country dbp:areaKm ?area .
                    ?country dbo:populationTotal ?pop .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
        """,

    "population":
        """
            SELECT DISTINCT ?country ?population 
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:capital ?capital .
                    ?country dbp:areaKm ?area .
                    ?country dbo:populationTotal ?population .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
        """,

    "area":
        """
            SELECT DISTINCT ?country ?area 
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:capital ?capital .
                    ?country dbp:areaKm ?area .
                    ?country dbo:populationTotal ?population .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
        """,

    "longitude":
        """
            SELECT DISTINCT ?country ?longitude 
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:populationTotal ?population .
                    ?country geo:long ?longitude .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
        """,

    "latitude":
        """
            SELECT DISTINCT ?country ?latitude 
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:populationTotal ?population .
                    ?country geo:long ?latitude .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
        """,

    "currency":
        """
            select distinct ?country ?currency ?currencyCode 
            WHERE {
                ?country rdf:type dbo:Country .
                ?country dbo:countryCode ?code .
                ?country dbo:capital ?capital .
                ?country dbo:currency ?currency .
                ?country dbo:currencyCode ?currencyCode .
                FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                FILTER NOT EXISTS {?country dbp:yearEnd ?year}
            } 
        """,
    
    "island": 
        """
            SELECT DISTINCT ?island ?country 
            WHERE {
                ?country dbo:countryCode ?code .
                ?island rdf:type yago:Island109316454.
                ?island dbp:areaKm ?area .
                ?island dbo:country ?country.
                FILTER NOT EXISTS {?island dbo:countryCode ?code}
                FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                FILTER NOT EXISTS {?country dbp:yearEnd ?year}
            }
            ORDER BY DESC (?area)
            LIMIT(100)
        """,

    "mountain": 
        """
            SELECT DISTINCT ?mountain ?height ?rank ?country 
            WHERE {
                ?mountain rdf:type schema:Mountain .
                OPTIONAL {?mountain dbp:elevationM ?height}.
                ?mountain dbo:mountainRange ?range.
                ?mountain dbp:elevationRef ?rank.
                FILTER regex(?rank, "Ranked")
                ?mountain dbo:locatedInArea ?country.
                ?country rdf:type dbo:Country.
            }
    """,

    "olympics":
        """
            select distinct ?country ?olympic 
            WHERE {
                ?games rdf:type dbo:Olympics.
                ?games dbo:games ?olympic .
                ?games dbp:venue ?country .
                ?country rdf:type dbo:Country .
                ?country dbo:countryCode ?code .
            } 
            order by (?olympic)
        """
    
    "country_neighbours":
    """
        SELECT ?Country ?CountryLabel ?Country3 ?Country3Label 
        WHERE {
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            ?Country wdt:P31 wd:Q6256.
            ?Country2 wdt:P31 wd:Q6256.
            ?Country3 wdt:P31 wd:Q6256.
            ?Country wdt:P47 ?Country2.
            ?Country2 wdt:P47 ?Country3.
            FILTER (?Country != ?Country3)
        }"
    """
}