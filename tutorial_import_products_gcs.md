# **Import Products From Cloud Storage Tutorial**

## Let's get started

Retail API offers you an easy way to import your catalog data from a Cloud Storage. All you need is to provide a name of
the JSON file in the GCS bucket.

This type of import is useful when you need to import a large amount of items to your catalog in a single step.

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

## Import products from Cloud Storage source

It is worth to mention that for import from GCS the only INCREMENTAL reconciliation mode is available, it means that
during the importing new products will be inserted and existing products will be updated, if there are products in a
catalog which are absent in the import source JSON they will remain unchanged.

To upload catalog data to the Cloud Storage bucket, you create one or more JSON files with producs, each file should be
less than 2 GB. In one import request you can set up to 100 JSON files. Please take a look at
an [example of the product in JSON format](https://cloud.google.com/retail/docs/upload-catalog#json-format)

Please open **product/import_products_gcs.py** and look at the example of import product request.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products.

The field ```input_config``` defines the **GcsSource** as an import source.

To perform the products import open terminal and run the command:

```bash
python product/import_products_gcs.py
```

## Response analysis

Once you have called the import products method of Retail API, the **import operation** has been started.

The importing may take some time depending on the size of products set in your Cloud Source.

When the field ```operation.done()``` is set with ```true``` that means the operation is finished. Now you can check the
result: there is exactly one of fields: ```error``` in case if the operation was failed or ```response``` if operation
is successful.

If the operation was successful you can unpack the response to **ImportProductsResponse** and see a sample of errors
encountered while processing the request in a field ```error_samples[]```.

```errors_config``` field points to the destination for the importing errors if it was set in the request.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from Google
Cloud Storage.

**Thank you for completing this tutorial!**
