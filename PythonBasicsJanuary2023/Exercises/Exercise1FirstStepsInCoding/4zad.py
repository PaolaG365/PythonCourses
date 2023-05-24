book_pages = int(input())
pages_per_hour = int(input())
days_number = int(input())

total_time_to_finish = book_pages // pages_per_hour
hours_a_day = total_time_to_finish // days_number

print(hours_a_day)
