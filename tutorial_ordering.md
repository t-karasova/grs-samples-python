# **Ordering Tutorial**

## Let's get started

This tutorial will show you how to order items in a search response. 

The ordering can be applied to most of the product fields, the full list of the fields you can find in [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#order)


Let's see how the ordering works.

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

**Tip**: Click the copy button beside the code box to later paste the command in the Cloud Shell terminal and run it.


## Ordering by a single field

To use the ordering feature you need to specify the field and the ordering direction. You can order by textual as well as by numerical fields.

First let's order the search results by price, the more expensive ones first. In such case the ordering expression should be set as 

```order = 'price desc'```
 

To see the whole request with ordering open **search_with_ordering.py**

Run the sample in a terminal with the command:
```bash
python search_with_ordering.py
```

Now you can see ```results[]``` are ordered by price descending.

Next let's change the ordering direction to show the cheapest products first.

Just find the comment 

"#TRY DIFFERENT ORDERING EXPRESSIONS HERE:" 

and change the ordering expression to: 
```order = 'price asc'``` or just ```order = 'price'``` - that's an equivalent expressions since ascending is the default ordering direction.

Run the sample in a terminal with the command:
```bash
python search_with_ordering.py
```

Now you see the products are ordered by price ascending

## Ordering by multiple fields

Ordering by multiple fields is supported through the use of comma-separated fields in the order of priority, more prioritized first. 

The lower priority fields will be used to order items with equal values for higher priority fields. 


For example, **```rating desc, price```** would order items by their rating first, then the products with the same rating will be ordered by price.

To try that, please change the ordering expression to:
```
order = 'rating desc, price'
```

Run the code sample in a terminal using the command:
```bash
python search_with_ordering.py
```

## Success 

You have completed the tutorial and now we **encourage** you to **test the ordering by yourself**, try different combinations of different order expressions.

**Thank you for completing this tutorial!**
