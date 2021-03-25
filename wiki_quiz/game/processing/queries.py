countrie_sqarql_querys = {
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
                    FILTER NOT EXISTS {?country dbo:administrativeCenter ?admin}
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
                    FILTER NOT EXISTS {?country dbo:administrativeCenter ?admin}
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year}
                }
    """,
    
    "island": 
        """
            SELECT DISTINCT ?island ?area ?country 
            WHERE {
                ?island rdf:type yago:Island109316454.
                ?island dbp:areaKm ?area .
                ?island dbo:country ?country.
                FILTER NOT EXISTS {?island dbo:countryCode ?code}
            }
            ORDER BY DESC (?area)
            LIMIT(100)
        """
}
