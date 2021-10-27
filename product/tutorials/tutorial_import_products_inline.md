# **Import Products From Inline Source Tutorial**

## Let's get started

The inline importing is a convenient way to make bulk changes in a catalog, such as:

- import some amount of products, no more than 100 at a time,
- update some products set,
- make fast and frequent changes of products quantity or price or any other field.

To import your products into a catalog inline you should prepare the ```product_inline_source``` object which is a set
of products. Each product should be provided in a JSON format as a standalone line (one product per line with line breaks as a
delimiter). To find an example of a product in JSON format, refer to
the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#json-format)

To find more information about different import types, their restrictions, and use cases, refer to the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations)

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and
run it.

## Import products from inline source

The only reconciliation mode available for inline import is INCREMENTAL. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the import JSON source will not change.

To check the example of an import product request, open **product/import_products_inline_source.py**.

The field ```parent``` contains a **catalog name** along with a branch number to which you are going to import your
products to.

The field ```input_config``` defines the **ProductInlineSource** as an import source.

To use generated products in this tutorial, check the ```get_products()``` function first.

To perform the products import, open terminal and run the command:

```bash
python product/import_products_inline_source.py
```

## Response analysis

Once you have called the import products method, the **import operation** has started.

Importing may take some time depending on the size of product set in your inline source.

The operation is completed when the field ```operation.done()``` is set to true. Check the result, one of the following fields should be present:
 - ```error```, if the operation failed, or
 - ```response```, if the operation was successful.

You have imported valid product objects to the catalog, so the operation should be successful, and the operation object should contain a field ```response```. 

Check the ```response``` field in the operation object returned and printed to the Terminal. 
The ```error_samples[]``` field should be empty.

## Error handling

Now, let's try to import a couple of product objects with one invalid and check the error message in the operation response, note that in this case the operation itself is considered as successful.

The field title is a required field, so if you remove it, you will get invalid product object.
Go to the code sample and comment or remove the ```line product1.title = "#IamRemarkable Pen"```

Now, run the code sample and wait till the operation will be done. Check the operation printed out to the Terminal.
The operation if completed, it is successful, so you can find a field ```response```, otherwise there would be a field ```error``` instead.
Check the error message in the ```response.error_samples``` list, it should point on the invalid product object and its field which caused a problem, in our case the message should be:

//TODO
//[PUT ERROR MESSAGE HERE]

Next, let's send invalid import request to get failed operation. 

Go tho the code sample and in the method ```get_import_products_inline_request```  and add there a local variable "default_catalog" with some invalid catalog name.

Now run the code one more time and check the operation object, now it contains the field ```error``` instead of ```response```. The error message should be the following:

//TODO
//[PUT ERROR MESSAGE HERE]

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for import and how to import some amount of
products directly inline.

**Thank you for completing this tutorial!**
