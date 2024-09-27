import base64
from PIL import Image
from io import BytesIO


def genImgEntry(avatar, talking):
  return {"avatar": f"{avatar}", "avatarTalking": f"{talking}"}


def resizeImage(image, height):
  img = Image.open(image)
  img = img.resize((int(img.width * (height / img.height)), height))
  buffer = BytesIO()
  img.save(buffer, format="PNG")
  return buffer.getvalue()


def b64encodeImageFromFile(image):
  with open(image, "rb") as f:
    # return resized image
    print("b64 size of original image: ", len(base64.b64encode(f.read())))
    print("b64 size of resized image: ", len(
        base64.b64encode(resizeImage(f, 256))))
    return f"'data:image/png;base64,{base64.b64encode(resizeImage(f, 256)).decode('utf-8')}'"


userList = {}
with open("id.csv", "r") as f:
  headers = f.readline().strip().split(",")
  userList = {line.strip().split(",")[0]: genImgEntry(
      line.strip().split(",")[1], line.strip().split(",")[2]) for line in f}

res = """@keyframes speak-now {
    0% {
        bottom: 0px;
    }

    15% {
        bottom: 10px;
    }

    30% {
        bottom: 0px;
    }
}

body {
    background-color: rgba(0, 0, 0, 0);
    margin: 0px auto;
    overflow: hidden;
    transform:scale(0.5);
}

.Voice_avatar__htiqH {
    content: url(""" + b64encodeImageFromFile("Default1.png") + """);
    height: auto !important;
    width: auto !important;
    border-radius: 0% !important;
    filter: brightness(50%);
    transform: rotate(30deg);
    margin-bottom: -1500px;
}

.Voice_avatarSpeaking__lE\\+4m {
    border-color: rgba(0, 0, 0, 0) !important;
    position: relative;
    animation-name: speak-now;
    animation-duration: 1s;
    animation-fill-mode: forwards;
    filter: brightness(100%);
    content: url(""" + b64encodeImageFromFile("Default1_-_Copy.png") + """);
}

"""


for user in userList:
  usercond = f'[src*="{user}"]'

  res += """.Voice_avatar__htiqH""" + usercond + """ {
content:url(""" + b64encodeImageFromFile(userList[user]["avatar"]) + """);
height:auto !important;
width:auto !important;
border-radius:0% !important;
filter: brightness(50%);
}

.Voice_avatarSpeaking__lE\\+4m""" + usercond + """ {
border-color: rgba(0,0,0,0) !important;
position:relative;
animation-name: speak-now;
animation-duration: 1s;
animation-fill-mode:forwards;
filter: brightness(100%);
content:url(""" + b64encodeImageFromFile(userList[user]["avatarTalking"]) + """);
}

"""

with open("talkies.css", "w") as f:
  f.write(res)
