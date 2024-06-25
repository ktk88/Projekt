import requests

url= 'https://api.vk.com/method/users.get?user_ids=159118253&fields=bdate&access_token=vk1.a.HOb7V5vFKHBlZGvUykzUbWGnHvPc6m4aek8aLleUBFSxF3sPRD6XsgC2vIeyM3TVTnyh1nJwIbuYJqkPTahEZfH6wya4dqLFZxLyIezvfLCO7A8Ov2eHv9jodPh6BE0Ci3LqduJ55JHxiS8K242Fb2vP1QjMD9CYawtlGjAKd0oqmkF-ZhHHgJpCF3gI3hKs&v=5.199'
response = requests.get(url)
print (response.status_code)
print (response.json())