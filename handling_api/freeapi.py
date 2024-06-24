import requests


def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json() #converting string data into json

    if data["success"] and "data" in data:
        User_data=data["data"]
        username=User_data["login"]["username"]
        country=User_data["location"]["country"]
        return username,country
    else:
        raise Exception("failed to fetch user data")

def main():
    try:
        username,country=fetch_random_user_freeapi()
        print(f"Username: {username} \n country: {country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
   

