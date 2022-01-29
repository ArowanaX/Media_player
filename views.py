import models 
import controllers

print("Wellcome...")

while True:
    ch=input("add media==> a\nplay simple==>p\nplay by name==>pn\nplay by rate==>pr\n")
    if ch=="a":
        location=input("location: ")
        name=input("name: ")
        rate=input("rate: ")

        if location.startswith('https://'):
            name=models.Web_Media(location,name,rate)
            models.mediaList.append(name)
            print("web media is added...!") 

        elif location.startswith('/') or location.startswith('c:\\'):
            name=models.Local_Media(location,name,rate)
            models.mediaList.append(name)
            print("local media is added...!") 
            
        else:
            raise Exception('Wrong media location')
        continue



    elif ch=="p":
        controllers._play(models.mediaList)



    elif ch=="pn":
        controllers.play_by_name()



    elif ch=="pr":
        controllers.play_by_rate()
