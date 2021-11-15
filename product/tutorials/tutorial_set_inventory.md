# **Set Inventory**

## Let's get started

Changes to a product's inventory information may occur much more frequently than changes to its catalog information.

You may decide to issue inventory updates instead of updating entire product.

In such cases, the **```SetInventory```** method can be used.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/inventory-updates#non-incremental-updates)


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

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Set inventory 

To send the SetInventoryRequest you need to set the following fields:
 - ```inventory``` - the inventory information to update. The allowable fields to update are: 
    * ```Product.price_info```
    * ```Product.availability``` 
    * ```Product.available_quantity``` 
    * ```Product.fulfillment_info```
 - ```set_mask``` - indicates which inventory fields in the provided Product to update,
 - ```set_time``` - the time when the request is issued, used to prevent out-of-order updates on inventory fields with the last update time recorded,
 - ```allow_missing``` - if set to true, and the Product is not found, the fulfillment information will still be processed and retained for at most 1 day and processed once the Product is created. 

Open **product/set_inventory.py** and check the SetInventoryRequest.

To add the fulfillment places, open terminal and run the command:

```bash
python product/set_inventory.py
```

Check the responses in the Terminal. As you can see, the product was initially created with some **price_info** and **availability** information, 
then check the get_product() response, to ensure that the product inventory information was successfully updated.


## Send out-of-order SetInventory request

The SetInventory method allows the caller to specify an update time for when the request is issued.
This update time is compared against the latest update time recorded for the relevant inventory fields,
and the update is committed if and only if the update time is strictly after the latest update time.

Let's modify some of product fields values, for example price.

Change the ```set_inventory_request``` - set ```request_time``` value to yesterday's date:
```
request_time = datetime.datetime.now() - datetime.timedelta(days=1)
```

Run the code once again:
```bash
python product/set_inventory.py
```

Check the product printed out in the Terminal, the inventory information was not updated.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to update the product inventory information using Retail API. We encourage you to 
practice in updating product inventory right here, in Cloud Shell environment.

**Thank you for completing this tutorial!**
