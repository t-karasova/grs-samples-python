# **Update Inventory. Add Fulfillment Places**

## Let's get started

Changes to a product's inventory information may occur much more frequently than changes to its catalog information.

Fulfillment availability for some specific places may change, and you may decide to issue updates that describe this change instead of using the UpdateProduct method to re-specify the entire product's fulfillment information.

In such cases, the AddFulfillmentPlaces and RemoveFulfillmentPlaces methods can be used to incrementally update a product's fulfillment changes based on which place IDs are added or removed for a given fulfillment type.

These methods are asynchronous because of downstream optimizations that support hundreds of concurrent updates per product, without sacrificing performance.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/inventory-updates#inventory-update-methods)


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

## Add fulfillment places 

Even if the product does not exist yet, the inventory information can be stored for when the product is eventually created.
Then, after the product will be added to the catalog it will be associated with the latest fulfillment information. 

Open **product/add_fulfillment.py** and check the AddFulfillmentPlacesRequest.

To add tje fulfillment places, open terminal and run the command:

```bash
python product/add_fulfillment.py
```

## Create a product. 

Now, when the fulfillment info is created let's create a product with the corresponding product_name and check the fulfillment information will be associated with this product.


## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to create a product in a catalog using Retail API. We encourage you to 
practice in creating products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
