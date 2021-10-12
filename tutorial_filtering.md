# **Filtering Tutorial**

## Let's get started

Filtering in Retail Service is a powerful and convenient search feature. It lets you fine-tune search requests according to your or your customer's needs.

- You can filter by a single or multiple fields.
- You can filter by text or numeric fields, or both 
- You can use an expression language for constructing a predicate for each field
- You can combine different expressions with the help of logical operators

See, the posibilities are impresive.

Lets try them.

**Time to complete**: About 4 minutes

## Before you begin

To run Python code samples from this tutorial you will need to setup your virtual environment.

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to run it.


## Filtering by textual field

A simple expression applying to a textual field could be written like this:

**```( textual_field, ":", "ANY", "(", literal, { ",", literal }, ")"```**

Function "ANY" returns true if the field contains any of the literals.

The example of such expression is 

```'(colorFamily: ANY("black"))'``` 

To see the whole request with filtering open **search_with_filtering.py**

Run it in a terminal with the command:
```bash
python search_with_filtering.py
```

Now you can see ```results[]``` has only items satisfied the filtering expression.

Feel free to test filtering by textual field yourself, right here in Cloud Shell environment.

Just find the comment 

"# [TRY DIFFERENT FILTER EXPRESSIONS HERE:]" 

and replace the filtering expression for something like this:

```
filter = '(brands: ANY("Google"))'
```

Or
```
filter = '(sizes: ANY("M","L"))'
```

To see the full list of textual fields you can apply the filters to please check the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

## Filtering by numerical field. IN range

If you want to filter by a numeric field you can write the filtering expression in two ways:
- To check whether the field value is within a range use the function **"IN"**
- Compare a field value with a double value with the help of operators **<=**,  **<**,  **>=**, **>**, **=**.

Let's try to use the function "IN" to search for products with price more than $50 and less than $100

Please use the same request as in the step before,  open **search_with_filtering.py** if you have it closed and change the filter expression to:

```
filter = 'price: IN(50.0, 100.0)'
```

Run the code sample in a terminal using command:
```bash
python search_with_filtering.py
```

Check the search response, now it has only items with price in the range $50 to $100.

To see the full list of numeric fields you can apply the filters to please check the [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter)

## Filtering by numeric field. Comparison operators

All the comparison operators **<=**,  **<**,  **>=**, **>**, **=** are available for filtering expressions.

Similarly to the previous step, use **search_with_filtering.py** to modify the filter expression.
Try the following expression which is equivalent to the one in the previous step:
```
filter = 'price >= 50.0 AND price < 100'
```

Run the code sample in a terminal using the command:
```bash
python search_with_filtering.py
```

Check the search response, now it has only items with price in the range between $50 and $100.

## Filtering by multiple fields

You can filter the search results by multiple fields joining the expressions with **"AND"** or **"OR"** operators.

**```filter = expression, { " AND " | "OR", expression };```**

Similarly to the previous step, use **search_with_filtering.py** to modify the filter expression.

Try this expression to see how different filtering conditions can be combined:
```
filter = '(categories: ANY("Nest > speakers and displays")) AND (price: IN(80.0, *))'
```

Run the code sample in a terminal using command:
```bash
python search_with_filtering.py
```

## Success 

You have completed the tutorial and now we **encourage** you to **test the filtering by yourself**, try different combinations of different filter expressions.

**Thank you for compleaing this tutorial!**





