import requests

get_url = "https://jsonplaceholder.typicode.com/posts"

# sending GET-request
responce_get = requests.get(get_url)

# checking answer code
if responce_get.status_code == 200:
    print("GET-request successful!")
    print("Page content: ")
    print(responce_get.text[:500])
else:
    print(f"GET-request error: {responce_get.status_code}")

post_url = "https://jsonplaceholder.typicode.com/posts"

# data for sending
post_data = {
    'title' : 'foo',
    'body' : 'bar',
    'userID' : 1
}

# sending POST-request
responce_post = requests.post(post_url, json=post_data)

# checking answer code
if responce_post.status_code == 201:
    print("\nPOST-request is successful")
    print("Recieved data: ")
    print(responce_post.json())
else:
    print(f"POST-request error: {responce_post.status_code}")