# **Import User Events From the Cloud Storage Tutorial**

## Let's get started

The Retail API offers you an easy way to import your user event data from a Cloud Storage. All you need is to provide a name of
the JSON file in the GCS bucket.

This type of import is useful when you need to import a large amount of items to your catalog in a single step.

You can find more information about different import types, their restrictions, and use cases in the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a Terminal:
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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell Terminal to
run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable. It will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Upload user events data to the Cloud Storage bucket

We have prepared a JSON file with a bunch of valid user events in the "events" directory: 

**events/import_user_events_tutorial.json**

You can use this file in the tutorial, or, if you want to use your own data, you should update the names of a bucket and a JSON file in the code samples.

You can import events that are **NOT older than 90 days** into the Retail catalog. Otherwise, the import will fail.

To keep our historical user evens more recent, update the timestamps in the **import_user_events_tutorial.json** file. 
Run this script in a Terminal, and you will get the user events with yesterday's date:

```bash
python  events/update_user_events_json.py
```

Now, your data are updated and ready to be deployed to the Cloud Storage.
In your own Google Platform project go to the [Cloud Storage](pantheon.corp.google.com/storage/browser)

Click "Create Bucket" button, give it a name **import_user_events**, and press "Create".

  *You can use your own bucket, but you should then update all references to your data in code.

Next, from the Cloud Shell Terminal run the following command:
```
gsutil cp events/import_user_events_tutorial.json gs://import_user_events
```
Now you can see the file is uploaded to the Cloud Storage bucket.

## Import user events to the Retail catalog from the Cloud Storage source

To check the example of an import user events request, open **events/import_user_events_gcs.py**.

The **```parent```** field in the **ImportUserEventsRequest** contains a **catalog name** along with a branch number you are going to import your
user events to.

The **```input_config```** field defines the **GcsSource** as an import source.

To perform the user events import, open Terminal and run the command:

```bash
python events/import_user_events_gcs.py
```

## Response analysis

Once you have called the import user events method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of user events set in your Cloud Source.

The operation is completed when the **```operation.done()```** field is set to true. 

Check the result. One of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid user event objects into the catalog.

Check the ```gcs_operation.metadata.success_count``` field to get the total number of the successfully imported events.

The number of failures during the import is returned to the ```gcs_operation.metadata.failure_count``` field.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal. It should look like this: 

```
errors_config {
  gcs_prefix: "gs://import_user_events/error"
}
import_summary {
  joined_events_count: 13500
}
```

## Errors appeared during the importing

Now, let's try to import a few invalid user event objects and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The ```type``` field is a required and should have one of [defined values](https://cloud.google.com/retail/docs/user-events#types), so if you set some invalid value, you get the invalid user event objects. 

There is a **```import_user_events_invalid.json```** file in the **events directory** containing such an invalid user events.

Let's upload it to the GCS as you did it before, repeat **Upload user events data to the Cloud Storage bucket** step for this file.

Now, import the invalid user event to get an error message.

Go to the code sample, assign a value of ```gcs_events_object``` to the file name:

```gcs_events_object = "import_user_events_invalid.json"```

Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case, the operation is considered as successful, and the ```gcs_operation.metadata.success_count``` field contains the number of the successfully imported events, which is "3".

There are two invalid user events in the input JSON file, and the number of failures during the importing in the ```gcs_operation.metadata.failure_count``` field is also "1".

The ```operation.result``` field points to the errors bucket where you can find a JSON file with all the importing errors.

The response is the following: 

```
errors_config {
  gcs_prefix: "gs://import_user_events/error"
}
import_summary {
  joined_events_count: 3
}
```

## Errors appeared due to an invalid request

Next, let's send an invalid import request to check the error message. 

In the code sample, find the **```get_import_events_gcs_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message. It should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing user events from the Google Cloud Storage.

**Thank you for completing this tutorial!**
