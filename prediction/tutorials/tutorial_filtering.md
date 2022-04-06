# Filter tutorial

## Get started

Filtering in the Prediction service allows to get more accurate 
recommendations based on your or your customer's needs.
You can:

- Filter by two types: `tag` or `filterOutOfStockItems`.
- Filter out-of-stock products.
- Filter by single or multiple tags.
- Combine tags expressions using logical operators.
- Combine out-of-stock and tag filters.
- Use an expression language to construct a predicate for tags.

In this tutorial you will learn some examples of product filtering.

## Filter by tags field: filtering expression

You can write a simple expression that applies to the tags field and looks like this:

```tag,"=",literal```

An example of such an expression is
```'tag="promotional"'```

1. To see the whole request with the filtering applied, open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_with_filtering.py" regex="TRY DIFFERENT TAG FILTER EXPRESSIONS HERE">predict_with_filtering.py</walkthrough-editor-select-regex>.

2. Run the following command in Terminal:
    ```bash
    python prediction/predict_with_filtering.py
    ```

3. Note that the results contain only items that satisfy the filtering expression.

## Filter by out-of-stock items: filtering flag

You can use flag filter to get only items in stock.

An example of such a flag is
```'filterOutOfStockItems'```

1. To see the whole request with the filtering applied, open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_with_filtering.py" regex="TRY WITH AND WITHOUT FLAG FILTERING">predict_with_filtering.py</walkthrough-editor-select-regex>.

2. Run the following command in Terminal:
    ```bash
    python prediction/predict_with_filtering.py
    ```

3. Note that the results contain only items that with a `stockState` of `OUT_OF_STOCK`.

## Filter by tags field: Use case

Now you can try filtering by tag's field yourself in the Cloud Shell environment.

1. To do that, replace the condition under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_with_filtering.py" regex="TRY DIFFERENT FILTER EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> with one of the following samples:
    ```
    filter = 'tag="season sale"'
    ```
   
    or
    ```
    filter = 'tag="season sale" tag="promotional"'
    ```
2. Run the following command in Terminal:
    ```bash
    python prediction/predict_with_filtering.py
    ```

## Filter by a tags field: boolean operators

The boolean operators `OR` and `NOT` are available for filtering expressions.

Tag values can also be immediately prepended by a dash (`-`), which is equivalent to the `NOT` operator.

1. Change the filter expression under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_with_filtering.py" regex="TRY DIFFERENT FILTER TAG EXPRESSIONS HERE">comment</walkthrough-editor-select-regex> to the following:
    ```
    filter = 'tag=("season sale" AND -"premium")'
    ```

2. Run the following command in Terminal:
    ```bash
    python prediction/predict_with_filtering.py
    ```

3. Check the prediction response. Now it contains only items with tag `season sale`, and the same time without `premium`.

## Filter by two types

To filter the prediction results by two types, you can just put them together with empty space between:

```filter = tag expression stock_flag```

1. Change the filter expression under the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_with_filtering.py" regex="TRY DIFFERENT FILTER HERE">comment</walkthrough-editor-select-regex> to the following:
    ```
    filter = 'tag="promotional" filterOutOfStockItems'
    ```

2. Run the following command in Terminal:
    ```bash
    python prediction/predict_with_filtering.py
    ```

3. Check the search response. Now it contains only in stock items with the `promotional` tag.
