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

Before you import products to your catalog, you need to upload the data to the BigQuery table first. You can do it two
ways:

 - create an [empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition)
  using Retail schema, and create products in it using SQL,
 - create a BigQuery table using prepared JSON file with all the products in GCS bucket. You can define Retail schema or
  use autodetect option.

Then, import your data to the Retail API.

For this tutorial we have already created a BigQuery table, so you can use it in your Retail API import request.

Open **product/import_products_big_query_table.py** and look at the example of import product request.

The field **```parent```** contains a **catalog name** along with a branch number to which you are going to import your
products to.

The field **```input_config```** defines the **BigQuerySource** as an import source.

To import products, open the terminal and run the following command:

```bash
python product/import_products_big_query_table.py
```

## Response analysis

Once you have called the import products method, the **import operation** has been started.

The importing may take some time depending on the size of product set in your BigQuery table.

The operation is completed when the field **```operation.done()```** is set to true. Check the result, one of the following fields should be present:
 - **```error```**, if the operation failed, or
 - **```response```**, if the operation was successful.

You have imported valid product objects to the catalog, so the operation should be successful, and the operation object should contain a field **```response```**. 

TODO[PUT OPERATION OBJECT HERE]

Check the **```response```** field in the operation object returned and printed to the Terminal. 

The **```error_samples[]```** field should be empty.



## Error handling

Now, let's try to import a couple of invalid product objects and check the error message in the operation response, note that in this case the operation itself is considered as successful.

The field title is a required field, so if you remove it, you will get invalid product object. There is a **```products_for_import_some_invalid```** table in the BigQuery dataset which contains such an invalid products.
Let's use it for import to get an error message.

Go to the code sample assign the file name as a value of gcs_products_object:
```py
table_id = "products_for_import_some_invalid"
```

Now, run the code sample and wait till the operation will be done. Check the operation printed out to the Terminal.
The operation if completed, it is successful, so you can find a field **```response```**, otherwise there would be a field **```error```** instead.

Check the error message in the **```response.error_samples```** list, it should point on the invalid product object and its field which caused a problem, in our case the message should be:

//TODO
//[PUT ERROR MESSAGE HERE]

Next, let's send invalid import request to get failed operation. 

Go tho the code sample and in the method **```get_import_products_big_query_request()```**  and add there a local variable ```default_catalog``` with some invalid catalog name.

Now run the code one more time and check the operation object, now it contains the field **```error```** instead of **```response```**. The error message should be the following:

//TODO
//[PUT ERROR MESSAGE HERE]

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from the
BigQuery table.

**Thank you for completing this tutorial!**
