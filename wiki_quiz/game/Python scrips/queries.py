countries = {
    "capital" :
    """
    SELECT ?country ?capital 
        WHERE {
            ?country dbo:capital ?capital .
            ?country dbo:countryCode ?code .
            FILTER NOT EXISTS {?country dbp:dateEnd ?date}
        }
    """,
    "population":
    """
    
    """
}
