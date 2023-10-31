class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + 1
        self.seconds = total_seconds % 60
        self.minutes = (total_seconds % 3600) // 60
        self.hours = total_seconds // 3600 if total_seconds // 3600 < Time.max_hours else 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
