#We seperate results based on difficulties, we use order to get these difficulties so that easier awnser are at the top

queries = {
    #Geography queries:

    "capital" :
        """
            SELECT DISTINCT ?country ?capital ?pop
                WHERE {
                    ?country rdf:type dbo:Country .
                    ?country dbo:countryCode ?code .
                    ?country dbo:capital ?capital .
                    ?country dbp:areaKm ?area .
                    ?country dbo:populationTotal ?pop .
                    FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
                order by desc (?pop)
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
                order by desc (?population)
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
                order by desc (?area)
        """,

    "currency":
        """
            select distinct ?currencyCode ?country ?population ?currency 
            WHERE {
                ?country rdf:type dbo:Country .
                ?country dbo:countryCode ?code .
                ?country dbo:capital ?capital .
                ?country dbo:populationTotal ?population .
                ?country dbo:currency ?currency .
                ?country dbo:currencyCode ?currencyCode .
                FILTER NOT EXISTS {?country dbp:dateEnd ?date}
                FILTER NOT EXISTS {?country dbp:yearEnd ?year}
            }  order by desc(?population)
        """,
    
    "island": 
        """
            SELECT DISTINCT ?country ?island 
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
    #Some mountains missing height, uses regex on ranking to get 100 highest mountains
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
            } order by desc(?height)
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
            order by desc (?olympic)
        """,
    
    # Limited to middle east and Nordic due to query time out:
    "country_neighbours":
        """
            SELECT ?startLabel ?middleLabel ?endLabel ?pop 
            WHERE {
                ?border wdt:P31 wd:Q15104814 ;
                        wdt:P17 ?start , ?middle .
                {?start wdt:P361 wd:Q7204.} UNION {?start wdt:P361 wd:Q52062.}
                ?border2 wdt:P31 wd:Q15104814 ;
                        wdt:P17 ?middle , ?end .
                ?end wdt:P1082 ?pop
                FILTER (?start != ?middle)
                FILTER (?start != ?end)
                FILTER (?middle != ?end)
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }order by desc(?pop)
        """,
    
    "largest_citys":
        """
            SELECT DISTINCT ?cityLabel ?population
            WHERE {
                SERVICE wikibase:label {bd:serviceParam wikibase:language "en" .}
                ?city wdt:P31/wdt:P279* wd:Q515 .
                ?city wdt:P1082 ?population .
            }
            ORDER BY DESC(?population)
            LIMIT 1000
        """,
    
    "land_locked": 
        """
            SELECT ?countryLabel ?locked ?pop WHERE {
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                ?country wdt:P31 wd:Q6256;
                         wdt:P1082 ?pop.
                OPTIONAL {?country wdt:P31 wd:Q123480.}
                BIND (exists{?country wdt:P31 wd:Q123480.} AS ?locked)
            }order by desc(?pop)
        """,





    # Movie queries:


    #Duplicate movies for movies with multiple directors
    "director":
        """
            SELECT DISTINCT  ?directorLabel ?movieLabel (count(?movie) as ?count) 
            WHERE {
                ?movie wdt:P31 wd:Q11424.
                ?movie wdt:P57 ?director.
                ?movie wdt:P166 ?award.
                ?award wdt:P31 wd:Q19020.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            group by ?directorLabel ?movieLabel
            order by desc(?count)
        """,

    "movie_length": 
        """
            SELECT DISTINCT ?lengthLabel ?movieLabel (count(?movie) as ?count) 
            WHERE {
                ?movie wdt:P31 wd:Q11424.
                ?movie wdt:P2047 ?length.
                ?movie wdt:P166 ?award.
                ?award wdt:P31 wd:Q19020.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            group by ?lengthLabel ?movieLabel
            order by desc(?count)
        """,
    
    "academy_awards_movie":
        """
            SELECT (count(?movie) as ?count)  ?movieLabel
            WHERE {
                ?movie wdt:P31 wd:Q11424.
                ?movie wdt:P166 ?award.
                ?award wdt:P31 wd:Q19020.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            group by ?movieLabel
            order by desc(?count)
        """,

    "academy_awards_person":
        """
            SELECT (count(?actor) as ?count) ?actorLabel
            WHERE {
                ?actor wdt:P31 wd:Q5.
                ?actor wdt:P166 ?award.
                ?award wdt:P31 wd:Q19020.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            group by ?actorLabel
            order by desc(?count)
        """,
    
    #Filters by strlen so that we get movies with more than one actor.
    "actors":
        """
            SELECT ?movieLabel ?actors WHERE {
                {SELECT DISTINCT ?movieLabel (GROUP_CONCAT(?actorLabel;separator=",") as ?actors)  
                WHERE {
                    SELECT ?movieLabel ?actorLabel 
                    WHERE {
                        ?movie wdt:P31 wd:Q11424.
                        ?movie wdt:P166 ?award.
                        ?award wdt:P31 wd:Q19020.
                        ?movie wdt:P161 ?actor.
                        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                    }
                } GROUP BY ?movieLabel}
            filter(strlen(?actors) > 24)
            }
        """,

    "release_year":
        """
            SELECT DISTINCT (SAMPLE(year(?release)) as ?year) ?movieLabel (count(?movie) as ?count) 
            WHERE {
                ?movie wdt:P31 wd:Q11424.
                ?movie wdt:P577 ?release.
                ?movie wdt:P166 ?award.
                ?award wdt:P31 wd:Q19020.
                SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            group by ?movieLabel
            order by desc(?count)
        """,
    
    #binds the variable bool to true or false depending if an actors parent is also an actor
    "actor_has_actor_parent":
        """ 
            SELECT DISTINCT ?actorLabel ?bool (count(?actor) as ?count)
                WHERE {
                    ?actor wdt:P31 wd:Q5 ; 
                        wdt:P106 wd:Q33999 ; 
                        wdt:P166 ?award ;
                        wdt:P22 ?parent .
                    ?award wdt:P31 wd:Q19020.
                    ?parent wdt:P31 wd:Q5.
                    BIND(EXISTS{?parent wdt:P106 wd:Q33999} as ?bool)
                    
                    SERVICE wikibase:label {bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".}
                }group by ?actorLabel ?bool
                order by desc (?count)
        """
}