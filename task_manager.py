#Jovanay Carter
#MPCS 50101
#Final Project
#Dec 6, 2023


import datetime, pickle, prettytable, argparse
from task import Task
'''Task Manager Class'''

class Task_Manager:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        self.tasks_list_all = [] # List of Task objects
        self.sorted_incomplete_list = []
        self.filename = "file.pickle"

    def __enter__(self):
        '''Unpickle list to start'''
        self.tasks_list_all = self.unpickle_tasks()
        return self
    
    def __exit__(self, *args):
        '''Pickle to exit'''
        self.pickle_tasks()
        print("Exiting Task Manager")

        
    def pickle_tasks(self):
        """Pickle your task list to a file"""
        with open(f'{self.filename}', 'wb') as file:
            pickle.dump(self.tasks_list_all, file)
        print("pickled")
        
        return self.filename

    def unpickle_tasks(self):
        """Unpickle your task list to a file"""
        try:
            with open(f'{self.filename}', 'rb') as file:
                loaded_tasks = pickle.load(file)
                self.tasks_list_all = loaded_tasks
            print("unpickled")
            return self.tasks_list_all
        except FileNotFoundError:
            print("In Task Manager -- No pickled file found.")
            return []
            
    def add(self, name: str, due_date: str = None, priority = None):
        '''Adds a pickle file of task objects to the Task Manager'''
        if priority == None:
            priority = 1
        new_task = Task(name, due_date, priority)
        self.tasks_list_all.append(new_task)
        id = new_task.get_id()
        print(f'Created task {id}')
        
    def report(self):
        '''Reports all task'''
        print("In report")
        self.print_table(self.tasks_list_all, True)
        return self.tasks_list_all
        
    def list(self, query=False):
        '''Should show a list of incomplete task, sorted by due date then by priority level'''
        print("In list")
        incomplete_list = []
        for task in self.tasks_list_all:
            if task.get_completed_date() == '-':
                incomplete_list.append(task)
        
        sorted_incomplete_list = sorted(incomplete_list, key=lambda task_x: (task_x.get_due_date(), task_x.get_priority(), task_x.get_name()))
        
        if not query:
            '''Print table for list i not query was not called'''
            self.print_table(sorted_incomplete_list, False)

        self.sorted_incomplete_list = sorted_incomplete_list
        return self.sorted_incomplete_list
        
    def print_table(self, data_list, extended: bool = False):
        '''Uses prettytable module to create flexible and formated table
            Table is different for printing lists vs printing all data.
            Extended bool is used to toggle printing all data vs pringint only ID, Age, Due Date, Priority and Task Name as with list method'''
        table = prettytable.PrettyTable()

        if extended:
            table.field_names = ["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"]
            for task in data_list:
                table.add_row([task.get_id(), task.get_age(), task.get_due_date(), task.get_priority(), task.get_name(), task.get_created_date(), task.get_completed_date()])
        else:
            table.field_names = ["ID", "Age", "Due Date", "Priority", "Task"]
            for task in data_list:
                table.add_row([task.get_id(), task.get_age(), task.get_due_date(), task.get_priority(), task.get_name()])

        print(table)
   
    
    def done(self, id):
        '''Update the given tasks' completed date as of the date of the update'''
        for task in self.tasks_list_all:
            if str(task.get_id()) == id:
                new_date = datetime.date.today()
                format_date = new_date.strftime("%m/%d/%Y")
                task.update_completed_date(str(format_date))
                
    def delete(self, id):
        '''Delete command pops task from task list objects'''
        for task in self.tasks_list_all:
            if str(task.get_id()) == id:
                self.tasks_list_all.remove(task)
                
    def query(self, keywords:str=None):
        incomplete_tasks = self.list(True)
        query_set = set()
        
        '''Take in string and make a list'''

        for task in incomplete_tasks:
            task_name = task.get_name().lower()
            for keyword in keywords:
                if keyword.lower() in task_name:
                    query_set.add(task)
        
        query_list = list(query_set)
        self.print_table(query_list)
        
        return query_list
        