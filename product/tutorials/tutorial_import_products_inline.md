# **Import Products From Inline Source Tutorial**

## Let's get started

The inline importing is a convenient way to make bulk changes in a catalog, such as:

- import some amount of products, no more than 100 at a time,
- update some products set,
- make fast and frequent changes of products quantity or price or any other field.

To import your products into a catalog inline you should prepare the ```product_inline_source``` object which is a set
of products. Each product should be provided in a JSON format as a standalone line (one product per line with line breaks as a
delimiter). To find an example of a product in JSON format, refer to
the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#json-format)

To find more information about different import types, their restrictions, and use cases, refer to the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a terminal:

```bash
python3 -m venv tutorial-env
```

```bash
source tutorial-env/bin/activate
```

Next, install Google packages:

```bash
python3 -m pip install google
```

```bash
python3 -m pip install google.cloud.retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and
run it.

## Import products from inline source

The only reconciliation mode available for inline import is INCREMENTAL. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the import JSON source will not change.

To check the example of an import product request, open **product/import_products_inline_source.py**.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products to.

The field ```input_config``` defines the **ProductInlineSource** as an import source.

To use generated products in this tutorial, check the ```get_products()``` function first.

To perform the products import, open terminal and run the command:

```bash
python product/import_products_inline_source.py
```

## Response analysis

Once you have called the import products method, the **import operation** has started.

Importing may take some time depending on the size of product set in your inline source.

The operation is completed when the field ```operation.done()``` is set to true. Check the result, one of the following fields should be present:
 - ```error```, if the operation failed, or
 - ```response```, if the operation was successful.

If the operation was successful, you can unpack the response to **ImportProductsResponse** and check a sample of errors
encountered while processing the request in the field ```error_samples[]```.

When set in the request, the ```errors_config``` field points to the destination for the importing errors.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import some amount of
products directly inline.

**Thank you for completing this tutorial!**
