import os


path = "C:\\Users\\Gautam Kumar Mahato\\Downloads\\Image_Background_Removal-main (1)\\Image_Background_Removal-main\\static\\uploads\\detected.png"


def delete():
    try:
        os.remove(path)
        print("success")
    except:
        print("file not found")