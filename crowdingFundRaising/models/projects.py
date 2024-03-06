from datetime import datetime

class Project:
    def __init__(self, title, details, total_target, start_date, end_date, owner):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner

    def validate_dates(self):
        return self.start_time < self.end_time
    
    def is_owner(self, user):
        return self.owner == user
