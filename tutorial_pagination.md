# **Pagination Tutorial**

## Let's get started

Using pagination is a simple and easy way not only to view and navigate the search results, but also to decrease the lookup time and the size of responses.

This tutorial will show you how to control pagination in your search request.

There are three fields in the search request that give you all the posibilities of navigating through search results: 
- **```page_size```**, 
- **```next_page_token```**,
- **```offset```**.

Lets see how each of them works.

**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial you will need to setup your virtual environment.

Please use these commands in a terminal:
```bash
pip install virtualenv
```
```bash
virtualenv <your-env>
```
```bash
source <your-env>/bin/activate
```

Now install Google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

**Tip**: Click the copy button on the side of the code box to later paste the command in the Cloud Shell terminal and run it.


## Page size

The ```page_size``` request field allows you to limit the number of items in the search response.

Open **search_with_pagination_page_size.py** to view the request with ```page_size```.

Run it in a terminal with the command:
```bash
python search_with_pagination_page_size.py
```

## Page size. Response analyze

Now you can see **```results[]```** contains the number of products which you set as the page size.

The **```total_size```** does not equal the page size, it's the number of matched items for this search query, so it will not change as you play with the number of products per page.

The **```next_page_token```** will be used in the next tutorial step.

## Next page token

Having received a response at the previous step, you can request the next page by sending the **same** request with an extra property, **```page_token```** set to the value of ```next_page_token``` from the previous response. That will get you the next N=<page_size> of found items.

Open the **search_with_pagination_next_page.py**, 

as you will run it as a whole, we have placed there a sequence of requests:
- the first one with only the page size, you will get the next_page_token value from its response, 
- the other demonstrates the navigation to the next page using ```page_token``` and that value. 

Run it in a terminal with the command:
```bash
python search_with_pagination_next_page.py
```

## Next page token. Analyzing the response

In the response you see the next page of <page_size> products.

The field **```next_page_token```** now has the value generated to point to the next page and can be used in furher results navigation.

## Offset

In some other cases, instead of navigating from page to page or getting results with top relevance, you could directly jump to a particular position with offset.

For example, if you want the tenth page of the results when the page size is 5, then you could set the offset to 45, calculated as (10 - 1) * 5.

Open the **search_with_pagination_offset.py**, run it and check the result of **```page_size```** and the **```offset```** parameters combination.

Run it in a terminal with the command:
```bash
python search_with_pagination_offset.py
```

## Offset. Analyzing the response

In the response you see the requested page of products. 

The field **```next_page_token```** now has the value generated to point to the next page and can be used in furher results navigation.


## Success 

You have completed the tutorial and now we **encourage** you to **test the pagination by yourself**, right here in the CloudShell environment, using different combinations of values for pagination parameters.

**Thank you for completing this tutorial!**





