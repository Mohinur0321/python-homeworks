class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = 'Incomplete'
       
    def mark_complete(self):
        self.status = 'Complete'

    def __str__(self):
        return f"Description : {self.description} \ntitle: {self.title} \ndeadline: {self.deadline} \nstatus = {self.status}"
        

class ToDoList:
    
    def __init__(self):
        self.my_ls = []
    
    
    def add_task(self, name):
        self.my_ls.append(name)

    

    def show_all(self):
        print(f"Your tasks are ")
        for i in self.my_ls:
                print(i)

    def show_incomplete(self):
        for i in self.my_ls:
            if i.status == 'Incomplete':
                print(i)

    def __str__(self):
        return f"MyList: {self.my_ls}"


todo = ToDoList()
task = Task('sleep', 'get some rest', 'tonight')
todo.add_task(task)
task.mark_complete()
todo.show_all()

def run_cli():
    todo = ToDoList()
    while True:
        print(f"List Menu") 
        print(f"1. Add task")
        print(f"2. Mark as complete")
        print(f"3. Show my tasks")
        print(f"4. Show my incomplete tasks")
        print(f"5. Exit")
        choice = input('Enter number:')

        if choice == '1':
            title = input('Enter name of the task')
            desc = input('Enter description: ')
            deadline = input('Enter deadline ')
            task = Task(title, desc, deadline)
            todo.add_task(task)
            print("Task added.")
        

        elif choice == '2':
            task_name = input('Enter title of task to mark as complete')

            found = False
            for tsk in todo.my_ls:
                if tsk == task_name:
                    task.mark_complete()
                    print('Successfull')
                if not found:
                    print('Task not found')
            
        elif choice == '3':
            todo.show_all()
            
        elif choice== '4':
            todo.show_incomplete()
            
        elif choice == '5':
            print('Exiting to do list')
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_cli()

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.my_ls = []

    def add_post(self, post_name):
        self.my_ls.append(post_name)

    def list_posts(self):
        if not self.my_ls:
            print("No posts available.")
        else:
            print("Your posts are:")
            for i in self.my_ls:
                print(i)

    def author(self, author_name):
        found = False
        for i in self.my_ls:
            if i.author == author_name:
                print(i)
                found = True
        if not found:
            print("No posts by that author.")

    def delete_post(self, name):
        for i in self.my_ls:
            if i.title == name:
                self.my_ls.remove(i)
                print("Post deleted.")
                return
        print('Post not found. Try again.')

    def edit_post(self, name, change_to_what):
        for i in self.my_ls:
            if i.title == name:
                i.content = change_to_what
                print("Post content updated.")
                return
        print("Post not found.")

    def latest_posts(self):
        if not self.my_ls:
            print("No posts available.")
        else:
            print("Latest posts:")
            for i in self.my_ls[-5:][::-1]:  # last 5 in reverse order
                print(i)


def run_cli2():
    blog = Blog()
    while True:
        print("\n===== Blog Menu =====")
        print("1. Add post")
        print("2. List all posts")
        print("3. Display posts by specific author")
        print("4. Edit post")
        print("5. Delete post")
        print("6. Show the latest posts")
        print("7. Exit")
        choice = input("Enter number: ")

        if choice == '1':
            title = input("Enter title: ")
            content = input("Enter content: ")
            author = input("Enter author: ")
            post1 = Post(title, content, author)
            blog.add_post(post1)

        elif choice == '2':
            blog.list_posts()

        elif choice == '3':
            author_name = input("Enter author's name: ")
            blog.author(author_name)

        elif choice == '4':
            name = input("Enter the title of the post to edit: ")
            new_content = input("Enter the new content: ")
            blog.edit_post(name, new_content)

        elif choice == '5':
            post_title = input("Enter the title of the post to delete: ")
            blog.delete_post(post_title)

        elif choice == '6':
            blog.latest_posts()

        elif choice == '7':
            print("Exiting the blog system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == '__main__':
    run_cli2()

class Account:
    def __init__(self, account_number, holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = 0

class Bank:
    def __init__(self):
        self.my_ls = []
        self.account_id = 1

    def add_account(self, holder_name):
        account = Account(self.account_id, holder_name)
        self.my_ls.append(account)
        print(f"Account created. Your ID is {account.account_number}")
        self.account_id += 1

    def check_balance(self, account_id):
        account_id = int(account_id)
        for i in self.my_ls:
            if i.account_number == account_id:
                print(i.balance)
                return
        print('Account was not found') 

    def deposit(self, account_id, amount):
        account_id = int(account_id)
        amount = float(amount)
        for i in self.my_ls:
            if i.account_number == account_id:
                i.balance += amount
                print(f"The deposited money: {amount} \nYour total balance: {i.balance}")
                return
        print('Account was not found')    

    def withdraw(self, account_id, with_amount):
        account_id = int(account_id)
        with_amount = float(with_amount)
        for i in self.my_ls:
            if i.account_number == account_id:
                if i.balance >= with_amount:
                    i.balance -= with_amount
                    print(f"The withdrawn money: {with_amount} \nYour total balance: {i.balance}")
                else:
                    print("Insufficient balance.")
                return
        print('Account was not found')

    def transfer(self, account_id, to_account, amount1):
        account_id = int(account_id)
        to_account = int(to_account)
        amount1 = float(amount1)

        sender = None
        receiver = None

        for account in self.my_ls:
            if account.account_number == account_id:
                sender = account
            elif account.account_number == to_account:
                receiver = account

        if sender is None or receiver is None:
            print('Either of accounts were not found')
            return

        if sender.balance < amount1:
            print("Insufficient balance for transfer.")
            return

        sender.balance -= amount1
        receiver.balance += amount1

        print(f"Transferred {amount1} from {account_id} to {to_account}")
        print(f"Sender new balance: {sender.balance}")
        print(f"Receiver new balance: {receiver.balance}")

    def details(self, account_id):
        account_id = int(account_id)
        for i in self.my_ls:
            if i.account_number == account_id:
                print(f"Account ID: {i.account_number}, Name: {i.holder_name}, Balance: {i.balance}")
                return
        print('Account was not found')

def cli():
    bank = Bank()
    while True:
        print("\n===== Bank Menu =====")
        print("1. Add account")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")
        choice = input("Enter number: ")

        if choice == '1':
            holder_name = input("Enter your name: ")
            bank.add_account(holder_name)

        elif choice == '2':
            id = input('Enter your ID: ')
            bank.check_balance(id)

        elif choice == '3':
            money = input('Enter amount to deposit: ')
            id = input('Enter your ID: ')
            bank.deposit(id, money)

        elif choice == '4':
            id = input("Enter your ID: ")
            amount = input("Enter amount to withdraw: ")
            bank.withdraw(id, amount)

        elif choice == '5':
            print("Exiting the bank system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == '__main__':
    cli()


git add string_utils.py
git commit -m "Add missing string_utils module"
git push origin main  # or replace 'main' with your branch name
