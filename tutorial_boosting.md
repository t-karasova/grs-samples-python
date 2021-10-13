# **Boosting Tutorial**

## Let's get started

Boosting is a powerful and convenient feature that allows you to prioritize products that match certain condition.
To specify a condition you can use filtering expressions.

A boosting specification can be based on a single field condition or on multiple fields. You can also combine several specifications within one boosting request.

In this tutorial you will see a couple of examples of products boosting, so let's get started.


**Time to complete**: About 4 minutes

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


## Boosting by one criterion

The boosting specification looks like this:
  
  ```
  condition_boost_specs {
         condition: string
         boost: double [-1;1]
    }
```

To set the **```condition```** you should use a filtering expression, like:

```'(colorFamily: ANY("black"))'``` 

or  
```'(rating: IN(4.0, 5.0))'```

More detailed information about the filtering expressions can be found in [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter) 

The field **```boost```** defines the strength of the condition boost, which should be in the range between -1 and 1. Negative boost means demotion.

To see the whole request with a product boosting open **search_with_boosting.py**

Run it in a terminal with the command:
```bash
python search_with_boosting.py
```

Now you can check ```results[]```, the products that correspond to the boost condition became reranked.

## Some notes about boosting

Please note that setting boost strength to 1.0 gives the item a strong promotion. However, it **does not necessarily mean that the boosted item will be the top result at all times**, nor that other items will be excluded. 
Results could still be shown even when none of them matches the condition. 

Also, results that are **significantly more relevant** to the search query can still trump your heavily favored but irrelevant items.

You can combine up to 10 boost specifications in one search request. In this way you may apply really sophisticated boosting rules to your search request.

## Success 

You have completed the tutorial and now we **encourage** you to **test the filtering by yourself**, try different combinations of different filter expressions.

**Thank you for completing this tutorial!**
