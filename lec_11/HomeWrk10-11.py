import requests

def get_filtered_titles_and_bodies():
    """Fetch data and filter titles and bodies based on conditions."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        filtered_titles = [post for post in posts if len(post['title'].split()) <= 6]

        filtered_bodies = [post for post in posts if post['body'].count('\n') <= 3]

        return filtered_titles, filtered_bodies
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
        return [], []


def post_new_data():
    """Send a POST request to create a new post."""
    new_post = {
        "title": "New Post",
        "body": "This is a new post created via the API.",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    if response.status_code == 201:
        print("Post created successfully:")
        print(response.json())
    else:
        print(f"Failed to create post. Status code: {response.status_code}")


def update_data(post_id):
    """Send a PUT request to update an existing post."""
    updated_post = {
        "title": "Updated Post",
        "body": "This post has been updated via the API.",
        "userId": 1
    }
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        print("Post updated successfully:")
        print(response.json())
    else:
        print(f"Failed to update post. Status code: {response.status_code}")


def delete_data(post_id):
    """Send a DELETE request to delete a post."""
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with ID {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")




titles, bodies = get_filtered_titles_and_bodies()
print("Filtered Titles:")
for post in titles:
    print(f"- {post['title']}")

print("\nFiltered Bodies:")
for post in bodies:
    print(f"- {post['body']}")

print("\nCreating a new post:")
post_new_data()

print("\nUpdating an existing post:")

print("\nDeleting a post:")
delete_data(1)
