# **Querying Tutorial**

## Let's get started

This tutorial shows you how to send a simple search query to the Retail Service and analyze the response.

**Time to complete**: About 1 minute

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run these commands in a terminal:

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

## Simple query request

The simple search request contains only the following required fields: 
  - ```placement``` - A resource name of the search engine placement.
  - ```visitor_id``` - A unique identifier to track visitors.
  - ```query``` - Raw search query or search phrase.

To check the results right away, you need to run a request against a catalog full of different products.

First, open the **search_simple_query.py** to review the request.

To send this request to the search service, open a terminal and run the follwoing command:
```bash
python search_simple_query.py 
```

## Simple query. Response analysis.

As you can see now, the field **```results[]```** contains a list of matched items returned by the Retail Search service.

**```total_size```** is the estimated total count of matched items.

**```attribution_token```** is a unique search token that enables accurate attribution of the search model performance.

**```next_page_token```** is a token that forwards to the next page in the search response. By default, the number of products per page is 100. If this field is omitted, there are no subsequent pages.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the search by yourself** right here in the Cloud Shell environment using different search queries.

**Thank you for completing this tutorial!**





