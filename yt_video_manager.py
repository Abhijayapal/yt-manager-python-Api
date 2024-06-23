import json

def load_data():
    try:
        with open('yt_manager','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def list_all_vdo(videos):
    pass
def update_vdo(videos):
    pass
def add_vdo(videos):
    pass
def delete_vdo(videos):
    pass

def main():
    videos=load_data()
    while True:
        print("\n Youtube manager")
        print("1. list of favourite videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos")
        print("4. delete a youtube videos")
        print("5. Exit")
        choice=input("enter your choice")

        # match syntax
        match choice:
            case '1':
                list_all_vdo(videos)
            case '2':
                add_vdo(videos)
            case '3':
                update_vdo(videos)
            case '4':
                delete_vdo(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__=="__main__":
    main()
        

