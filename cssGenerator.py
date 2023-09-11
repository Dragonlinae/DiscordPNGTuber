userList = {
    "123456789012345678": {
        "avatar": "https://image.png",
        "avatarTalking": "https://imagetalk.png"
    },
    "223456789012345678": {
        "avatar": "https://image2.png",
        "avatarTalking": "https://image2talk.png"
    }
}

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
    content: url(https://default.png);
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
    content: url(https://defaulttalk.png);
}

"""

for user in userList:
    res += f""".Voice_avatar__htiqH[src*=\"""" + user + """\"] {
content:url(""" + userList[user]["avatar"] + """);
height:auto !important;
width:auto !important;
border-radius:0% !important;
filter: brightness(50%);
}

.Voice_avatarSpeaking__lE\\+4m[src*=\"""" + user + """\"] {
border-color: rgba(0,0,0,0) !important;
position:relative;
animation-name: speak-now;
animation-duration: 1s;
animation-fill-mode:forwards;
filter: brightness(100%);
content:url(""" + userList[user]["avatarTalking"] + """);
}

"""

with open("talkies.css", "w") as f:
    f.write(res)
