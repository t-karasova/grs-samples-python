# Import user events from the BigQuery table tutorial

## Introduction

The Retail API lets you to import user event data from previously loaded BigQuery table.

Using BigQuery table allows you to import a massive number of user events data with no limits.

For more information about different import types, their restrictions, and use cases, see the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events#considerations).

<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API tutorial you run.
Otherwise, you can skip it.

### Select your project and enable the Retail API

Google Cloud organizes resources into projects. This lets you
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet or you're not the owner of an existing one, you can
[create a new project](https://console.cloud.google.com/projectcreate).

After the project is created, set your PROJECT_ID to a ```project``` variable.
1. Run the following command in Terminal:
    ```bash
    gcloud config set project <YOUR_PROJECT_ID>
    ```

1. Check that the Retail API is enabled for your project in the [Admin Console](https://console.cloud.google.com/ai/retail/).

### Set up authentication

To run a code sample from the Cloud Shell, you need to authenticate. To do this, use the Application Default Credentials.

1. Set your user credentials to authenticate your requests to the Retail API

    ```bash
    gcloud auth application-default login
    ```

1. Type `Y` and press **Enter**. Click the link in Terminal. A browser window should appear asking you to log in using your Gmail account.

1. Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

1. Run the code sample and check the Retail API in action.

**Note**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

### Set the PROJECT_NUMBER and PROJECT_ID environment variables

Because you are going to run the code samples in your own Google Cloud project, you should specify the **project_number** and **project_id** as environment variables. It will be used in every request to the Retail API.

1. You can find these values in the Project Info card displayed on **Home/Dashboard**.

1. Set **project_number** with the following command:
    ```bash
    export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
    ```
1. Set **project_id** with the following command:
    ```bash
    export PROJECT_ID=<YOUR_PROJECT_ID>
    ```

### Install Google Cloud Retail libraries

To run Python code samples for the Retail API tutorial, you need to set up your virtual environment.

1. Run the following commands in a Terminal to create an isolated Python environment:
    ```bash
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
    ```
1. Next, install Google packages:
    ```bash
    pip install google
    pip install google-cloud-retail
    pip install google.cloud.storage
    pip install google.cloud.bigquery

    ```

## Clone the Retail code samples

This step is required if this is the first Retail API tutorial you run.
Otherwise, you can skip it.

Clone the Git repository with all the code samples to learn the Retail features and check them in action.

<!-- TODO(ianan): change the repository link -->
1. Run the following command in the Terminal:
    ```bash
    git clone https://github.com/t-karasova/grs-samples-python.git
    ```

    The code samples for each of the Retail services are stored in different directories.

1. Go to the ```grs-samples-python``` directory. This is our starting point to run more commands.
    ```bash
    cd grs-samples-python
    ```

## Prepare user events for importing

There is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events.json" regex="id">resources/user_events.json</walkthrough-editor-select-regex> file with valid user events prepared in the `resources` directory.

The other file, <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events_some_invalid.json" regex="id">resources/user_events_some_invalid.json</walkthrough-editor-select-regex>, contains both valid and invalid user events. You will use it to check the error handling.

You can use this file in the tutorial, or, if you want to use your own data, you should update the names of a bucket and a JSON files in the code samples.

You can import events that aren't older than 90 days into the Retail catalog. Otherwise, the import will fail.

To keep our historical user evens more recent, update the timestamps in the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events.json" regex="id">user_events.json</walkthrough-editor-select-regex> and <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events_some_invalid.json" regex="id">user_events_some_invalid.json</walkthrough-editor-select-regex> files.

1. Run this script in the Terminal to get the user events with yesterday's date:
    ```bash
    python  setup/update_user_events_json.py
    ```

Now, your data are updated and ready to be deployed to the Cloud Storage.

## Create the BigQuery table and upload user events

To upload the data to the BigQuery table you need to create a dataset first, then create table with specific user events data schema.

Next, upload data to the table from prepared JSON file. The data in the file should correspond the user events schema as well.

<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events.json" regex="id">resources/user_events.json</walkthrough-editor-select-regex> file should be uploaded to the `user_events` dataset, `events` table.

<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events_some_invalid.json" regex="id">resources/user_events_some_invalid.json</walkthrough-editor-select-regex> that contains some invalid user events along with valid ones should be uploaded to the `user_events` dataset, `events_some_invalid` table. This table will be used to demonstrate the error handling.

1. Run the following code in the Terminal to create tables and import data:
    ```bash
    python events/setup/events_create_bigquery_table.py
    ```
The dataset `user_events` with both tables are created, check them in [Cloud Console](https://console.cloud.google.com/bigquery).

## Create the BigQuery table and upload products from UI admin console

In case if you don't have permissions to run the ```bq``` command and performing the previous step you have got "Permission denied" error, you can try the other way to create the table and upload your data.


### Upload catalog data to Cloud Storage

After you have updated the timestamps in <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events.json" regex="id">resources/user_events.json</walkthrough-editor-select-regex> and <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events_some_invalid.json" regex="id">resources/user_events_some_invalid.json</walkthrough-editor-select-regex> files you can proceed with uploading these data to Cloud Storage.

In your own project create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique, for convenience it can be named as `<YOUR_PROJUCT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file run the following command in the Terminal:
    ```bash
    python events/setup/events_create_gcs_bucket.py
    ```
    The bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the file is uploaded.

1. Save the name of the created Cloud Storage bucket printed in the Terminal for the next steps.

### Create the BigQuery table and upload user events

1. Go to the [BigQuery in Cloud Console](https://console.cloud.google.com/bigquery).

1. In the Explorer panel you see the list of your projects.

1. Click the View actions button next to the current project name and chose **Create Dataset** option.

1. Set the Dataset ID and click **Create Dataset**.

1. Expand node of your current project.

1. Click View actions button next to your new dataset and choose **Create table**.

1. Set the Source: in the field **Create table from** choose **Google Cloud Storage** option.

1. Click **Browse** in the **Select file from GCS bucket** and choose the bucket you have created on the previous step.

1. Choose the **`user_events.json`** and click **Select**.

1. Set the **Destination** field **Table** with a value ```events```.

1. Provide a table **Schema**: activate toggle **Edit as a text** and paste in the field the schema which you can find in the **`events/resources/events_schema.json`** file.

1. Click **Create table**.

As a result the BigQuery table is created. You can proceed and import user events to the catalog.

## Import user events to the Retail catalog from the BigQuery table

You have already created a BigQuery table, so you can use it in your Retail API import request.

1. To check the example of an import user events request, open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/events/import_user_events_big_query.py" regex="# get import user events from big query request">events/import_user_events_big_query.py</walkthrough-editor-select-regex> file.

    The `parent` field in the `ImportUserEventsRequest` method contains a catalog name along with a branch number you are going to import your user events to. You can import user events to the default branch. However, if you're using custom user events, change the default branch, which is `0`, to another branch ID, for example `1`.

    The `input_config` field defines the `BigQuerySource` method as an import source.

1. To perform the user events import, open Terminal and run the command:
    ```bash
    python events/import_user_events_big_query.py
    ```

## Response analysis

Once you have called the import user events method from the Retail API, the import operation starts.

Importing can take some time depending on the size of your BigQuery table.

The operation is completed when the **```operation.done()```** field is set to true.

1. Check the result. One of the following fields should be present:
    - `error`, if the operation failed.
    - `result`, if the operation was successful.

    You have imported valid user event objects into the catalog.

1. Check the `big_query_operation.metadata.success_count` field to get the total number of the successfully imported events.

    The number of failures during the import is returned to the `big_query_operation.metadata.failure_count` field.

    The operation is successful, and the operation object contains a `result` field.

1. Check it printed out in the Terminal:
    ```terminal
    errors_config {
      gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
    }
    import_summary {
      joined_events_count: 4
    }
    ```

## Errors appeared during the importing

Try to import one invalid user event object and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The `type` field is required and should have one of [defined values](https://cloud.google.com/retail/docs/user-events#types). That is, if you set some invalid value, you get the invalid user event object.

1. Create one more `import_tutorial_invalid` BigQuery table in the same dataset that contains such invalid user events.

    Follow the instructions described in **Upload user events data to the Cloud Storage bucket** and **Create the BigQuery table with the user events data** steps and use the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/user_events_some_invalid.json" regex="id">resources/user_events_some_invalid.json</walkthrough-editor-select-regex> file as a source.

1. Go to the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/events/import_user_events_big_query.py" regex="# TO CHECK ERROR HANDLING USE THE TABLE OF INVALID USER EVENTS:">events/import_user_events_big_query.py</walkthrough-editor-select-regex> file and assign a value of `table_id` to the table name:
    ```table_id = "events_some_invalid"```

1. Run the code sample and wait till the operation is completed:
    ```bash
    python events/import_user_events_big_query.py
    ```

Next, check the operation printed out to the Terminal.

## Errors appeared during importing: output analysis

If the operation is completed successfully, you can find a `result` field. Otherwise, there would be an `error` field instead.

In this case, the operation is considered as successful, and the `big_query_operation.metadata.success_count` field contains the number of the successfully imported events, which is `3`.

There is one invalid user event in the input table, and the number of failures during the importing in the `big_query_operation.metadata.failure_count` field is also `1`.

The `operation.result` field points to the errors bucket where you can find a JSON file with all the importing errors.

The response is the following:
```terminal
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 3
}
```

## Errors appeared due to an invalid request

Next, send an invalid import request to check the error message.

1. Open the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/events/import_user_events_big_query.py" regex="# TO CHECK ERROR HANDLING PASTE THE INVALID CATALOG NAME HERE:">events/import_user_events_big_query.py</walkthrough-editor-select-regex> file and find the `get_import_events_big_query_request()` method, and add there a local variable `default_catalog` with some invalid catalog name.

1. Run the code again and check the error message:
    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to prepare data and to test the importing user events from BigQuery table by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
