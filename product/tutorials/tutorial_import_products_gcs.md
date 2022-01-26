<walkthrough-metadata>
  <meta name="title" content="Import products from Cloud Storage tutorial" />
  <meta name="description" content="Import a large number of items to your catalog in a single step." />
  <meta name="component_id" content="593554" />
</walkthrough-metadata>

# Import products from Cloud Storage tutorial

## Get started

The Retail API offers you an easy way to import your catalog data from Cloud Storage. All you need is to provide the name of
the JSON file in the Cloud Storage bucket.

This type of import is useful when you need to import a large number of items to your catalog in a single step.

You can find more information about different import types, their restrictions, and use cases in the [Retail API documentation](https://cloud.google.com/retail/docs/upload-catalog#considerations).

<walkthrough-tutorial-duration duration="5"></walkthrough-tutorial-duration>

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

To run a code sample from the Cloud Shell, you need to be authenticated using the service account credentials.

1. Login with your user credentials.
    ```bash
    gcloud auth login
    ```

1. Type `Y` and press **Enter**. Click the link in Terminal. A browser window should appear asking you to log in using your Gmail account.

1. Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

1. Upload your service account key JSON file and use it to activate the service account:

    ```bash
    gcloud iam service-accounts keys create ~/key.json --iam-account <YOUR_SERVICE_ACCOUNT_EMAIL>
    ```

    ```bash
    gcloud auth activate-service-account --key-file  ~/key.json
    ```

1. Set key as the GOOGLE_APPLICATION_CREDENTIALS environment variable to be used for requesting the Retail API:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
    ```

**Note**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

### Set the PROJECT_NUMBER and PROJECT_ID environment variables

Because you are going to run the code samples in your own Google Cloud project, you should specify the **project_number** and **project_id** as environment variables. It will be used in every request to the Retail API.

1. Find the project number and project ID in the Project Info card displayed on **Home/Dashboard**.

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

## Upload catalog data to Cloud Storage

There is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/products.json" regex="id">resources/products.json</walkthrough-editor-select-regex> file with valid products prepared in the `resources` directory.

The other file, <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/products_some_invalid.json" regex="id">resources/products_some_invalid.json</walkthrough-editor-select-regex>, contains both valid and invalid products. You will use it to check the error handling.

In your own project you should create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique. For convenience, you can name it `<YOUR_PROJECT_ID>_<TIMESTAMP>`.

1. To create the bucket and upload the JSON file, run the following command in the Terminal:
    ```bash
    python product/setup/products_create_gcs_bucket.py
    ```
1. Now you can see the bucket is created in the [Cloud Storage](https://console.cloud.google.com/storage/browser), and the file is uploaded. The name of the created Cloud Storage bucket is printed in the Terminal.

1. Copy the name and set it as the environment variable `BUCKET_NAME`:
    ```bash
    export BUCKET_NAME=<YOUR_BUCKET_NAME>
    ```

## Import products from the Cloud Storage source

The only reconciliation mode available for import from Cloud Storage is `INCREMENTAL`. That is, importing automatically creates new products and updates current products. Products already present in a catalog and missing from the import JSON source will not change.

To upload catalog data to the Cloud Storage bucket, you can create one or more JSON product files that do not exceed 2 GB each. You can set up to 100 JSON files in a single import request. For more information, see the [example of the product in JSON format](https://cloud.google.com/retail/docs/upload-catalog#json-format).

1. To check the example of an import product request, open <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_gcs.py" regex="# call the Retail API to import products">product/import_products_gcs.py</walkthrough-editor-select-regex>.

    The `parent` field contains a catalog name along with a branch number where products will be imported.

    If you are using products prepared for these tutorials from <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/products.json" regex="id">resources/products.json</walkthrough-editor-select-regex> file, you can use the defailt branch to import products to. But, if you are using custom products, change the default_branch, which is **0**, to another branch ID, for example **1**. In the search tutorials you will request `SearchService` to search for products in the default branch.

    The `input_config` field defines the `GcsSource` as an import source.

1. To perform the product import, open Terminal and run the command:
    ```bash
    python product/import_products_gcs.py
    ```

## Response analysis

After you have called the import products method from the Retail API, the import operation has started.

Importing can take a lot of time depending on the size of the product set.

The operation is completed when the field `operation.done()` is set to true.

1. Check the result. One of the following fields should be present:
    - `error`, if the operation failed.
    - `result`, if the operation was successful.

1. You have imported valid product objects into the catalog.

1. Check the `gcs_operation.metadata.success_count` field to get the total number of successfully imported products. The number of failures during the product import is returned in the `gcs_operation.metadata.failure_count` field.

1. Check the results printed out in the Terminal:
    ```terminal
    errors_config {
      gcs_prefix: "gs://products_catalog/error"
    }
    ```

## Errors appeared during the importing

Try to import some invalid product objects and check the error message in the operation response.

**Note**: The operation in this example will generate an error message, but will complete successfully.

The title field is required. If you remove it, you get the invalid product object.

Another example of an invalid product is a product with an incorrect value in the `product.availability` field.

There is a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/resources/products_some_invalid.json" regex="id">resources/products_some_invalid.json</walkthrough-editor-select-regex> file in the Cloud Storage bucket that contains some invalid products.

1. Open the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_gcs.py" regex="# TO CHECK ERROR HANDLING USE THE JSON WITH INVALID PRODUCT">code sample</walkthrough-editor-select-regex> and assign `gcs_products_object` value to the file name:
    ```
    gcs_products_object = "products_for_import_some_invalid.json"
    ```

1. Run the code sample and wait until the operation is completed:
    ```bash
    python product/import_products_gcs.py
    ```

Next, check the operation printed out in the Terminal.

## Errors appeared during importing: output analysis

If the operation is completed successfully, the `result` field will be displayed. Otherwise, an `error` field is displayed instead.

Check the operation printed out in the Terminal. The operation is considered **successful** and the `gcs_operation.metadata.success_count` field contains the number of successfully imported products, which is `2`.

There are two invalid products in the input JSON file, and the number of failures during the product import in the `gcs_operation.metadata.failure_count` field is `1`.

The `operation.result` field points to the errors bucket, where you can find a JSON file with all of the importing errors.

The error is the following:
```json
{"code":3,"message":"Invalid value at 'availability' (type.googleapis.com/google.cloud.retail.v2main.Product.Availability): \"INVALID_VALUE\"","details":[{"@type":"type.googleapis.com/google.protobuf.Struct","value":{"line_number":1}}]}
```

## Errors appeared due to invalid request

Next, send an invalid import request to check the error message.

1. Open the  <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/import_products_gcs.py" regex="# TO CHECK ERROR HANDLING PASTE THE INVALID CATALOG NAME HERE">get_import_products_gcs_request()</walkthrough-editor-select-regex> method, and uncomment the line with the `default_catalog` local variable with an invalid catalog name.

1. Run the code again with the following command:
    ```bash
    python product/import_products_gcs.py
    ```
1. Check the error message in the Terminal:
    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the importing products from Google Cloud Storage by yourself and try different combinations of various filter expressions.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
