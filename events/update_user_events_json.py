import datetime
import re

"""Run the file to update the import_user_events_tutorial.json file with more recent timestamp"""


def update_events_timestamp():
    # Get the yesterday's date
    request_time = datetime.datetime.now() - datetime.timedelta(days=1)
    day = request_time.date().strftime("%Y-%m-%d")
    print(day)

    # Read in the file
    with open('events/import_user_events_tutorial.json', 'r') as file:
        filedata = file.read()

    # Replace the target string  '"eventTime":"YYYY-mm-dd' with yesterday date
    filedata = re.sub('\"eventTime\"\:\"(\d{4})-(\d{2})-(\d{2})', '\"eventTime\":\"' + day, filedata, flags=re.M)

    # Write the file out again
    with open('events/import_user_events_tutorial.json', 'w') as file:
        file.write(filedata)
    print("The import_user_events_tutorial.json is updated")


update_events_timestamp()
