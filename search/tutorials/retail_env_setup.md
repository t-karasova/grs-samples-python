# Getting started with Google Cloud Retail (Python)

<walkthrough-disable-features toc></walkthrough-disable-features>

#


Learn how to call the Google Cloud Retail API using client libraries:

1.  Enable the Retail API in a Google Cloud project.

2.  Set up authentication.

3.  Use code samples to call the Retail API.

Estimated time to complete:
<walkthrough-tutorial-duration duration="3"></walkthrough-tutorial-duration>

To get started, click **Start**.

## Select your project

Google Cloud Platform organizes resources into projects. This allows you to
collect all the related resources for a single application in one place.

<walkthrough-project-setup billing="true"></walkthrough-project-setup>

To learn how to enable the Cloud Translation API, click **Next**.

## Enable the Retail API

Enable the Retail API by clicking **Enable APIs**:

<walkthrough-enable-apis apis="retail.googleapis.com">
    </walkthrough-enable-apis>

To learn how to set up your application, click **Next**.


## Set up authentication

To run a code sample from the Cloud Shell, you need to authenticate. Luckily, Google Cloud makes it easy to use the Application Default Credentials. 

Open Terminal and run the following command to set the project:
```bash
gcloud config set project <YOUR_PROJECT_ID>
```

Click **Authorize** in the Authorization popup.

Next, set your user credentials to authenticate your requests to Retail API

```bash
gcloud auth application-default login
```

Type 'Y' and press Enter. Click on the link in Terminal. A browser window should open asking you to login using your gmail account.

Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

Now we can run the code sample and check the Retail API in action.

To learn how to call the Retail API from the Cloud Shell code samples, click **Next**.

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Install Google Cloud Retail libraries

To run Python code samples for Retail API tutorial, you need to set up your virtual environment.

Run the following commands in a terminal:
```bash
pip install virtualenv
```
```bash
virtualenv myenv
```
```bash
source myenv/bin/activate
```
Next, install Google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

## Open CloudShell tutorials

'#Need to add tutorials to some regestry to make them available by ID
<walkthrough-tutorial-card id="tutorial_querying" title="Search simple query tutorial" keepPrevious=true>
Learn how to search for products in catalog using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="tutorial_pagination" title="Search with pagination tutorial" keepPrevious=true>
Learn how to navigate the search results using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="tutorial_filtering" title="Search with filtering tutorial" keepPrevious=true>
Learn how to filter search results using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="tutorial_ordering" title="Search with ordering tutorial" keepPrevious=true>
Learn how to order search results using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="tutorial_boosting" title="Search with boosting tutorial" keepPrevious=true>
Learn how to prioritize products in the search response using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="tutorial_query_expansion" title="Search with query expansion tutorial" keepPrevious=true>
Learn how to enable the query expansion feature using Retail API</walkthrough-tutorial-card>