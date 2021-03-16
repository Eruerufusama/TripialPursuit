countries = {
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
                    FILTER NOT EXISTS {?country dbp:yearEnd ?year
                }
            }
        """,
    "population":
        """
            SELECT DISTINCT ?country ?pop 
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
            }
        """
}
