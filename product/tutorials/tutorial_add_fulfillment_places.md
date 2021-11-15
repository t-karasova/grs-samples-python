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

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Add fulfillment places 

To send the AddFulfillmentPlacesRequest you need to set the following fields:
 - ```product``` - the product name which inventory information you wnd to update,
 - ```type``` - the fulfillment type, you may set commonly used types (such as pickup in store and same day delivery) or custom types,
 - ```place_ids[]``` - the store IDs for each of the fulfillment type,
 - ```add_time``` - the time when the fulfillment updates are issued, used to prevent out-of-order updates on fulfillment information. If not provided, the internal system time will be used,
 - ```allow_missing``` - if set to true, and the Product is not found, the fulfillment information will still be processed and retained for at most 1 day and processed once the Product is created. 

Open **product/add_remove_fulfillment.py** and check the AddFulfillmentPlacesRequest.

To add the fulfillment places, open terminal and run the command:

```bash
python product/add_remove_fulfillment.py
```

Check the responses in the Terminal. As you can see, the product was initially created without the fulfillment information, 
then check the get_product() response, the fulfillment places 'store1', 'store2', 'store3' was added to the fulfillment type 'pickup-in-store'.

## Send out-of-order add_fulfillment_places request

The AddFulfillmentPlaces method allows the caller to specify an update time for when the request is issued.
This update time is compared against the latest update time recorded for the relevant inventory fields,
and the update is committed if and only if the update time is strictly after the latest update time.

Let's modify the ```add_fulfillment_request```, change the list of the **place_ids**.

Change the ```request_time``` value, set now() - 1 day:
```
request_time = datetime.datetime.now() - datetime.timedelta(days=1)
```

Run the code once again:
```bash
python product/add_remove_fulfillment.py
```

Check the product printed out in the Terminal, the fulfillment places information was not updated.

## Remove fulfillment places 

The RemoveFulfillmentPlacesRequest is pretty match the same as AddFulfillmentPlacesRequest,

Check the RemoveFulfillmentPlacesRequest in **product/add_remove_fulfillment.py**, get_remove_fulfillment_request() method.

Next, comment out the lines:
```
create_product(product_id)
add_fulfillment_places(product_name)
```

Uncomment **```remove_fulfillment_places(product_name)```**.

Run the code sample again with the command:

```bash
python product/add_remove_fulfillment.py
```

Check the responses in the Terminal. The **'store1'**  was remover from the list of fulfillment places for type 'pickup-in-store'.

## Send out-of-order remove_fulfillment_places request

The RemoveFulfillmentPlaces method also allows to set an update time,
if the value is strictly after the latest update time recorded for the relevant inventory fields, the update will be committed.

Next, modify the ```remove_fulfillment_request```, change the list of the **place_ids**, 
for example, you can add 'store3' value to the list in ```remove_fulfillment_request.place_ids```.

Set ```request_time``` value to yesterday's date:
```
request_time = datetime.datetime.now() - datetime.timedelta(days=1)
```

Uncomment the line ```delete_product(product_name)``` to clean up after these exercises. 

Run the code one more time:
```bash
python product/add_remove_fulfillment.py
```

Check the product printed out in the Terminal, the fulfillment places information was not updated.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to update the product fulfillment places using Retail API. We encourage you to 
practice in updating fulfillment information right here, in Cloud Shell environment.

**Thank you for completing this tutorial!**