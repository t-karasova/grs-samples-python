# **Import Products From the BigQuery Table Tutorial**

## Let's get started

Retail API offers you a convenient way to import your catalog data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive amounts of catalog data with no limits.

Moreover, you can specify the Retail schema that has more product attributes than other import options including
key/value custom attributes.

You can choose one of the reconciliation modes, **INCREMENTAL** or **FULL**, using the BigQuery table as an import source.

 - Incremental import creates products that did not exist in a catalog before importing and updates all current products.
 - Full import deletes current products if they are not present in the BigQuery source, adds new products, and updates
  current products that existed in the catalog before importing and in the BigQuery table.

To find more information about different import types, their restrictions, and use cases, check the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

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

Before you import products to your catalog, you need to upload the data to the BigQuery table first. There are two ways to do it:

 - Create an [empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition)
  using the Retail schema, and create products in it using SQL.
 - Create a BigQuery table using the prepared JSON file with products. You can define the Retail schema or
  use an autodetect option.

Then, import your data to the Retail API.

For this tutorial we have already created a BigQuery table, so you can use it in your Retail API import request.

Open **product/import_products_big_query_table.py** and look at the example of the import product request.

The field **```parent```** contains a **catalog name** along with a branch number you are going to import your
products to.

The field **```input_config```** defines the **BigQuerySource** as an import source.

To import products, open the terminal and run the following command:

```bash
python product/import_products_big_query_table.py
```

## Response analysis

Once you have called the import products method, the **import operation** has started.

Importing may take some time depending on the size your BigQuery table.

The operation is completed when the field **```operation.done()```** is set to true. 

Check the result, one of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid product objects to the catalog.

Check the ```big_query_operation.metadata.success_count``` field to get the total number of the successfully imported products - expected number is 316.

The number of failures during the product import is returned in ```big_query_operation.metadata.failure_count``` field - expected number is 0.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal, it should be like following: 
```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_product/errors7399332380794639317"
}
```

## Errors appeared during the importing

Now, let's try to import a couple of invalid product objects and check the error message in the operation response. 

The title field is required, so if you remove it, you get the invalid product object. 
The other example of invalid product is a product with some incorrect value of product.availability field.
There is a **```products_for_import_invalid```** table in the BigQuery dataset that contains such invalid products.

Let's use it for importing to get an error message.

Go to the code sample and assign the ```table_id```value to the table with invalid products:

```py
table_id = "products_for_import_invalid"
```
Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during the importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case the operation considered as successful, and the ```big_query_operation.metadata.success_count``` field contains the number of the successfully imported products, which is "2".

There are two invalid products in the input JSON file, and the number of failures during the product import in the ```big_query_operation.metadata.failure_count``` field is also "2".

The ```operation.result``` field points to the errors bucket where you can find a json file with all the importing errors.

The errors are the following: 

```json
{"code":3,"message":"Invalid value at 'availability' (type.googleapis.com/google.cloud.retail.v2main.Product.Availability): \"INVALID_VALUE\"","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":1}}]}
{"code":3,"message":"The string in \"product.title\" is a required field, but no value is found.","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":4}}]}
```

## Errors appeared due to invalid request

Next, let's send invalid import request to make the operation fail. 

In the code sample, find the **```get_import_products_big_query_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message, it should be like following:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare data for importing and import products from the
BigQuery table.

**Thank you for completing this tutorial!**
