# **Pagination Tutorial**

## Let's get started

Using pagination lets you view and navigate the search results effortlessly. Moreover, it decreases both the lookup time and the size of responses.

This tutorial shows you how to control pagination in your search request.

There are three fields in the search request that give you all the possibilities of navigating through the search results: 
- **```page_size```**,
- **```next_page_token```**,
- **```offset```**

Let's see how each of them works.

**Time to complete**: About 2 minutes

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER="<YOUR_PROJECT_NUMBER>"
```

## Page size

The ```page_size``` request field allows you to limit the number of items in the search response.

To view the request with ```page_size```, open **search_with_pagination.py**. 

Run the sample in a terminal using the command:

```bash
python search_with_pagination.py
```

As you can see now, **```results[]```** contain the exact number of products you have set as the page size.

The **```total_size```** is not equal to the page size; it's the number of items matching the search query and it does not change as you adjust the number of products per page.

We will use **```next_page_token```** in the next tutorial step.

## Next page token

After you have received a response at the previous step, you can request the next page. 

You need to receive the ```next_page_token```, set it to a request field ```page_token```, and call the Search service again.
To do it, find the comment "#PASTE CALL WITH NEXT PAGE TOKEN HERE:" and paste this piece of code:
```
    next_page_token = search_response_first_page.next_page_token
    search_request_next_page = get_search_request("Hoodie", page_size, offset, next_page_token)
    search_response_next_page = get_search_service_client().search(search_request_next_page)

    print("---next page search results---")
    print(search_response_next_page)
```

Run the code sample again:
```bash
python search_with_pagination.py
```

You can see the next page of <page_size> products in the response.

The field **```next_page_token```** possesses the value intended to forward you to the next page. You can use this field in further results navigation.

## Offset

In other cases, instead of navigating from page to page or getting results with top relevance, you can directly jump to a particular position using the offset.

You have requested the second page with 6 products per page using ```next_page_token``` in the previous step .

To reproduce the same effect using ```offset```, configure the field ```page_size``` with the same value which is "6",
and perform a small calculation to get the offset value:

offset = 6 * (2 - 1) = 6, where 6 is a page size, and 2 is a number of page you would like to switch too.

## Offset use case

Find the comment "#PASTE CALL WITH OFFSET HERE:" and paste this piece of code:
```
    offset = 6
    search_request_second_page = get_search_request("Hoodie", page_size, offset, page_token)
    search_response_second_page = get_search_service_client().search(search_request_second_page)

    print("---second page search results---")
    print(search_response_second_page)
```

Run the code sample again:
```bash
python search_with_pagination.py
```

Take a look at both "next page search results" and "second page search results". You can compare the lists of received products using both the next_page_token and offset that should be equal.

Now you kow how the offset works. Let's perform the calculation one more time to make it clear.

If you want to jump to the 7th page with a page size 12, the offset value you need to set should be calculated this way:

offset = 12 * (7 - 1) = 72

## Pagination. Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Search Service responds with an error message.
To find a complete list of the Search Request fields with their corresponding requirements, check the [Search Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#searchservice)

If you try to request the Search Service with negative page size, you will get an error message.


Change the value of the variable ```page_size``` to any negative value and run the code one more time.
```bash
python search_with_pagination.py
```

You should see the following error message:
```google.api_core.exceptions.InvalidArgument: 400 `page_size` must be nonnegative, but is set to -6.``` 

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! We **encourage** you to **test the pagination by yourself** right here in the Cloud Shell environment using different combinations of values for pagination parameters.

**Thank you for completing this tutorial!**
