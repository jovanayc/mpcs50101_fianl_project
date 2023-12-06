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

import datetime, itertools, pickle

class Task:
    id_obj = itertools.count()
    
    def __init__(self, name: str, due_date: str = None, priority: int = 1):
        self.name = name
        self.id = next(Task.id_obj)
        self.due_date = due_date
        self.created_date = datetime.datetime.now()
        self.completed_date = "-" #value will change when task is completed
        if priority not in {1, 2, 3}:
            raise ValueError("Invalud priority range. Acceptable input is 1, 2, or 3.")
        self.priority = priority #if priority limits are followed, autmatically set to priority


    def __str__(self):
        return f'Task Name: {self.name}, \
            Date Created: {self.created_date}, \
            Date Completed: {self.completed_date}, \
            Priority: {self.priority}, \
            Due Date: {self.due_date}'
            
    def __repr__(self):
        return f'Task Name: {self.name}, \
            Date Created: {self.created_date}, \
            Date Completed: {self.completed_date}, \
            Priority: {self.priority}, \
            Due Date: {self.due_date}'
        
    def pickle_obj(self):
        with open(f'task_{self.id}.pickle', 'wb') as file: 
            pickle.dump(self, file)
        return file
        
                
    def print_info(self):
        print(f'\nTask Name: {self.name} \
            Task ID: {self.id} \
            Date Created: {self.created_date} \
            Date Completed: {self.completed_date} \
            Priority: {self.priority} \
            Due Date: {self.due_date}')

class Task_Manager:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks_list = []
        self.pickled_file_name = "tasks_list.pickle"

    def add(self, new_task_pickled_file: str):
        '''Adds a pickle file of task objects to the Task Manager'''
        print("new_task_pickled_file:", new_task_pickled_file)
        try:
            with open(new_task_pickled_file, 'rb') as file:
                loaded_tasks = pickle.load(file)
                if isinstance(loaded_tasks, Task):
                    self.tasks_list.append(loaded_tasks)
                elif isinstance(loaded_tasks, list) and all(isinstance(task, Task) for task in loaded_tasks):
                    self.tasks_list.extend(loaded_tasks)
                else:
                    raise ValueError("Invalid file content. Please provide a pickled Task object or a list of Task objects.")
        except FileNotFoundError:
            print("In Task Manager -- No pickled file found.")    

    
    def pickle_tasks(self):
        """Pickle your task list to a file"""
        with open(self.pickled_file_name, 'wb') as file:
            pickle.dump(self.tasks_list, file)
        return self.pickled_file_name

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        print("In report")
        for temp_task in self.tasks_list:
            print("Type", type(temp_task))
            print(temp_task, "\n")
        print(len(self.tasks_list))
        
        # if isinstance(new_task, pickle):
        #     self.tasks_list.append(new_task)
        # else:
        #     raise ValueError("Invalid file. Please only add pickled files.")
        
    def done(self):
        pass

    def query(self):
        pass


        
    

'''Example Tasks'''
task1 = Task("Drive to Grandma's House", "Tuesday", 1)
task2 = Task("Get Pizza", "Tuesday", 2)
task3 = Task("Get On Airplane", "Tuesday", 3)
task4 = Task("Get gas", "Tuesday", 1)


'''Example Task Manager'''
task_manager = Task_Manager()
task_manager.add(task1.pickle_obj())
task_manager.add(task2.pickle_obj())
task_manager.report()

