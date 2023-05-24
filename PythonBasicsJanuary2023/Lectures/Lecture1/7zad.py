architect_name = input()
project_numbers = int(input())

HOURS_NEEDED_ON_A_PROJECT = 3

needed_hours_on_all = project_numbers * HOURS_NEEDED_ON_A_PROJECT

print(f'The architect {architect_name} will need {needed_hours_on_all} hours to complete {project_numbers} project/s.')
