from task import Task
from task_manager import Task_Manager
import argparse


def main():    
    parser = argparse.ArgumentParser(description="Your script description")

    # Command line arguments
    parser.add_argument('--add', type=str, required=False, help="adding task to list")
    parser.add_argument('--due', type=str, required=False, help="adding due date to task")
    parser.add_argument('--priority', type=int, required=False, help="adding priority to task")
    parser.add_argument('--list', type=str, required=False, help="print list of incomplete tasks")
    parser.add_argument('--done', type=str, required=False, help="changes task to done, setting complete date")
    parser.add_argument('--report', type=str, required=False, help="reports all task complete or incomplete")
    parser.add_argument('--query', type=str, required=False, nargs="+", help="sorted list by query")
    parser.add_argument('--delete', type=str, required=False, help="deletes task")


    args = parser.parse_args()

    # Access the input into comman line
    add_name = args.add
    due_date = args.due
    priority = args.priority
    list_command = args.list
    done_command = args.done
    report_command = args.report
    query_command = args.query
    delete_command = args.delete


    # Now you can use query_keywords and other_option_value in your script
    print("Query Keywords:", query_command)
    print("What we added:", add_name)
    print("What's the due date:", due_date)
    print("What's the priority:", priority)
    print("Do: print list:", list_command)
    print("Do: mark done:", done_command)
    print("Do: report list:", report_command)
    print("Do: delete list:", delete_command)
    
    '''Set up context manager'''
    with Task_Manager() as task_manager:
        print("\n Starting Task Manager\n")
        
        if add_name != None:
            task_manager.add(add_name, due_date, priority)
        elif list_command != None:
            task_manager.list()
        # task_manager.query(query_command)

        
        

    # '''Example Tasks'''
    # #$ python todo.py --add "Walk Dog" --due 4/17/2018 --priority 1
    # task1 = Task("Call Mom", "12/15/2023", 2)
    # task2 = Task("Get Pizza", "12/23/2026", 2)
    # task3 = Task("Get On Airplane", "1/1/2024", 3)
    # task4 = Task("Get gas", "12/15/2023", 1)
    # task5 = Task("Do Homework", "12/25/2023", 3)
    # task6 = Task("Feed Dog", "12/20/2025", 3)

    # '''Example Task Manager'''
    # task_manager.add(task1)
    # task_manager.add(task2)
    # task_manager.add(task3)
    # task_manager.add(task4)
    # task_manager.add(task5)
    # task_manager.add(task6)


if __name__ == "__main__":
    main() 