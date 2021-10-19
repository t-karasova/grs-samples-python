# **Import Products From the Cloud Storage Tutorial**

## Let's get started

Retail API offers you an easy way to import your catalog data from a Cloud Storage. All you need is to provide a name of
the JSON file in the GCS bucket.

This type of import is useful when you need to import a large amount of items to your catalog in a single step.

You can fing more information about different import types, their restrictions, and use cases in the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to
run it.

## Import products from the Cloud Storage source

The only reconciliation mode available for import from GCS is INCREMENTAL. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the import JSON source will not change.

To upload catalog data to the Cloud Storage bucket, create one or more JSON product files that do not exceed 2 GB each. You can set up to 100 JSON files in a single import request. For more information, refer to the [example of the product in JSON format](https://cloud.google.com/retail/docs/upload-catalog#json-format)

To check the example of an import product request, open **product/import_products_gcs.py**.

The field ```parent``` contains a **catalog name** along with a branch number you are going to import your
products to.

The field ```input_config``` defines the **GcsSource** as an import source.

To perform the products import, open terminal and run the command:

```bash
python product/import_products_gcs.py
```

## Response analysis

Once you have called the import products method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of product set in your Cloud Source.

Call the Operation Client to get the operation status. 

If the operation was successful, you can unpack the response to **ImportProductsResponse** and check a sample of errors
encountered while processing the request in the field ```error_samples[]```.

When set in the request, the ```errors_config``` field points to the destination for the importing errors.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from Google
Cloud Storage.

**Thank you for completing this tutorial!**
