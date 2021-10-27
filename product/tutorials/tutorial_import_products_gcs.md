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

The operation is completed when the field ```operation.done()``` is set to true. Check the result, one of the following fields should be present:
 - ```error```, if the operation failed, or
 - ```response```, if the operation was successful.

You have imported valid product objects to the catalog, so the operation should be successful, and the operation object should contain a field ```response```. 

Check the ```response``` field in the operation object returned and printed to the Terminal. 
The ```error_samples[]``` field should be empty.

## Error handling

Now, let's try to import a couple of invalid product objects and check the error message in the operation response, note that in this case the operation itself is considered as successful.

The field title is a required field, so if you remove it, you will get invalid product object. There is a ```invalid_products_for_import.json``` in the Cloud Storage bucket which contains such an invalid product.
Let's use it for import to get an error message.

Go to the code sample assign the file name as a value of gcs_products_object:

```gcs_products_object = "invalid_products_for_import.json"```

Now, run the code sample and wait till the operation will be done. Check the operation printed out to the Terminal.
The operation if completed, it is successful, so you can find a field ```response```, otherwise there would be a field ```error``` instead.

Check the error message in the ```response.error_samples``` list, it should point on the invalid product object and its field which caused a problem, in our case the message should be:

//TODO
//[PUT ERROR MESSAGE HERE]

Next, let's send invalid import request to get failed operation. 

Go tho the code sample and in the method ```get_import_products_gcs_request```  and add there a local variable "default_catalog" with some invalid catalog name.

Now run the code one more time and check the operation object, now it contains the field ```error``` instead of ```response```. The error message should be the following:

//TODO
//[PUT ERROR MESSAGE HERE]

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import products from Google
Cloud Storage.

**Thank you for completing this tutorial!**
