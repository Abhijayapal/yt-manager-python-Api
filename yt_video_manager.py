import json

def load_data():
    try:
        with open('yt_manager.txt','r') as file:
        # giving us data as string 
            return json.load(file)
    except FileNotFoundError:
        return []

# helper data-situations can be directly handled
def save_data_helper(videos):
    with open('yt_manager.txt','w') as file:
        # dump-inserting data- 2 parameters
        # what to be written, where to be written
        json.dump(videos,file)

def list_all_vdo(videos):
    # enumerate add indexing
    for index, video in enumerate(videos,start=1):
        # imp statement
        print("\n")
        
        print(f"{index}. {video['name']}, Duration: {video['time']}")
                                  

def update_vdo(videos):
    list_all_vdo(videos)
    index=int(input("enter the video to be updated "))
    if 1<= index <=len(videos):
        name=input("enter new video name")
        time=input("enter new video time")
        videos[index-1]={'name':name , 'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")



def add_vdo(videos):
    # 2 input to be taken from user
    name=input("enter video name")
    time=input("enter video time")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
    
def delete_vdo(videos):
    list_all_vdo(videos)
    index=int(input("enter the video to be deleted "))
    if 1<= index <=len(videos):
        
        del videos[index-1]

        save_data_helper(videos)
    else:
        print("invalid index selected")
    

def main():
    videos=load_data()
    while True:
        print("\n Youtube manager")
        print("1. list of favourite videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube videos ")
        print("4. delete a youtube videos ")
        print("5. Exit ")
        choice=input("enter your choice ")
        # print(videos)

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
                print("invalid choice ")

if __name__=="__main__":
    main()
        

