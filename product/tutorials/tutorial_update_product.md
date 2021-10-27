# **Update Product Tutorial**

## Let's get started

To fill the catalog or to update a massive amount of products we recommend to use Import products method. 
However sometimes you may need to make some detached changes in your product catalog. So Retail API provides you such ability
exposing create_product, get_product, update_product, and delete_product methods.

In this tutorial you will **update product in a catalog**.

[Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#json-format)

**Time to complete**: About 3 minutes

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

## Update a product

To update a product you should send a **UpdateProductRequest** to Retail API with the following required fields specified:
```product``` the product object to be updated or created (depending on the ```allow_missing``` value the product can be created if missing).
```update_mask``` - indicates which fields in the provided product to update.
```allow_missing``` - if set to true, and the Product is not found, a new Product will be created.

You can find the update product request example in a **update_product.py**

When you run this code sample, first a product will be created in a catalog, then it will be updated using a prepared request.

To run this code sample, open terminal and run the command:

```bash
python product/update_product.py
```

The Retail API returns the updated product as a response.

Check the product in the response, as you can see only the product fields listed in the request field ```update_mask``` were actually updated, the other fields were not changed even if provided in the product object in the UpdateProductRequest.

## Error handling

If you send a request without one of required fields or if the field format is incorrect you will get an error message.
Let's now remove the product field ```name``` and send this request again. The expected error message should be like:

TODO
```[PUT THE ERROR MESSAGE HERE]```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to update a product in a catalog using Retail API.

**Thank you for completing this tutorial!**
