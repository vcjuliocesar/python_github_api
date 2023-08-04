import requests

def get_user_info():
    
    user = input('Enter a user name => ')
    
    r = requests.get(f'https://api.github.com/users/{user}')
    
    if r.status_code == 200:
        
        print(r)
    
        info = r.json()
        
        user = user
        name = info['name']
        followes = info['followers']
        public_repos = info['public_repos']
        
        print(f'User: {user}')
        print(f'Name: {name}')
        print(f'Followes: {followes}')
        print(f'Public repos: {public_repos}')
    else:
        print("User not found")