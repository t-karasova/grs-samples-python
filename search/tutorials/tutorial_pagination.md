# **Pagination Tutorial**

## Let's get started

Using pagination lets you view and navigate the search results effortlessly. Moreover, it decreases both the lookup time and the size of responses.

This tutorial shows you how to control pagination in your search request.

There are three fields in the search request that give you all the possibilities of navigating through the search results: 
- **```page_size```**,
- **```next_page_token```**,
- **```offset```**

Let's see how each of them works.

**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a terminal:

```bash
pip install virtualenv
```
```bash
virtualenv <your-env>
```
```bash
source <your-env>/bin/activate
```

Next, install Google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.


## Page size

The ```page_size``` request field allows you to limit the number of items in the search response.

To view the request with ```page_size```, open **search_with_pagination_page_size.py**. 

Run it in a terminal with the next command:

```bash
python search_with_pagination_page_size.py
```

As you can see now, **```results[]```** contain the exact number of products you have set as the page size.

The **```total_size```** is not equal to the page size; it's the number of items matching the search query and it does not change as you adjust the number of products per page.

We will use **```next_page_token```** in the next tutorial step.

## Next page token

After you have received a response at the previous step, you can request the next page. 
To get the next N=<page_size> of found items, send the **same** request with a **```page_token```** property set to the value of ```next_page_token``` from the previous response.

First, open the **search_with_pagination_next_page.py**. We have placed there a sequence of requests for you to run:
- The first one with only the page size, to get the ```next_page_token``` value from its response. 
- The other, to navigate to the next page using ```page_token``` and the ```next_page_token``` value. 

Run the following command in a terminal:
```bash
python search_with_pagination_next_page.py
```

You can see the next page of <page_size> products in the response.

The field **```next_page_token```** possesses the value intended to forward you to the next page. You can use this field in further results navigation.

## Offset

In other cases, instead of navigating from page to page or getting results with top relevance, you can directly jump to a particular position using the offset.

For example, to request the tenth page of the results when the page size is **5**, set the offset to **45**, calculated as **(10 - 1) * 5**.

Open the **search_with_pagination_offset.py**, run it, and check the result of **```page_size```** and the **```offset```** parameters combination.

Run it in a terminal using the command:
```bash
python search_with_pagination_offset.py
```

You receive the requested page of products in a response. 

The field **```next_page_token```** now possesses the value intended to forward you to the next page. You can use this field in further results navigation.


## Success 

You have completed the tutorial! We **encourage** you to **test the pagination by yourself** right here in the Cloud Shell environment using different combinations of values for pagination parameters.

**Thank you for completing this tutorial!**





