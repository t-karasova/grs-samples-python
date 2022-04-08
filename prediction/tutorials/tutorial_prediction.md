# Prediction tutorial

## Get started

This tutorial shows you how to get a recommendations with Prediction service and analyze the response.

## Simple prediction request

The prediction request contains only the following required fields:
- `placement`—a resource name of the Recommendation AI model placement.
- `user_event`— context about the user for event logging. User event includes
the next required fields:
   - `event_type` - a user event type.
   - `visitor_id` - a unique identifier to track visitors.
   - `product_details` - the main product details related to the event. 
*Note this field is required only for particular event types*. 
The list of event types you can take a look here [UserEvent](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UserEvent).

1. Open
<walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_simple.py">predict_simple.py</walkthrough-editor-select-regex> to review the request.

2. To request the prediction for the provided user event, run the following command in Terminal:
    ```bash
    python prediction/get_prediction.py
    ```

3. Note that the results contain a list of matched items returned by the Prediction service.

    - `attribution_token` is a unique search token that enables accurate attribution of the search model performance.

## Error handling

In case of sending some invalid data or if any of the required fields is missing in the request, the Prediction Service responds with an error message.
To find a complete list of the Prediction Request fields with their corresponding requirements, check the [Prediction Service references](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#predictionservice)

In this tutorial, you will get an error message when trying to request the Prediction Service without setting the `user_event`, which is a required field.

1. To check it, comment out a <walkthrough-editor-select-regex filePath="cloudshell_open/grs-samples-python/prediction/predict_simple.py" regex="user_event">line</walkthrough-editor-select-regex>: `predict_request.user_event = user_event`.

1. Run the following command in Terminal:
    ```bash
    python prediction/get_prediction.py
    ```

1. You should see the following error message:

    ```terminal
    google.api_core.exceptions.InvalidArgument: 400 Field "userEvent" is a required field, but no value is found.
    ```
