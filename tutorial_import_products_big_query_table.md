# **Import Products From BigQuery Table Tutorial**

## Let's get started

Retail API offers you a convenient way to import your catalog data from previously loaded BigQuery table.

Using BigQuery table you are able to import really large volume of catalog data with no limits.

Also you can specify the Retail schema that has more product attributes than other import options, including key/value
custom attributes.

And finally using BigQuery table as an import source you can choose one of reconciliation modes: **INCREMENTAL** or 
**FULL**.

- In a case of incremental import the products which were not existed in a catalog before import will be created, and
  the existent products will be updated.
- In a case of full import an existing products will be deleted if they are not present in the BigQuery source, new
  products will be added, and the products existent in the catalog before import and in the BigQuery table will be
  updated.

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

## Import products from BigQuery table

Before you import products to your catalog you will need to upload the data to the BigQuery table first. You can do it 2
ways:

- create
  an [empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition)
  using Retail schema and create products there using SQL,
- create a BigQuery table using prepared JSON file with all the products in GCS bucket, you can define Retail schema or
  use autodetect option.

Then, upload your data to the Retail API.

For this tutorial we have already created a BigQuery table, so you can use it in your Retail API import request.

Please open **product/import_products_big_query_table.py** and look at the example of import product request.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products.

The field ```input_config``` defines the **BigQuerySource** as an import source.

To perform the products import open terminal and run the command:

```bash
python product/import_products_big_query_table.py
```

## Response analysis

Once you have called the import products method of Retail API, the **import operation** has been started.

The importing may take some time depending on the size of products set in your BigQuery tabe.

When the field ```operation.done()``` is set with ```true``` that means the operation is finished. Now you can check the
result: there is exactly one of fields: ```error``` in case if the operation was failed or ```response``` if operation
is successful.

If the operation was successful you can unpack the response to **ImportProductsResponse** and see a sample of errors
encountered while processing the request in a field ```error_samples[]```.

```errors_config``` field points to the destination for the importing errors if it was set in the request.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from the
BigQuery table.

**Thank you for completing this tutorial!**
