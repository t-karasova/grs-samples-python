# **Import User Events From the Big Query Table Tutorial**

## Let's get started

Retail API offers you a convenient way to import user event data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive amounts of user events data with no limits.

To find more information about different import types, their restrictions, and use cases, check the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events#considerations)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to
run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Import user events from the BigQuery table

Before you import products to your catalog, you need to upload the data to the BigQuery table first. There are two ways to do it:

 - Create an [empty BigQuery table](https://cloud.google.com/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition)
  using the Retail schema, and create products in it using SQL.
 - Create a BigQuery table using the prepared JSON file with products. 

Then, import your data to the Retail API.

For this tutorial we have already created a BigQuery table, so you can use it in your Retail API import request.

To check the example of an import user events request, open **events/import_user_events_big_query.py**.

The field **```parent```** contains a **catalog name** along with a branch number you are going to import your
user events to.

The field **```input_config```** defines the **BigQuerySource** as an import source.

To perform the user events import, open terminal and run the command:

```bash
python events/import_user_events_big_query.py
```

## Response analysis

Once you have called the import user events method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of your BigQuery table.

The operation is completed when the field **```operation.done()```** is set to true. 

Check the result, one of the following fields should be present:
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

The ```type``` field is required and should have one of defined values, so if you set some invalid value, you get the invalid user event objects. 

There is a **```import_tutorial_invalid```** table in the BigQuery dataset that contains such invalid user events.

Let's use it for import to get an error message.

Go to the code sample, assign a value of ```table_id``` to the table name:

```table_id = "import_tutorial_invalid"```

Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case, the operation is considered as successful, and the ```big_query_operation.metadata.success_count``` field contains the number of the successfully imported events, which is "3".

There are one invalid user event in the input table, and the number of failures during the importing in the ```big_query_operation.metadata.failure_count``` field is also "1".

The ```operation.result``` field points to the errors bucket where you can find a json file with all the importing errors.

The errors are the following: 

```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 3
}
```

## Errors appeared due to invalid request

Next, let's send invalid import request to check the error message. 

In the code sample, find the **```get_import_events_big_query_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message. It should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing user events from the Big Query table.

**Thank you for completing this tutorial!**
