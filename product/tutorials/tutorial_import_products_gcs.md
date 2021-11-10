# **Import Products From the Cloud Storage Tutorial**

## Let's get started

Retail API offers you an easy way to import your catalog data from a Cloud Storage. All you need is to provide a name of
the JSON file in the GCS bucket.

This type of import is useful when you need to import a large amount of items to your catalog in a single step.

You can find more information about different import types, their restrictions, and use cases in the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to
run it.

## Import products from the Cloud Storage source

The only reconciliation mode available for import from GCS is INCREMENTAL. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the import JSON source will not change.

To upload catalog data to the Cloud Storage bucket, create one or more JSON product files that do not exceed 2 GB each. You can set up to 100 JSON files in a single import request. For more information, refer to the [example of the product in JSON format](https://cloud.google.com/retail/docs/upload-catalog#json-format)

To check the example of an import product request, open **product/import_products_gcs.py**.

The field **```parent```** contains a **catalog name** along with a branch number you are going to import your
products to.

The field **```input_config```** defines the **GcsSource** as an import source.

To perform the product import, open terminal and run the command:

```bash
python product/import_products_gcs.py
```

## Response analysis

Once you have called the import products method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of product set in your Cloud Source.

The operation is completed when the field **```operation.done()```** is set to true. 

Check the result, one of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid product objects into the catalog.

Check the ```gcs_operation.metadata.success_count``` field to get the total number of the successfully imported products.

The number of failures during the product import is returned to the ```gcs_operation.metadata.failure_count``` field.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal. It should look like this: 

```
errors_config {
  gcs_prefix: "gs://products_catalog/error"
}
```

## Errors appeared during the importing

Now, let's try to import a few invalid product objects and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The title field is required, so if you remove it, you get the invalid product object. 
Another example of an invalid product is a product with an incorrect value of the ```product.availability``` field.
There is a **```products_for_import_some_invalid.json```** file in the Cloud Storage bucket containing such an invalid products.

Let's use it for import to get an error message.

Go to the code sample, assign a value of ```gcs_products_object``` to the file name:

```gcs_products_object = "products_for_import_some_invalid.json"```

Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case, the operation is considered as successful, and the ```gcs_operation.metadata.success_count``` field contains the number of the successfully imported products, which is "2".

There are two invalid products in the input JSON file, and the number of failures during the product import in the ```gcs_operation.metadata.failure_count``` field is also "2".

The ```operation.result``` field points to the errors bucket where you can find a json file with all the importing errors.

The errors are the following: 

```json
{"code":3,"message":"Invalid value at 'availability' (type.googleapis.com/google.cloud.retail.v2main.Product.Availability): \"INVALID_VALUE\"","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":1}}]}
{"code":3,"message":"The string in \"product.title\" is a valid UTF-8 string, but only contains space characters, control characters or non-characters. The invalid field value is:  .","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":2}}]}
```

## Errors appeared due to invalid request

Next, let's send invalid import request to make the operation fail. 

In the code sample, find the **```get_import_products_gcs_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message. It should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing andd import products from the Google Cloud Storage.

**Thank you for completing this tutorial!**