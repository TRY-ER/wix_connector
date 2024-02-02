from wix_connector.URLs.base import BaseUrl



InsertDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items",
 description="""
    Adds an item to a collection.

    An item can only be inserted into an existing connection. You can create a new collection using the Data Collections API.

    When an item is inserted into a collection, the item's ID is automatically assigned a random value. You can optionally provide a custom ID in dataItem.id when inserting the item. If you specify an ID that already exists in the collection, the insertion will fail.

    If dataItem.data is empty, a new item is created with no data fields.
""",
 example="""{
    "dataCollectionId": "cities",
    "dataItem": {
        "data": {
            "state": "California",
            "year": 2022,
            "city": "Los Angeles",
            "population": 3800000
        }
    }
    }""",
    request_type="POST"
)

UpdateDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items/{}",
 description="""
   Updates an item in a collection.

    This endpoint replaces the data item's existing data with the payload provided in dataItem.data in the request.

    To update an item, you need to specify an item ID and a collection ID. If an item is found in the specified collection with the specified ID, that item is updated. If the collection doesn't contain an item with that ID, the request fails.

    When an item is updated, its data._updatedDate field is changed to the current date and time. 
 """,
 example="""{
    "dataCollectionId": "cities",
    "dataItem": {
        "data": {
            "state": "California",
            "year": 2022,
            "city": "Los Angeles",
            "population": 3800000
        }
    }
}""",
    request_type="PUT"
)

SaveDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items/save",
 description="""
   Inserts or updates an item in a collection.

    The Save Data Item endpoint inserts or updates the specified item, depending on whether it already exists in the collection.

    If you don't provide an ID, a new item is created.

    If you provide an ID that does not exist in the collection, a new item is created with that ID.

    If an item with the ID you provide already exists in the collection, that item is updated. When an item is updated, its data._updatedDate field is changed to the current date and time. 
 """,
 example="""{
    "dataCollectionId": "cities",
    "dataItem": {
        "data": {
            "state": "California",
            "year": 2022,
            "city": "Los Angeles",
            "population": 3800000
        }
    }
    }""",
    request_type="POST"
)

GetDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items/{}",
 description="""
   Retrieves an item from a collection. 
 """,
 example="""As it's a get response you will just pass the id. There will be no body""",
    request_type="GET"
)

RemoveDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items/{}",
 description="""
 Removes an item from a collection.

If any items in other collections reference the removed item in reference or multi-reference fields, those fields are cleared.
 """,
 example="""Just id is given in the URL hence no exmaple of body""",
 request_type="DELETE"
)

QueryDataUrl= BaseUrl(
 url="https://www.wixapis.com/wix-data/v2/items/query",
 description="""
Retrieves a list of items, on the basis of the filtering, sorting, and paging preferences you provide. 
 """,
 example="""
    for normal simple query
    {
    "dataCollectionId": "cities",
    "query": {
        "filter": {
            "state": "California"
        },
        "paging": {
            "limit": 2
        }
    }
    }

    query for specific field and sorting
    
    {
    "dataCollectionId": "cities",
    "query": {
        "filter": {
            "state": "California"
        },
        "sort": [
            {
                "fieldName": "population",
                "order": "ASC"
            }
        ],
        "paging": {
            "limit": 2
        },
        "fields": ["population"]
    },
    "returnTotalCount": true
    } 
    """,
 request_type="POST"
)

