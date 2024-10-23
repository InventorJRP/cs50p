file = input("File name: ").lower()

if file.find(".") != int("-1"):
    first, last = file.split('.')
    match last:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "":
            print("Please include file extention")
        case _:
            print("Media type not found")
else:
    print("application/octet-stream")