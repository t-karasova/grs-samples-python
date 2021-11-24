# **Import User Events From the BigQuery Table Tutorial**

## Let's get started

The Retail API offers you a convenient way to import user event data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive amounts of user events data with no limits.

To find more information about different import types, their restrictions, and use cases, check the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events#considerations)

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

You should remember that you can only import to Retail catalog events which are **NOT older than 90 days** otherwise the import will fail.

To keep our historical user evens more recent let's update the timestamps in the import_user_events_tutorial.json. 
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

## Create the BigQuery table with the user events data

In your own Google Platform project go to the [BigQuery](pantheon.corp.google.com/bigquery)

Click three dots icon near your project name in the "Explorer" panel, and chose **"Create dataset"** option. Set the Dataset Id as "user_events" and click "Create Dataset".

In the newly created dataset click "Create Table" , chose **Google Cloud Source** option as the Source, select **"import_user_events"** bucket and  **"import_user_events_tutorial.json"** file, click "Select".

Set the table name as **"import_tutorial"**

Now, let's specify the table schema. In the Schema section turn on the "Edit as a text" option, copy the schema from the **"events_schema.json"** file and paste in the text field.
Press Create.

## Import user events to the Retail catalog from the BigQuery table

You have already created a BigQuery table, so you can use it in your Retail API import request.

To check the example of an import user events request, open **events/import_user_events_big_query.py**.

Set the ```project_id``` field, you can find the ```project_id``` in the **Home/Dashboard/Project Info card**.

The **```parent```** field in the **ImportUserEventsRequest** contains a **catalog name** along with a branch number you are going to import your
user events to.

The **```input_config```** field defines the **BigQuerySource** as an import source.

To perform the user events import, open Terminal and run the command:

```bash
python events/import_user_events_big_query.py
```

## Response analysis

Once you have called the import user events method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of your BigQuery table.

The operation is completed when the **```operation.done()```** field is set to true. 

Check the result. One of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid user event objects into the catalog.

Check the ```big_query_operation.metadata.success_count``` field to get the total number of the successfully imported events.

The number of failures during the import is returned to the ```big_query_operation.metadata.failure_count``` field.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal. It should look like this: 

```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 13500
}
```

## Errors appeared during the importing

Now, let's try to import one invalid user event object and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The ```type``` field is required and should have one of [defined values](https://cloud.google.com/retail/docs/user-events#types). That is, if you set some invalid value, you get the invalid user event object. 

You should create one more BigQuery table **```import_tutorial_invalid```** in the same dataset, dataset that contains such invalid user events.

Follow the instructions described in **Upload user events data to the Cloud Storage bucket** and **Create the BigQuery table with the user events data** steps, use the **events/import_user_events_invalid.json** as a source.

Let's import from the table with one invalid user event to get an error message.

Go to the code sample, assign a value of ```table_id``` to the table name:

```table_id = "import_tutorial_invalid"```

Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case, the operation is considered as successful, and the ```big_query_operation.metadata.success_count``` field contains the number of the successfully imported events, which is "3".

There is one invalid user event in the input table, and the number of failures during the importing in the ```big_query_operation.metadata.failure_count``` field is also "1".

The ```operation.result``` field points to the errors bucket where you can find a JSON file with all the importing errors.

The response is the following: 

```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 3
}
```

## Errors appeared due to an invalid request

Next, let's send an invalid import request to check the error message. 

In the code sample, find the **```get_import_events_big_query_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message. It should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing user events from the BigQuery table.

**Thank you for completing this tutorial!**
