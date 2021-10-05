# **Querying and Pagination Tutorial**

## Let's get started

This tutorial first will show you how to send simple search query to the Retail Service and then how to send request using parameters of pagination to easily navigate search results

**Time to complete**: About 3 minutes

## Before you begin
To run Python code samples from this tutorial you will need to setup your virtual environment.

Please use this commands in a terminal:
```
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
```
Now install google packages:
```
pip install google
pip install google-cloud-retail
```

## Simple query request
The simple search request contains only required fields which are: 
  - ```placement``` - The resource name of the search engine placement
  - ```visitor_id``` - A unique identifier for tracking visitors
  - ```query``` - Raw search query or search phrase

There is a request ready to be run on a catalog full of different products, so you will see the results right away, 
but first please open the **search_simple_query.py** to review the request.

To send this request to the search service, open a terminal and run:
```
python search_simple_query.py 
```

## Simple query. Response analyze
Now in a field ```results[]``` you can see A list of matched items returned by Retail Search service.

```total_size``` it's the estimated total count of matched items.

```attribution_token``` it's a unique search token which enables accurate attribution of search model performance.

```next_page_token``` A token that points to the next page in the search response. By default the number of products per page is 100. If this field is omitted, there are no subsequent pages.

## Pagination
Using pagination is simple and easy way not only to view and navigate the search results, but also to decrease the lookup time and the size of the responses.

There are three fields in the search request which gives you all the posibilities of navigation throug the search results: ```page_size```, ```next_page_token```, ```offset```.

Lets see how each of them works.

## Page size

The ```page_size``` request field allows you to limit the number of items in the search response.

Open **search_with_pagination_page_size.py** to view the request with ```page_size```.

Run it in a terminal with a command:
```
python search_with_pagination_page_size.py
```

## Page size. Response analyze
Now you can see the ```results[]``` contains the number of products which you set as page size.

The ```total_size``` does not equal the page size, it's the number of matched items for this search query, so it will not change as you are changing the number of products per page.

The ```next_page_token``` will be used in the next tutorial step.

## Next page token
As you have received the response from previous step you can take the value of field ```next_page_token```,
and if you send the **same** request but set a request parametr ```page_token``` with this value (next_page_token) you will get the result products with the next <page_size> relevance.

Open the **search_with_pagination_next_page.py**, 

as you will run it whole independently, we placed there a sequence of requests:
- first with only the page size, you will get the next_page_token value from it's response, 
- the other demonstrates the navigation to the next page using ```page_token``` and this value. 

Run it in a terminal with a command:
```
python search_with_pagination_next_page.py
```

## Next page token. Response analyze
In the response you see the next page of products which is the next <page_size> relevence.

The field ```next_page_token``` now has value generated to point on the next page and can be used in furher results navigation.

## Offset
In some other cases, instead of navigating from page to page or getting results with top relevance, you could directly jump to a particular position with offset.

For example, if you want the tenth page of the results when the page size is 5, then you could set the offset to be 45, which is calculated by (10 - 1) * 5.

Open the **search_with_pagination_offset.py**, run it and check the result of ```page_size``` and the ```offset``` parameters combination.

Run it in a terminal with a command:
```
python search_with_pagination_offset.py
```

**We encourage you to test the pagination by yourself, right here in the CloudShell environment, using different combinations of values for pafination parameters**

**Thank you for compleating this tutorial!**





