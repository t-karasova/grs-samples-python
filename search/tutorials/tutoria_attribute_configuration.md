# **Attribute Configuration Tutorial**

## Let's get started

Retail Search allows you to configure the product attributes for the search purpose. 

If you want the Retail Search to be able to filter and facet your catalog using a product attribute, you should set it as indexable.

If you want to enable the search by some product attribute, you should make this attribute searchable. Note, that only text attributes can be searchable.

In this tutorial you will learn how to configure the product attributes to make them searchable and indexable for the Retail Search service.

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

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER="<YOUR_PROJECT_NUMBER>"
```

## Filter by unindexable field

There are several products in the catalog with the attribute "eco-friendly".  The attribute field **```indexable```** is set to **false**.

```json
 "ecofriendly":{
      "indexable":"false",
      "searchable":"false",
      "text":[
         "recycled fabrics",
         "recycled packaging",
         "plastic-free packaging",
         "ethically made"
      ]
   }
```

Let's try to search for a sweater and filter the search results by this field.

To do that, use a filter **```'(attributes.eco-friendly: ANY("recycled packaging"))'```**

You can find the prepared SearchRequest in the **search/search_attribute_config.py**

Run the sample in a Terminal using the following command:

```bash
python search/search_attribute_config.py
```
Check the search response printed out to the Terminal.

The attribute was not indexed, so the filter was not applied to this field and the following error message is expected:

```
google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(attributes.ecofriendly: ANY("recycled packaging"))'. Parsing filter failed with error: Unsupported field "attributes.ecofriendly" on ":" operator..
```
## Make the product attribute indexable

To make the attribute indexable, set the "indexable" field to "true". 

Let's do it using the **```update_product()```** method in **search/update_attribute_configuration.py**

Run the code in a Terminal using the following command:

```bash
python search/update_attribute_configuration.py
```
Note, as you have changed the catalog data, the Retail Search needs some time to index products,
the time depends on the catalog size, it usually takes up to 5 minutes.

## Filter by indexable field

Now, as you have configured the product attribute "eco-friendly" as **indexable**, let's check how the Retail API treats it now.

Request the Search Service again using the same request with the filter: ```'(attributes.eco-friendly: ANY("recycled packaging"))'```

```bash
python search/search_attribute_config.py
```

As you run the search by indexable field, the filter applies to the search response. You can see the requested product in the result list.

## Search for non-searchable attribute value

Next, let's request the Retail Search using the **"ethically made sweater"** query. This is one of the values of the "eco-friendly" attribute, which is still non-searchable.

The search response should be empty because the Retail Search does not take this attribute into account while performing the search.

Open the **search/search_attribute_config.py** and change the value in the **```search_request.query```** field:
```py
 search_request.query = "ethically made sweater"
```

Comment out the line ```search_request.filter = '(attributes.eco-friendly: ANY("recycled packaging"))'``` to avoid the narrowing search results down. 

Run the code in a Terminal using the following command:

```bash
python search/search_attribute_config.py
```
Check the result: it should be empty.

## Make the attribute searchable

Next, open the **search/search_attribute_config.py** and change the value of  **attribute.searchable** to "true":

```py
 attribute.searchable = "true"
```
Update the product running the command:

```bash
python search/update_attribute_configuration.py
```
The changes will take effect after the Retail Search will index them, it might take approximately 5 minutes.

## Search for searchable attribute value

Call the Retail Search  with the **"ethically made sweater"** query again.

This time the service should return the matched product. 

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the searchability and indexability** of different product attributes by yourself.

**Thank you for completing this tutorial!**