class Job:
    """A class to represent a job posting."""
    
    def __init__(self, title, company, location, description, salary=None, experience_level=None):
        self.title = title
        self.company = company
        self.location = location
        self.description = description
        self.salary = salary
        self.experience_level = experience_level

    def __repr__(self):
        return f"<Job(title={self.title}, company={self.company}, location={self.location})>"
