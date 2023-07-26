from datetime import datetime, timedelta

def get_dates_between(start_date, end_date):
    date_format = "%Y-%m-%d"
    dates_list = []

    # Convert the input strings to datetime objects
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    # Add the start date to the list
    dates_list.append(start_date.strftime(date_format))

    # Calculate the number of days between the start and end date
    delta = timedelta(days=1)

    # Generate and add the dates between the start and end date to the list
    while start_date < end_date:
        start_date += delta
        dates_list.append(start_date.strftime(date_format))

    return dates_list

# Example usage:
start_date = "2023-07-20"
end_date = "2023-07-25"
dates_between = get_dates_between(start_date, end_date)
print(dates_between)
