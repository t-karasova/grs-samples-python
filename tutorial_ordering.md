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


## Ordering by a single field

To use the ordering feature, you need to specify the field and the ordering direction. You can order by both the text and numeric fields.

First, let's order the search results by price when more expensive items come first. To do that, set the ordering expression as follows: 

```order = 'price desc'```
 

To see the whole request with ordering, open **search_with_ordering.py**

Run the sample in a terminal using the following command:
```bash
python search_with_ordering.py
```

As you can see now, ```results[]``` are ordered by price descending.

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

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the ordering by yourself**, and try different combinations of various order expressions.

**Thank you for completing this tutorial!**
