# **Ordering Tutorial**

## Let's get started

This tutorial shows you how to order items in a search response. 

You can apply ordering to most of the product fields. To find the complete list of available fields, check the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#order)


And now, let's see how the product ordering works.

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

**Tip**: Click the copy button beside the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Ordering by a single field. Ordering expression

To use the ordering feature, you need to specify the field and the ordering direction. You can order by both the text and numeric fields.

First, let's order the search results by price when more expensive items come first. To do that, set the ordering expression as follows: 

```order = 'price desc'```
 

To see the whole request with ordering, open **search_with_ordering.py**

Run the sample in a terminal using the following command:
```bash
python search_with_ordering.py
```

As you can see now, ```results[]``` are ordered by price descending.

## Ordering by a single field. Product sorting

Next, let's change the ordering direction to show the cheapest products first.

To do that, find the comment 

"#TRY DIFFERENT ORDERING EXPRESSIONS HERE:" 

and change the ordering expression to the following one:

```order = 'price asc'``` or just ```order = 'price'``` - those are equivalent expressions since ascending is the default ordering direction.

Run the sample in a terminal using the command:

```bash
python search_with_ordering.py
```

You have sorted the products by price ascending.

## Ordering by multiple fields

You can order items by multiple fields using the comma-separated fields in order of priority (more prioritized come first). 

To order items with equal values for higher priority fields, use the lower priority fields. 

For example, **```price desc, discount desc```** orders items by their price first. The products with the same price will be ordered by a discount amount.

To try that, change the ordering expression to the next one:
```
order = 'price desc, discount'
```

or

```
order = 'brands, attributes.collection desc'
```

Run the code sample in a terminal using the command:
```bash
python search_with_ordering.py
```

## Ordering. Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

To check a list of **ordering fields**, use the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#order)

If you try to order the search results by the field that is **not intended for ordering** (for example, the "name" field), you will get an error message.

Change the variable "order" value to the following:
```order = 'name desc'```

and run the code once again:
```bash
python search_with_ordering.py
```

You should see the following error message:

```google.api_core.exceptions.InvalidArgument: 400 Invalid orderBy syntax 'name desc'. Parsing orderBy failed with error: Unsupported field in orderBy: name. ```

## Success 

You have completed the tutorial! We **encourage** you to **test the ordering by yourself**, and try different combinations of various order expressions.

**Thank you for completing this tutorial!**
