<walkthrough-metadata>
  <meta name="title" content="Create/Get/Update/Delete product tutorial" />
  <meta name="description" content="How to use Retail API Product Service methods" />
  <meta name="component_id" content="593554" />
</walkthrough-metadata>

# Create/Get/Update/Delete product tutorial

## Introduction

In this tutorial you will learn how to use Retail API Product Service methods, which are exposed to perform the following methods:
- create_product
- get_product
- update_product
- delete_product

You will start with creating a simple product, then call the `get product` method. Next you will update some product fields, and finally remove the product from the catalog.

For more information about managing catalog information, see the [Retail API documentation](https://cloud.google.com/retail/docs/manage-catalog).

<walkthrough-tutorial-duration duration="5"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API Tutorial you run.
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

### Create service account

To access the Retail API you must create a service account.

1. To create service account follow this [instruction](https://cloud.google.com/retail/docs/setting-up#service-account)

1. Find your service account on the [IAM page](https://console.cloud.google.com/iam-admin/iam),
   click `Edit` icon and add the roles 'Storage Admin' and 'BigQuery Admin. It may take a while for the changes to take effect.

1. Copy the service account email in the field Principal.

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

This step is required if this is the first Retail API Tutorial you run.
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

## Product object overview

The required product fields are:

- `name`—a full resource name of the product, which is:
    ```none
    projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
    ```
- `id`—product identifier, which is the final component of the product name.
- `type`—the type of the product. The default value is `PRIMARY`.
- `primary_product_id`—a variant group identifier required for `VARIANT` products.
- `categories[]`—names of categories that the product belongs to. This can represent different category hierarchies.
- `title`—the product title that will be visible to a customer.

## Generate a simple product object

In this tutorial you will create a simple `PRIMARY` product presented in JSON format:

```json
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/crud_product_id",
  "id": "crud_product_id",
  "type": "PRIMARY",
  "categories": [
    "Speakers and displays"
  ],
  "brands": [
    "Google"
  ],
  "title": "Nest Mini",
  "availability": "IN_STOCK",
  "price_info": {
    "price": 30.0,
    "original_price": 35.5,
    "currency_code": "USD"
  }
}
```

Open the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# generate product for update">crud_product.py</walkthrough-editor-select-regex> code sample and check this product generation with the `generate_product()` method.

## Create a product request

1. To create a product, send a `CreateProductRequest` request to Retail API with the following required fields specified:
    - `product`—the product object you want to create
    - `product_id`—product ID
    - `parent`—a branch name in a catalog where the product will be created

1. Check the `CreateProductRequest` request along with the Retail API call in a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# create product">`create_product()`</walkthrough-editor-select-regex> method.

1. Comment out <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# call the methods">the lines</walkthrough-editor-select-regex> with the following calls: `get_product()`, `update_product()`, and `delete_product()`. These actions will be checked in the next steps.

1. To create a product, run the sample in the Terminal using the command:
    ```bash
    python product/crud_product.py
    ```

    The Retail API returns a created product as a response.

## Get a product

To build the `GetProductRequest` request, only the `name` field is required. You should pass the full resource name of the product, which is:
    ```
    projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
    ```

1. You can find the `GetProductRequest` example in a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# get product">`get_product()`</walkthrough-editor-select-regex> method.

1. Comment out <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# call the methods">the lines</walkthrough-editor-select-regex> with the following calls: `create_product()`, `update_product()`, and `delete_product()`. These actions were already checked or will be checked in the next steps.

1. Uncomment the line with the `get_product()` method call.

1. To get a product, run the sample in the Terminal using the command:
    ```bash
    python product/crud_product.py
    ```

    The Retail API returns the requested product with all product fields. The `product.retrievable_fields` value, which defines the displayed product fields in the search response, won't affect the product fields in the result.

## Update a product request

To update a product you should send an `UpdateProductRequest` request to the Retail API with the following required fields specified:
 - `product`—the product object to be updated or created (depending on the  `allow_missing` value, the product can be created if it's missing).
 - `update_mask`—indicates which fields in the provided product should be updated.
 - `allow_missing`—if the value is set to `true`, and the product is not found, a new product is created.


## Prepare data for the update request

To update each of its fields, you need to set the product object in a catalog to the `product` request field.

Take a look at the `generate_product_for_update()` method that returns the product object with updated fields except for these fields: `name`, `id`, and `type`—these fields are immutable.

```py
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/<PRODUCT_ID>", #cannot be updated , should point to existent product
  "id": "<PRODUCT_ID>", #cannot be updated
  "type": "PRIMARY", #cannot be updated
  "categories": [
    "Updated Speakers and displays"
  ],
  "brands": [
    "Updated Google"
  ],
  "title": "Updated Nest Mini",
  "availability": "OUT_OF_STOCK",
  "price_info": {
    "price": 20.0,
    "original_price": 55.5,
    "currency_code": "EUR"
  }
}
```

1. Check the `UpdateProductRequest` example in the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# update product">`update_product()`</walkthrough-editor-select-regex> method.

1. Comment out <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# call the methods">the lines</walkthrough-editor-select-regex> with the following calls: `create_product()`, `get_product()`, `delete_product()`. These actions were already checked or will be checked in the next steps.

1. Uncomment the line with the `update_product()` method call.

1. To update a product, run the sample in the Terminal using the command:
    ```bash
    python product/crud_product.py
    ```

    In the Retail API response an updated product is returned.

## Delete a product

To build the `DeleteProductRequest` request, only the `name` field is required.

You should use the full resource name of a product, such as:
```
projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
```

1. Check the `DeleteProductRequest` example in the <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# delete product">`delete_product()`</walkthrough-editor-select-regex> method.

1. Comment out <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/product/crud_product.py" regex="# call the methods">the lines</walkthrough-editor-select-regex> with the following calls: `create_product()`, `get_product()`, and `update_product()`. These actions were already checked or will be checked in the next steps.

1. Uncomment the line with the `delete_product()` method call.

1. To remove a product, run the sample in the Terminal using the command:
    ```bash
    python product/crud_product.py
    ```

    There is no return value for this method.
1. To check if the product was successfully removed, you need to remove the product one more time.
    ```bash
    python product/crud_product.py
    ```

    You should see the following error message:
    ```terminal
    google.api_core.exceptions.NotFound: 404 Product with name "projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>" does not exist.
    ```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We encourage you to test the managing products by yourself.

<walkthrough-inline-feedback></walkthrough-inline-feedback>
