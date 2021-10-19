# **Import Products From BigQuery Table Tutorial**

## Let's get started

Retail API offers you a convenient way to import your catalog data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive amounts of the catalog data with no limits.

Moreover, you can specify the Retail schema that has more product attributes than other import options including
key/value custom attributes.

You can choose one of reconciliation modes, **INCREMENTAL** or **FULL**, using the BigQuery table as an import source.

- Incremental import creates products that did not exist in a catalog before import and updated all current products.
- Full import deletes current products if they are not present in the BigQuery source, adds new products, and updates
  current products that existed in the catalog before import and in the BigQuery table.

You can find more information about different import types, their restrictions, and use cases in
the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Import products from the BigQuery table

Before you import products to your catalog, you need to upload the data to the BigQuery table first. You can do it two
ways:

- create
  an [empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition)
  using Retail schema, and create products in it using SQL,
- create a BigQuery table using prepared JSON file with all the products in GCS bucket. You can define Retail schema or
  use autodetect option.

Then, upload your data to the Retail API.

For this tutorial we have already created a BigQuery table, so you can use it in your Retail API import request.

Open **product/import_products_big_query_table.py** and look at the example of import product request.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products to.

The field ```input_config``` defines the **BigQuerySource** as an import source.

To import products, open the terminal and run the following command:

```bash
python product/import_products_big_query_table.py
```

## Response analysis

Once you have called the import products method, the **import operation** has been started.

The importing may take some time depending on the size of product set in your BigQuery table.

The operation is completed when the field ```operation.done()``` is set to true. Check the result, one of the following fields should be present:
 - ```error```, if the operation failed, or
 - ```response```, if the operation was successful.

If the operation was successful, you can unpack the response to **ImportProductsResponse** and check a sample of errors
encountered while processing the request in the field ```error_samples[]```.

When set in the request, the ```errors_config``` field points to the destination for the importing errors.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from the
BigQuery table.

**Thank you for completing this tutorial!**
