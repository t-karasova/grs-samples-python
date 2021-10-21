# **Filtering Tutorial**

## Let's get started

Filtering in the Retail Service is a powerful and convenient search feature. It lets you fine-tune search requests according to your or your customer's needs.

- You can filter by single or multiple fields.
- You can filter by text or numeric fields, or both. 
- You can use an expression language to construct a predicate for each field.
- You can combine different expressions using logical operators.

See, the possibilities are impressive.

Let's try them.

**Time to complete**: About 4 minutes

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to run it.


## Filtering by text field

You can write a simple expression that applies to the text field and looks like this:

```(textual_field,":", "ANY", "(",literal,{",",literal},")"```

Function "ANY" returns true if the field contains any of the literals.

The example of such expression is 

```'(colorFamily: ANY("black"))'``` 

To see the whole request with the filtering applied, open **search_with_filtering.py**

Run it in a terminal along with the command:
```bash
python search_with_filtering.py
```

As you can see now, ```results[]``` contains only items that satisfy the filtering expression.

Feel free to test filtering by a textfield yourself, right here in the Cloud Shell environment.

To do that, find the comment: 

"#TRY DIFFERENT FILTER EXPRESSIONS HERE:" 

and replace the filtering expression with something like this:

```
filter = '(brands: ANY("YouTube"))'
```

Or
```
filter = '(colorFamily: ANY("White","Grey"))'
```

Please check the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter) to see the complete list of the text fields you can apply the filters to.

## Filtering by a numeric field. IN range

To filter by a numeric field, you can write the filtering expression in two ways:
- To check whether the field value is within a range, use the function **"IN"**
- To compare a field value with a double value, use operators **<=**,  **<**,  **>=**, **>**, **=**.

Let's use the function "IN" to search for products with the price exceeding $15 and less than $30.

Please use the same request as in the previous step. Open **search_with_filtering.py** if you have closed it, and change the filter expression to the following:

```
filter = 'price: IN(15.0, 45.0)'
```

Run the code sample in a terminal using the next command:
```bash
python search_with_filtering.py
```

Check the search response. Now, it contains only items with prices in the range of $15 to $45.

Please check the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter) to see the complete list of the numeric fields you can apply the filters to.

## Filtering by a numeric field. Comparison operators

All comparison operators **<=**,  **<**,  **>=**, **>**, **=** are available for filtering expressions.

Like in the previous step, use **search_with_filtering.py** to modify the filter expression.

Try the following expression which is equivalent to the one you have used in the previous step:
```
filter = 'price >= 15.0 AND price < 45.0'
```

Run the code sample in a terminal using the command:
```bash
python search_with_filtering.py
```

Check the search response. Now, it contains only items with prices in the range between $15 and $45.

## Filtering by multiple fields

To filter the search results by multiple fields, you can combine the expressions with **"AND"** or **"OR"** operators.

**```filter = expression, { " AND " | "OR", expression };```**

Like in the previous step, use **search_with_filtering.py** to modify the filter expression.

Try the following expression to see how you can combine different filtering conditions: 
```
filter = '(categories: ANY("Apparel")) AND (price: IN(30.0, *))'
```

Run the code sample in a terminal using the next command:
```bash
python search_with_filtering.py
```

## Filtering. Error handling

In case of sending some invalid data or if any of required fields is missed in the request the Search Service will respond with an error message.
An entire list of fields of Search Request with the requirements to each of them you may find in the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

There is a list of **textual and numerical fields supported for filtering** in the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

In this tutorial you will get an error message trying to filter the search results by a field which is not supposed to be used for filtering, like "name".

Please change the value of variable "filter" to:
``` filter = '(name: ANY("some_random"))'```

and run the code once again:
```bash
python search_with_filtering.py
```

You should see the following error message:

```google.api_core.exceptions.InvalidArgument: 400 Invalid filter syntax '(name: ANY("some_randome"))'. Parsing filter failed with error: Unsupported field "name" on ":" operator.```


## Success 

You have completed the tutorial! We **encourage** you to **test the filtering by yourself** and try different combinations of various filter expressions.

**Thank you for completing this tutorial!**





