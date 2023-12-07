#Jovanay Carter
#MPCS 50101
#Final Project
#Dec 6, 2023

#Task class

"""Representation of a task
  
  Attributes:
        - created - date
        - completed - date
        - name - string
        - unique id - number
        - priority - int value of 1, 2, or 3; 1 is default
        - due date - date, this is optional
  """

import datetime, itertools, pickle, functools, prettytable

class Task:
    id_obj = itertools.count(start=1)
    
    def __init__(self, name: str, due_date: str = None, priority: int = 1):
        self.name = name
        self.id = next(Task.id_obj)
        self.due_date = (
            datetime.datetime.strptime(due_date, "%m/%d/%Y").date()
            if due_date is not None
            else None
        )
        self.created_date = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
        self.completed_date = "-" #value will change when task is completed
        if priority not in {1, 2, 3}:
            raise ValueError("Invalud priority range. Acceptable input is 1, 2, or 3.")
        self.priority = priority #if priority limits are followed, autmatically set to priority
        self.age = self.calculate_age()

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, age: {self.age}, created: {self.created_date}, completed: {self.completed_date}, priority: {self.priority}, due: {self.due_date}'

    # def __repr__(self):
    #     return f'name: {self.name}, id: {self.id}, age: {self.age}, created: {self.created_date}, completed: {self.completed_date}, priority: {self.priority}, due: {self.due_date}' 

       
    def get_name(self):
        '''Allows name to be accesbile outside of class'''
        return self.name
    
    def get_id(self):
        '''Allows ID to be accesbile outside of class'''
        return self.id
      
    def calculate_age(self):
        '''Method to calculate age from created date - completed date'''
        new_datetime = datetime.datetime.strptime(self.created_date, "%a %b %d %H:%M:%S %Y")
        day_difference = datetime.datetime.now() - new_datetime
        age_in_days = day_difference.days
        return f"{age_in_days}d"
    
    def get_age(self):
        '''Allows age to be accesbile outside of class'''
        return self.age
    
    def get_due_date(self):
        '''Allows Due Date to be accesbile outside of class'''
        return self.due_date
      
    def get_created_date(self):
        '''Allows Created Date to be accesbile outside of class'''
        return self.created_date
          
    def update_completed_date(self, new_completed_date):
        '''Allows Completed Date to be accesbile outside of class'''
        new_completed_date = datetime.datetime.strptime(new_completed_date, "%m/%d/%Y").date()
        formatted_completed_date = new_completed_date.strftime("%a %b %d %H:%M:%S %Z %Y")
        self.completed_date = formatted_completed_date
        return self.completed_date
    
    def get_completed_date(self):
        '''Allows Completed Date to be accesbile outside of class'''
        return self.completed_date
          
    def get_priority(self):
        '''Allows Priority to be accesbile outside of class'''
        return self.priority
                
    def print_info(self):
        print(f'\nTask Name: {self.name} \
            Task ID: {self.id} \
            Age: {self.age} \
            Date Created: {self.created_date} \
            Date Completed: {self.completed_date} \
            Priority: {self.priority} \
            Due Date: {self.due_date}')