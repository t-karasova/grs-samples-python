# **Search With Boosting Tutorial**

## Let's get started

Boosting is a powerful and convenient feature that allows you to prioritize products that match certain condition.
To specify a condition, you can use filtering expressions.

A boosting specification can be based on a single field condition or on multiple fields. Also, you can combine several specifications into one boosting request.

In this tutorial you will learn some examples of product boosting.


**Time to complete**: About 4 minutes


## Boosting by one criterion. Condition and filtering expression 

The boosting specification looks like this:
  
  ```
  condition_boost_specs {
         condition: string
         boost: double [-1;1]
    }
```

To set the **```condition```**, you should use a filtering expression like the one below:

```'(colorFamily: ANY("Blue"))'``` 

or  
```'(price: IN(15.0, 30.0))'```

You can learn how to use filters in the [Filtering Tutorial](tutorial_filtering.md) 
or read about it in the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter) 

The field **```boost```** defines the strength of the condition boost, which should be in the range of -1 to 1. Negative boost means demotion.

Now, open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="boost.*0">search_with_boost_spec.py</walkthrough-editor-select-regex>


In the initial request, the boost strength is set to zero: ```boost = 0.0```, so the boosting will **not affect** the order of the products in the response.


## Boosting by one criterion. Boost results

Run the sample in a <walkthrough-editor-spotlight spotlightId="menu-terminal-new-terminal">terminal</walkthrough-editor-spotlight> with the following command:
```bash
python cloudshell_open/grs-samples-python/search/search_with_boost_spec.py
```
Check the response to see the original order of products depending on their relevance to the query phrase.

Next, let's change the value of the field **boost** and run the code sample once again:
```boost = 1.0```

Now you can check ```results[]```. The products corresponding to the boost condition became reranked. Now, blue products are **on the top** of the list.

If you set ```boost = -1.0```, blue products will appear **at the bottom** of the search result.

## Some notes about boosting

Please note that setting the boost strength to 1.0 gives the item a strong promotion. However, it **does not necessarily mean that the boosted item will be the top result at all times**, nor that other items will be excluded. 
Results could still be shown even when none of them matches the condition. 

Also, results that are **significantly more relevant** to the search query can still trump your heavily favored but irrelevant items.

You can combine up to 10 boost specifications in one search request. In this way, you may apply really sophisticated boosting rules to your search request.

## Try different boosting conditions

Feel free to test product boosting yourself right now in the Cloud Shell environment.

Replace the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="condition = '.*'">condition</walkthrough-editor-select-regex> expression with something like this:

```
condition = '(categories: ANY("Office"))'
```

Or
```
condition = '(attributes.material: ANY("Cotton", "Polyester")) AND (brands: ANY("Google"))'
```

At the same time, you can test the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="boost = /D.*">boost strength</walkthrough-editor-select-regex> by setting any value from -1 to 1.

## Boosting. Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

To check the list of **text and numeric fields that support boosting**, use the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

## Boosting. Error handling results

If you try to boost the search results and set a condition in the field which is **not supposed for boosting** (for example, the "name" field), you will get an error message.

Change the variable <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/search/search_with_boost_spec.py" regex="condition = '.*'">condition</walkthrough-editor-select-regex> value to the following:
``` condition = '(name: ANY("some_random"))'```

Run the code once again:
```bash
python cloudshell_open/grs-samples-python/search/search_with_boost_spec.py
```

You should see the following error message:

```google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(name: ANY("some_random"))'. Parsing filter failed with error: Unsupported field "name" on ":" operator.```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the boosting by yourself** and try different combinations of various filter expressions.

### What's next?

<walkthrough-tutorial-card id="retail_api_querying_python_v2" title="Search simple query tutorial" keepPrevious=true>
Learn how to search for products in a catalog using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_pagination_python_v2" title="Search with pagination tutorial" keepPrevious=true>
Learn how to navigate the search results using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_filtering_python_v2" title="Search with filtering tutorial" keepPrevious=true>
Learn how to filter search results using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_ordering_python_v2" title="Search with ordering tutorial" keepPrevious=true>
Learn how to order search results using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_boosting_python_v2" title="Search with boosting tutorial" keepPrevious=true>
Learn how to prioritize products in the search response using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_query_expansion_python_v2" title="Search with query expansion tutorial" keepPrevious=true>
Learn how to enable the query expansion feature using the Retail API</walkthrough-tutorial-card>


**Thank you for completing this tutorial!**
