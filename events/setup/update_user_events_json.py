import datetime
import re

"""Run the file to update the user_events.json file with more recent timestamp"""


def update_events_timestamp(json_file):
    # Get the yesterday's date
    request_time = datetime.datetime.now() - datetime.timedelta(days=1)
    day = request_time.date().strftime("%Y-%m-%d")
    print(day)

    # Read in the file
    with open(json_file, 'r') as file:
        filedata = file.read()

    # Replace the target string  '"eventTime":"YYYY-mm-dd' with yesterday date
    filedata = re.sub('\"eventTime\"\:\"(\d{4})-(\d{2})-(\d{2})', '\"eventTime\":\"' + day, filedata, flags=re.M)

    # Write the file out again
    with open('events/resources/user_events.json', 'w') as file:
        file.write(filedata)
    print("The user_events.json is updated")


update_events_timestamp('events/resources/user_events.json')
update_events_timestamp('events/resources/user_events_some_invalid.json')
