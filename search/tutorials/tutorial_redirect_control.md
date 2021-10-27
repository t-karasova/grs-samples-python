# **Redirect Control Tutorial**

## Let's get started

Redirect Control lets you specify a URL to redirect the users to when they search for a specific query. 
Since we are not able to check its effect on the Evaluate page, we will test it in the Cloud Shell 
using our Python code samples. Make sure that you have created and attached the Redirect Control
to the serving config. You can find the step-by-step instruction on how to do it in the Creating and Managing Controls video tutorial.

**Time to complete**: About 4 minutes

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to run it.


## Configuring search to use Redirect Control

Open Editor to see all the code samples and choose **search_simple_query.py**. Make sure that ```project_number``` variable
is set:

```project_number = "<YOUR_PROJECT_NUMBER>"```

Now you need to change the query variable to match the one you configured as query term in
your Redirect Control:

```title_query = "<YOUR_QUERY_TERM>"```

Next step is to configure the Search Service to use the serving config that has the redirect control attached.

## Configuring search to use serving config

In the code sample, find `default_search_placement` variable.

Before applying the changes, it should look like this:

```default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/default_search"```

You need to replace the `default_search` part to the ID of your serving config.

After applying the changes, it should look like this:

```default_search_placement = "projects/" + project_number + "/locations/global/catalogs/default_catalog/placements/<YOUR_SERVING_CONFIG_ID>"```

## Redirect control console output

We want to check the effect of the Redirect Control printed in our console. 

Let's go to the bottom of the code sample and find a following code fragment:

```print("---search response---")```

Add the following piece of code below:

```print("redurect uri: " + search_response.redirect_uri)```

Great! We're done in the editor. Let's go  back to the Terminal.

## Authentication

To run a code sample from the Cloud Shell, you need to authenticate. Luckily, Google Cloud
makes it easy to use the Application Default Credentials. Open Terminal and run the following command:
```bash
gcloud auth application-default login
```

Type 'Y' and press Enter. Click on the link in Terminal. A browser window should open asking you to login using your gmail account.
Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

Now we can run the code sample and check the Redirect Control in action.

## Testing the Redirect Control

To execute our code sample, run the following command:
```bash
python cloudshell_open/grs-samles-python/search_simple_query.py
```
You should see the redirect URL printed in the Terminal.

**Thank you for completing this tutorial!**
