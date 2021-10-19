# **Query Expansion Tutorial**

## Let's get started

This tutorial shows you how to enable the query expansion feature to **increase the efficiency for search** for ambiguous or long-tail* query terms.

Disabling the query expansion results in using only the exact search query, even if the total number of search results is zero.

Enable the query expansion feature and let the Google Retail Search build an **automatic query expansion**.

You can also **pin unexpanded products**, so that they always appear at the top of search results followed by products enlisted via expansion.

This useful feature helps you to **enhance a customer experience**. 

Let's look at it closely.

**Time to complete**: About 2 minutes


*Long-tail query terms are unpopular keyword phrases with low search volume and high variation.

## Before you begin

To run the Python code samples from this tutorial, you need to set up your virtual environment.

Run these commands in a terminal:
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

**Tip**: Click the copy button on the side of the code box to later paste the command in the Cloud Shell terminal and run it.


## Query expansion

Open **search_with_query_expansion_spec.py** and take a look at the search request. Here you can see the query expansion condition set with value "AUTO". The setting enables the query expansion feature and expands the search results.

Run the sample in a terminal using the command:
```bash
python search_with_query_expansion_spec.py
```

As you can see, ```results[]``` contain products that do not exactly match the search query but are close to it.

Next, let's change the condition value to "DISABLED".

To do that, find the comment 

 "#TRY DIFFERENT QUERY EXPANSION CONDITION HERE:"

and change the condition to the following: 

```condition = SearchRequest.QueryExpansionSpec.Condition.DISABLED```

Run the sample in a terminal using the command:

```bash
python search_with_ordering.py
```

As you can see, the results contain only items that exactly match the search query.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the query expansion by yourself** and try different search phrases with and without query expansion.

**Thank you for completing this tutorial!**
