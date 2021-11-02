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
 - Create a BigQuery table using the prepared JSON file with products set in the GCS bucket. You can define the Retail schema or
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

Importing may take some time depending on the size of product set in your BigQuery table.

The operation is completed when the field **```operation.done()```** is set to true. Check the result, one of the following fields should be present:
 - **```error```** if the operation failed.
 - **```response```** if the operation was successful.

You have imported valid product objects to the catalog. The operation should be successful, and the operation object should contain a **```response```** field. 

TODO[PUT OPERATION OBJECT HERE]

Check the **```response```** field in the operation object returned to and printed in the Terminal. 

The **```error_samples[]```** field should be empty.


## Error handling

Now, let's try to import a couple of invalid product objects and check the error message in the operation response. 

Note that in this case the operation itself is considered successful.

The title field is required. If you remove it, you will get invalid product object. There is a **```products_for_import_some_invalid```** table in the BigQuery dataset that contains such invalid products.

Let's use it for importing to get an error message.

Go to the code sample and assign the ```gcs_products_object```value to the file name:
```py
table_id = "products_for_import_some_invalid"
```

Now, run the code sample and wait till the operation is completed. Check the operation result printed out to the Terminal.

The operation is completed successfully, so you can find a **```response```** field. Otherwise, there would be an **```error```** field instead.

## Error handling output analysis

Check the error message in the **```response.error_samples```** list. It should point to the invalid product object and its field that has caused a problem. 
In our case, the message should look like this:

//TODO
//[PUT ERROR MESSAGE HERE]

Next, let's send invalid import request to make the operation fail. 

In the code sample, find the **```get_import_products_big_query_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the operation object. It contains the **```error```** field instead of **```response```**. 

The error message should be as follows:

//TODO
//[PUT ERROR MESSAGE HERE]

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare data for importing and import products from the
BigQuery table.

**Thank you for completing this tutorial!**
