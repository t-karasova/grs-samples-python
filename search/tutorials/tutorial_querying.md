# **Querying Tutorial**

## Let's get started

This tutorial shows you how to send a simple search query to the Retail Service and analyze the response.

**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run these commands in a terminal:


```bash
python -m venv <your-env>
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

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER="<YOUR_PROJECT_NUMBER>"
```

## Simple query request

The simple search request contains only the following required fields: 
  - ```placement``` - A resource name of the search engine placement.
  - ```visitor_id``` - A unique identifier to track visitors.
  - ```query``` - Raw search query or search phrase.

To check the results right away, you need to run a request against a catalog full of different products.

First, open the **search_simple_query.py** to review the request.

To request the search service with a "Hoodie" query, run this code sample.

Open a terminal and  send this request running the following command:
```bash
python search_simple_query.py 
```

## Simple query. Response analysis.

As you can see now, the field **```results[]```** contains a list of matched items returned by the Retail Search service.

**```total_size```** is the estimated total count of matched items.

**```attribution_token```** is a unique search token that enables accurate attribution of the search model performance.

**```next_page_token```** is a token that forwards to the next page in the search response. By default, the number of products per page is 100. If this field is omitted, there are no subsequent pages.

## Simple query. Query phrase calibrating

Next, try to experiment with the query phrases. 

Find the comment "# TRY DIFFERENT QUERY PHRASES HERE:" 
and change the value of "query_phrase" with something like this:

``` query_phrase= "Zip Hoodie"``` 

```query_phrase= "Unisex Zip Hoodie"``` 

Adding one more word to the query phrase makes your request more accurate. You can expect less products in the response, and the most relevant products will appear on the top of the response list.

## Simple query. Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

In this tutorial, you will get an error message when trying to request the Search Service without setting the ```visitorId``` which is a required field.

To check how it works, comment out a line ```search_request.visitor_id = "123456"``` and run the code sample again.

Send the request once again:
```bash
python search_simple_query.py 
```

You should see the following error message:

```google.api_core.exceptions.InvalidArgument: 400 Field "visitorId" is a required field, but no value is found.```

## Success 

You have completed the tutorial! We **encourage** you to **test the search by yourself** right here in the Cloud Shell environment using different search queries.

**Thank you for completing this tutorial!**
