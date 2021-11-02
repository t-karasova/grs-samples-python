# **Attribute Configuration Tutorial**

## Let's get started

Retail Search allows you to configure the product attributes for the search purpose. 

If you want the Retail Search to be able to filter and facet your catalog using this product attribute, you should set it as indexable.

If you want to enable the search by some product attribute, you should make this attribute searchable. Note, that onsy text attributes can be searchable.

In this tutorial you will learn how to configure the product attributes to allow the Retail Search to perform products indexing and search.

**Time to complete**: About 4 minutes

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

Run the following commands in a terminal:
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

## Filter by unindexable field

There are several products in the catalog with the attribute "eco-friendly".  The attribute's field **```indexable```** is set to **false**.

```json
 "eco-friendly":{
      "indexable":"false",
      "searchable":"false",
      "text":[
         "Low-impact fabrics",
         "recycled fabrics",
         "recycled packaging",
         "plastic-free packaging",
         "ethically made"
      ]
   }
```

Let's try to search for a sweater and filter the search results by this field.

To do that you should use a filter **```'(attributes.eco-friendly: ANY("recycled packaging"))'```**

You can find the prepared SearchRequest in the **search/search_attribute_config.py**

Run the sample in a terminal using the command:

```bash
python search/search_attribute_config.py
```
Check the search response printed out to the Terminal.
As the attribute was not indexed, the filter was not applied to the search resuts, and you see the unfiltered list of products in a response.

## Make the product attribute Indexable

To make the attribute indexable we need to set the "indexable" field to "true". 

Let's do it using the **```update_product()```** method in **search/update_attribute_configuration.py**

Run it in a terminal using the command:

```bash
python search/update_attribute_configuration.py
```

## Filter by indexable field

Now, as you have configured the product attribute "eco-friendly" as **indexable**, let's check the Retail API treats it now.

Request the Search Service again with the same request with the filter: ```'(attributes.eco-friendly: ANY("recycled packaging"))'```

```bash
python search/search_attribute_config.py
```

As you are searching by the indexable field the filter is applied to the search response and in the result list you will see the requested product.

## Search for non-searchable attribute value

Next, let's request the Retail Search with a query **"Low-impact fabrics"**. This is one of the values of the "eco-friendly" attribute, which is still non-searchable.

The search response should be empty as the Retail Search do not take this attribute into account performing the search.

Open the **search/search_attribute_config.py** and change the value in the field **```search_request.query```**:
```py
 search_request.query = "Low-impact fabrics"
```

Comment out the line ```search_request.filter = '(attributes.eco-friendly: ANY("recycled packaging"))'``` to avoid the narrowing down search results. 

Run the code in a terminal using the command:

```bash
python search/search_attribute_config.py
```
Check the result is empty

## Make the attribute searchable

Next, open the **search/search_attribute_config.py** and change the value of  **attribute.searchable** to "true":

```py
 attribute.searchable = "true"
```
Update the product running the command:

```bash
python search/update_attribute_configuration.py
```

## Search for Searchable attribute value

Call the Retail Search  with the query **"Low-impact fabrics"** again.

This time the service should return the matched product. 

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the searchability and indexability** of different product attributes by yourself.

**Thank you for completing this tutorial!**