# Country queries:

queries = {
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
    #Some mountains missing height
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
    
    "country_neighbours":
        """
            SELECT ?start_countryLabel ?middle_countryLabel ?end_countryLabel ?pop 
            WHERE {
                filter(?start_country = wd:Q183)
                ?border wdt:P31 wd:Q15104814 ;
                        wdt:P17 ?start_country , ?middle_country .
                ?border2 wdt:P31 wd:Q15104814 ;
                        wdt:P17 ?middle_country , ?end_country .
                ?end wdt:P1082 ?pop
                FILTER (?start_country != ?middle_country)
                FILTER (?start_country != ?end_country)
                FILTER (?middle != ?end_country)
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
    
    "actors":
        """
            SELECT DISTINCT ?movieLabel (GROUP_CONCAT(?actorLabel;separator=",") as ?actors)  
            WHERE {
                SELECT ?movieLabel ?actorLabel WHERE {
                    ?movie wdt:P31 wd:Q11424.
                    ?movie wdt:P166 ?award.
                    ?award wdt:P31 wd:Q19020.
                    ?movie wdt:P161 ?actor.
                    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                }
            } GROUP BY ?movieLabel
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