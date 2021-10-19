# **Import Products From Inline Source Tutorial**

## Let's get started

The inline importing is a convenient way to make bulk changes in a catalog:

- import some amount of products, no more than 100 at a time,
- update some products set,
- make fast and frequent changes of products quantity or price or any other field.

To import your products into a catalog inline you should prepare the ```product_inline_source``` object which is a set
of products. Each product should be provided in a JSON format as single line (one product per line with line breaks as a
delimiter). An example of a product in JSON format can be found in
a [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#json-format)

More information about different import types, their limitations and use cases you can find
in [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

**Time to complete**: About 2 minutes

## Before you begin

To run Python code samples from this tutorial you will need to set up your virtual environment.

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

**Tip**: Click the copy button on the side of the code box to later paste the command in the Cloud Shell terminal and
run it.

## Import products from inline source

It is worth to mention that for inline import the only INCREMENTAL reconciliation mode is available, it means that
during the importing new products will be inserted and existing products will be updated, if there are products in
catalog which are absent in the import source JSON they will remain unchanged.

Please open **product/import_products_inline_source.py** and look at the example of import product request.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products.

The field ```input_config``` defines the **ProductInlineSource** as an import source.

In this tutorial we are going to use generated products, please check get_products() function.

To perform the products import open terminal and run the command:

```bash
python product/import_products_inline_source.py
```

## Response analysis

Once you have called the import products method of Retail API, the **import operation** has been started.

The importing may take some time depending on the size of products set iin your inline source.

When the field ```operation.done()``` is set with ```true``` that means the operation is finished. Now you can check the
result: there is exactly one of fields: ```error``` in case if the operation was failed or ```response``` if operation
is successful.

If the operation was successful you can unpack the response to **ImportProductsResponse** and see a sample of errors
encountered while processing the request in a field ```error_samples[]```.

```errors_config``` field points to the destination for the importing errors if it was set in the request.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import some amount of
products directly inline.

**Thank you for completing this tutorial!**
