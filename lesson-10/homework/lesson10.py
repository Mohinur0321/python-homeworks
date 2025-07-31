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

