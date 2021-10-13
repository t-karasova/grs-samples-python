# **Query Expansion Tutorial**

## Let's get started

This tutorial will show you how to enable the query expansion feature which allows you to increase the recall for query terms with multiple results,
especially long tail queries.

If the query expansion is disabled, only the exact search query is used, even if the total number of search result is zero.

Enable query expansion feature and let Google Retail Search build an automatic query expansion.

You can also pin unexpanded products, so they will always be at the top of search results, followed by those that come via expansion.

This is a really useful feature that helps you enhance a customer experience. So let's look at it closely.


**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial you will need to set up your virtual environment.

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


## Query expansion

Open **search_with_query_expansion_spec.py**, take a look at the search request, here you see the query expansion condition set with value "AUTO". The setting means that the query expansion feature is turned on, and the search results will be expanded.

Run the sample in a terminal with the command:
```bash
python search_with_query_expansion_spec.py
```

Now you can see ```results[]``` have products that do not exactly match the search query but are really close to it.

Next let's change the condition value to "DISABLED":

Just find the comment 

 # [TRY DIFFERENT QUERY EXPANSION CONDITION HERE:] 

and change the condition to: 
```condition = SearchRequest.QueryExpansionSpec.Condition.DISABLED```

Run the sample in a terminal with the command:
```bash
python search_with_ordering.py
```

Now you see the results contain only the items that are an exact match.

## Success 

You have completed the tutorial and now we **encourage** you to **test the query expansion by yourself**, try different search phrases with and without query expansion.

**Thank you for completing this tutorial!**
