# WRITE  BY @lMl10l
# PLUGIN FOR JepThon jepthon
# @JepThon

import random
from telethon import events
import random, re

from jepthon.utils import admin_cmd

import asyncio
from jepthon import jmthon

from ..core.managers import edit_or_reply

plugin_category = "extra"

# اوامر الادمن لسورس جـيبثون

@jmthon.ar_cmd(
    pattern="اوامر الحظر$",
    command=("اوامر الحظر ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الحـظر \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n( `.حظر` ) \n-  تقوم بالرد على شخص او وضع معرفه مع الامر وسيحظره من المجموعة\n\n( `.الغاء حظر` )\n - بالرد على الشخص او كتابة معرفه مع الامر لالغاء حظره\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon "
           )
      
@jmthon.ar_cmd(
    pattern="اوامر الكتم$",
    command=("اوامر الكتم ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الكـتم \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n( `.كتم` ) \n-  تقوم بالرد على شخص او وضع معرفه مع الامر وسيكتمه من المجموعة\n\n( `.الغاء كتم` )\n - بالرد على الشخص او كتابة معرفه مع الامر لالغاء كتمه\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon "
           )
       #@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التثبيت$",
    command=("اوامر التثبيت ", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر التثبيت \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n( `.تثبيت` ) \n-  تقوم بالرد على الرسالة مع الامر وستثبت في المجموعة\n\n( `.الغاء التثبيت` )\n - بالرد على الرسالة مع الامر لإلغاء تثبيتها\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon "
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الاشراف$",
    command=("اوامر الاشراف", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الاشراف \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n( `.رفع مشرف` ) \n-  تقوم بالرد على الشخص مع الامر و سيرفع مشرفا في المجموعة\n\n( `.تك` )\n - بالرد على الشخص مع الامر لإنزاله من الاشراف في المجموعة\n\n( `.ارفع` ) \n- لرفع المستخدم في جميع المجموعات مع كافة الصلاحيات مع لقب مخفي\n\n( `.نزل` ) \n-لتنزيل الشخص من رتبة الاشراف في جميع المجموعات\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon "
           )

# اوامر المجموعة ل سورس جـيبثون
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التفليش$",
    command=("اوامر التفليش", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
       "شـرح عـن اوامـر التفليـش \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.تفليش بالطرد` ) \n ارسل  الامـر لطرد جميع الاعضاء من المجموعه \n\n- ( `.تفليش` ) \n كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر المحذوفين$",
    command=("اوامر المحذوفين", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر المـحذوفين \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.حذف المحظورين` ) \n كتابة  الامـر في الكروب لالغاء حظر جميع الاعضاء \n\n- ( `.اطردني` ) \n فقـط ارسل الامر في المجموعة لمغادرة المجموعه التي تم ارسال الامر فيها\n\n- ( `.المحذوفين` ) \n لعرض الحسابات المحذوفة في مجمـوعة معيـنة ولحذفهم ارسل .المحذوفين اطردهم\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الكروب$",
    command=("اوامر الكروب", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الكروب \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.الاحداث` ) \n كتابة  الامـر في الكروب لعرض احداث الكروب\n\n- ( `.الاعضاء` ) \n فقـط ارسل الامر في المجموعة لعرض اعضاء المجموعة\n\n- ( `.المشرفين` ) \n ارسل الامر في المجموعه لعرض حسابات المشرفين\n\n- ( `.البوتات` )\n ارسل الامر في المجموعه لعرض البوتات\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
@jmthon.ar_cmd(
    pattern="اوامر الترحيب$",
    command=("اوامر الترحيب", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الترحيب \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n--( `.ترحيب + ترحيبك` )\n اكتب الامر مع ترحيب في المجموعه ليرحب بالاعضاء الجدد\n\n- ( `.حذف الترحيبات` ) \n فقـط ارسل الامر في المجموعة لحذف الترحيبات\n\n- ( `.الترحيبات` )\n ارسل الامر في المجموعه لعرض ترحيبات المجموعة\n\n- ( `.الترحيب السابق ايقاف/تشغيل` )\n لتعطيل اخر ترحيب وضعته في المجموعة او تشغيل\n\n- ( `.رحب + ترحيبك` )\n لوضع ترحيب في عند دخول الاعضاء للمجموعة سوف يرحب بهم في الخاص\n\n- ( `.حذف رحب` )\n لحذف الترحيب في الخاص➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الردود$",
    command=("اوامر الردود", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـردود \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.اضف رد + ردك` ) \n\n لوضع رد معين في المجموعة اكتب الامر وردك\n\n- ( `.حذف الردود` ) \n فقـط ارسل الامر في المجموعة لحذف الردود المضافة\n\n- ( `.الردود` ) \n ارسل الامر في المجموعه لعرض ردود المجموعة\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الحماية$",
    command=("اوامر الحماية", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـخاص \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.الحماية تشغيل/تعطيل` ) \n لتشغيل امر الحمايه او تعطيله في الـخاص \n\n- ( `.سماح` ) \n بالرد على الشخص للسماح له بالتكلم في الخاص\n\n- ( `.رفض` ) \n بالرد على الشخص لرفضه من الخاص \n\n- ( `.المسموح لهم` )\n فقط ارسل الامر لاظهار الاشخاص المسموح لهم والمرفوضين\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التلكراف$",
    command=("اوامر التلكراف", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر التلكراف \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.تلكراف ميديا` ) \n\n لاستخراج رابط من الصورة على شكل رابط تلكراف  \n\n- ( `.تلكراف نص` ) \n بالرد على النص او المقالة لصنع رابط تلكراف للنص\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
@jmthon.ar_cmd(
    pattern="اوامر الانتحال$",
    command=("اوامر الانتحال", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الانتحال \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.انتحال` ) \n\n بالرد على الشخص لنسخ حسابه بالكامل من صورة واسم وبايو  \n\n- ( `.اعادة` ) \n لارجاع الحساب الى وضعه الطبيعي لما كان سابقا\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
@jmthon.ar_cmd(
    pattern="اوامر التقليد$",
    command=("اوامر التقليد", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـتقليـد \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.تقليد` ) \n بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n- ( `.الغاء التقليد` ) \n بالرد على الشخص لايقاف التقليد\n\n- ( `.المقلدهم` ) \nلاظهـار قائمه الاشخاص الذي فعـلت عليهم امر التقليد ولمسحهم ارسل  (`.مسح المقلدهم`) \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
           #@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر المنشن$",
    command=("اوامر المنشن", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـمنشن \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.تاك + معرف + نص` ) \n\n لعمل تاك لشخص في الكروب و وضع التاك في النص \n- مثـال | .تاك` @JepThon  ههلا` \n\n- ( `.للكل + نص` ) \n لعمل تاك للكل مع النص اكتب الامر مع النص وارسله فقط\n\n- ( `.ابلاغ` )\n بالرد على الشخص لعمل ابلاغ لمشرفين المجموعة \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
           #@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التحميل$",
    command=("اوامر التحميل", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن امـر التحمـيل\n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر\n\n- (`.بحث + اسم الاغنية`)\nبكتابة اسم الاغنية مع الامر لارسال الاغنيه مباشرا واذا ما اشتغل جرب اوامر التحميل الاخرى\n- مثـال : `.بحث ماهر زين`\n\n- (`.يوت + اسم الفيديو او الاغنية`)\nكتابة الامر مع اسم الفيديو او الاغنية ليعطيك نتائج البحث وروابط من يوتيوب تستخدم مع اوامر التحميل\n- مثـال : `.يوت ماهر زين`\n\n- (`.تحميل ص + رابط الاغنية`)\nلتحميل اغنيه من خلال وضع الرابط مع الامر\n- مثـال : `.تحميل ص https://youtube.com/...`\n\n- (`.تحميل ف + رابط الفيديو`)\nكتابة الامر مع رابط المقطع لتحميله وارساله\n- مثـال : `.تحميل ف https://youtube.com/...`\n\n- (`.انستا + الرابط `)\nيستخدم هذا الامر لتحميل من الانستا فقط اكتب الامر مع رابط الفيديو ليحمله\n- مثـال : `.انستا https://instagram.com/jdisjejjd...`\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
@jmthon.ar_cmd(
    pattern="اوامر الترجمة$",
    command=("اوامر الترجمة", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الترجمة \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.ترجمة ar` ) \n\n بالرد على النص لترجمته للغه العربية\n\n- ( `.ترجمة en` ) \n بالرد على النص لترجمته للغه الانكليزية\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر النطق$",
    command=("اوامر النطق", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـنطق \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.تكلم ar` ) \n بالرد على النص لتحويله الى مقطع صوتي للغة العربيه \n\n- ( `.تكلم en` ) \n بالرد على النص لتحوليه الى مقطع صوتي للغه الانكليزية\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر القفل$",
    command=("اوامر القفل", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر القـفـل \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.قفل + الاضافة` ) \n تكتب الامر مع الاضافة لقفل شي معين في المجموعة \n\nالاضافات  : \n - الدردشه  : لقفل ارسال الرسائل \n- الوسائط   : لقفل ارسال الوسائط\n - الملصقات  : لقفل ارسال الملصقات\n- الروابط  : لقفل ارسال الروابط\n- المتحركه  : لقفل ارسال المتحركه\n- الالعاب  : لقفل ارسال الالعاب الانلاين\n- الانلاين  : لقفل ارسال البوتات الانلاين\n- التصويت  : لقفل ارسال التوصيتات \n- الكل :  لقفل ارسال كل شي\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
@jmthon.ar_cmd(
    pattern="اوامر الفتح$",
    command=("اوامر الفتح", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الفـتـح \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.فتح + الاضافة` ) \n تكتب الامر مع الاضافة لفتـح شي معين في المجموعة \n\nالاضافات  : \n - الدردشه  : لفتح ارسال الرسائل \n- الوسائط   : لفتح ارسال الوسائط\n - الملصقات  : لفتح ارسال الملصقات\n- الروابط  : لفتح ارسال الروابط\n- المتحركه  : لفتح ارسال المتحركه\n- الالعاب  : لفتح ارسال الالعاب الانلاين\n- الانلاين  : لفتح ارسال البوتات الانلاين\n- التصويت  : لفتح ارسال التوصيتات \n- الكل :  لفتح ارسال كل شي\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر المنع$",
    command=("اوامر المنع", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الـمنـع \n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر \n\n- ( `.منع + الكلمة` ) \n لمـنع الـكلمة في الـدردشة وسيتم حذفها عند ارسالها من اي شخص \n\n- ( `.الغاء منع + الكلمة` ) \n لالغاء منع الكلمة والسماح للجميع بأرسالها في الدردشة\n\n- ( `.قائمة المنع` ) \nلاظهـار قائمه الكـلمات الـتي منعـتها في الـدردشـه \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 1$",
    command=("تسلية 1", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 1 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.غبي` )\n- ( `.القنابل` )\n- ( `.اتصل` )\n- ( `.قتل` )\n- ( `.شنو` )\n- ( `.طوبة` )\n- ( `.مربعات` )\n- ( `.حلويات` )\n- ( `.نار` )\n- ( `.شحن` )\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 2$",
    command=("تسلية 2", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 2 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.افكر` )\n- ( `.متت` )\n- ( `.ضايج` )\n- ( `.ساعه` )\n- ( `.مح` )\n- ( `.قلب` )\n- ( `.جيم` )\n- ( `.الارض` )\n- ( `.قمر` )\n- ( `.اقمار` )\n- ( `.قمور` )\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 3$",
    command=("تسلية 3", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 3 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.نجمه` )\n- ( `.مكعبات` )\n- ( `.مطر` )\n- ( `.تفريغ` )\n- ( `.فليم` )\n- ( `.احبك` )\n- ( `.طائره` )\n- ( `.شرطه` )\n- ( `.النضام الشمسي` )\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 4$",
    command=("تسلية 4", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 4 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.قاتل` )\n- ( `.عين` )\n- ( `.افكرر` )\n- ( `.افعى` )\n- ( `.رجل` )\n- ( `.مايكرو` )\n- ( `.فايروس` )\n- ( `.قطار` )\n- ( `.نيكول` )\n- ( `.موسيقى` )\n- ( `.رسم` )\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 5$",
    command=("تسلية 5", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 5 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.تحميل` )\n- ( `.مربع` )\n- ( `.دائره` )\n- ( `.انيم` )\n- ( `.بشره` )\n- ( `.قرد` )\n- ( `.يد` )\n- ( `.العد التنازلي` )\n- ( `.قلوب` )\n\nتحذيـر : لا تكثر من استخدام هذه الاوامر لانها قد تسبب ضغط على حسابك او تعليقه من ارسال الرسائل لفترة وجيزة.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 6$",
    command=("تسلية 6", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "قائمة اوامر التسـلية 6 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.ترامب` + النص )\n- ( `.مودي` + النص )\n- ( `.بنر` + النص )\n- ( `.كانا` + النص )\n- ( `.تويت` + المعرف ; النص )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 7$",
    command=("تسلية 7", plugin_category),
               )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
         "قائمة اوامر التسـلية 7 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.تراش` بالرد على ملصق/صورة )\n- ( `.تهديد` بالرد على ملصق/صورة )\n- ( `.فخ`  بالرد على ملصق/صورة + الاسم1 ; الاسم2 )\n- ( `.بورن`  بالرد على ملصق/صورة + المعرف ; النص )\n- ( `.تويت` + المعرف ; النص )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="تسلية 8$",
    command=("تسلية 8", plugin_category),
               )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
         "قائمة اوامر التسـلية 8 :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.نص` + النص )\n- ( `.ستيكر` + النص )\n- ( `.هونك` + النص )\n- ( `.تغريد` + النص )\n- ( `.غلاكس` + النص )\n- ( `.دوغي` + النص )\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
           )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الملصقات$",
    command=("اوامر الملصقات", plugin_category),
           )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر الملصقـات\n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر\n\n- ( `.ملصق` )\nبالرد على الملصق لأخذه و عمل حزمه خاصة بك و اضافته بها\n\n- ( `.حزمة` )\nبالرد على الملصق لنسخ الحزمة كاملة بداخل حزمة ملصقاتك الخاصة\n\n- (`.معلومات_الملصق` )\nبالرد على الملصق لعرض معلومات الحزمة\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
            )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التكرار$",
    command=("اوامر التكرار", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر التـكرار\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.كرر  +عدد التكرار  +بالرد على الرسالة` )\n يقوم بتكرار النصوص والوسائط بالرد على الرسالة او الصورة \nمثال  :  ( بالرد على صورة  `.كرر 10` )\n\n- ( `.تكرار الملصق + بالرد على ملصق` )\n بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها\n\n- (`.مكرر  + وقت بالثواني  + عدد  + بالرد` )\n بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين .\nمثال  : بالـرد على نص ( `.مكرر 10 2` )  عندها سترسل 10 رسائل نصية ( النص الي رديت عليه ) بفاصل ثانيتين بين كل رسالة\n\n- ( `.ضع تكرار` + العدد )\nلمنع التكرار بالمجموعة الخاصة بك بالعدد الذي وضعته للعودة للوضع الطبيعي ضع 999999.\nمثال : ( `.ضع تكرار 10 )\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
            )
            #@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر السبام$",
    command=("اوامر السبام", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر السبـام\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.سبام + كلمـة` )\nيقوم بتفصيخ احرف الكلمه وارسالها جربه بنفسك\n\n- ( `.وسبام + كلـمة` )\nكتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
             )
             #@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التنظيف$",
    command=("اوامر التنظيف", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر التنظيـف\n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر\n\n- ( `.تنظيف + عدد الرسائل` )\nيقوم بحذف الرسائل اكتب الامر وعدد معين من الرسائل سيقوم بحذفها \n\n- ( .تنظيف  + الاضافة )\n يـجب وضع الشـارحه مع الاضافة (-)\nمثـال  :  ( `.تنظيف -ح` )  <سيقوم بحذف المتحركات في الدردشة>\nالاضافات : \n (-ب) : لحـذف الرسائل الـصوتية\n (-م): لحـذف الملفات\n (-ح): لحـذف المتحـركه\n (-ص): لحـذف الـصور\n (-غ): لحـذف الاغاني\n (-ق): لحـذف الـملصقات\n (-ر): لحـذف الـروابط \n(-ف): لحـذف الفـيديوهـات\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
          )               

@jmthon.ar_cmd(
    pattern="اوامر المسح$",
    command=("اوامر المسح", plugin_category),
            )
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شـرح عـن اوامـر المسـح\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.مسح  + بالرد على النص` )\nفقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n\n- ( `.حذف رسائلي` )\nاكتب الامر في اي مكان وسيقوم بحذف جميع رسائلك في الدردشه حتى لو لم يكن لديك صلاحيات \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
         )
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern= "اوامر الوقت والتاريخ$",
    command=("اوامر الوقت والتاريخ", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الوقت والتاريخ :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.تاريخ` )\nبالرد على الشخص او كتابة معرفه مع الامر لعرض سجل اسماء حسابه.\n\n- ( `.الوقت` )\nلعرض الوقت على شكل ملصق\n\n- ( `.وقت` )\nلعرض الوقت على شكل كتابة\n\n- ( `.مؤقت` + الوقت + النص )\nيقوم بإرسال رسالة مؤقتة و حذفها بعد وقت معين\n- مثـال : `.مؤقت 5 جـيبثون`\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر كورونا$",
    command=("اوامر كورونا", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر كورونا :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر\n\n- ( `.كورونا` + الدولة )\nللحصول على احصائيات فايروس كورونا\n- مثـال : `.كورونا Morocco`\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الصلاة$",
    command=("اوامر الصلاة", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الصلاة :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.صلاة` )\nاكتب الامر مع اسم محافظتك باللغه الانكليزية للحصول على اوقات الصلاة\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر مساعدة$",
    command=("اوامر مساعدة", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر المساعدة :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.موقع` + المكان )\nللحصول على مكان في الخريطه و ارساله لك\n\n- ( `.صورة` )\nبالرد على الشخص للحصول على صورة حسابه الشخصية.\n\n- ( `.صوره كلها` )\nللرد على الشخص للحصول على صور حسابه الشخصية كلها.\n\n- ( `.سرعة الانترنت` )\nارسل الامر لقياس سرعة الانترنت\n\n- ( `.حساب` )\nكتابة الامر مع معادلة رياضية و سيقوم بحلها و ارسالها لك\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="فارغ $",
    command=("فارغ ", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر، :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.معلومات` )\nارسل الامر في المجموعة لرؤية معلومات المجموعة او اكتب الامر مع معرف المجموعة\n\n- ( `.البوتات` )\nارسل الامر في المجموعة لرؤية البوتات الموجودة في المجموعة او اكتب الامر مع معرف المجموعة\n\n- ( `.المشرفين` )\nارسل الامر في المجموعة لرؤية مشرفين المجموعة او اكتب الامر مع معرف المجموعة\n\n- ( `.الاعضاء` )\nارسل الامر في المجموعة لرؤية اعضاء المجموعة او اكتب الامر مع معرف المجموعة\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الروابط$",
    command=("اوامر الروابط", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الروابط :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.دنس` + الرابط )\nلكشف نظام دومين موقع معين اكتب الامر مع الرابط\n\n- ( `.مصغر` )\nبالرد على الرابط او وضع الرابط مع الامر ليقوم بتصغيره\n\n- ( `.رابط_مخفي` )\nبالرد على الرابط لاخفاء الرابط و جعله في مسافه معينة جرب الامر بنفسك\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="اوامر التحذيرات$",
    command=("اوامر التحذيرات", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر التحذيرات :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.تحذير + السبب` )\nبالرد على الشخص ليقوم بتحذيره يمكنك وضع سبب كذلك\n\n- ( `.التحذيرات` )\nبالرد على الشخص ليقوم باظهار تحذيراته.\n\n- ( `.حذف التحذيرات` )\nبالرد على الشخص لحذف تحذيراته.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر اللستة$",
    command=("اوامر اللستة", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر اللستة :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.لستة` )\nيقوم بصنع لستة شفافة لمنشور معين\nشـرح الامـر  : \n https://t.me/Jepthon\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الملكية$",
    command=("اوامر الملكية", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الملكية :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.ملكية` )\nيقوم بكتابة التمر في القناة التي تريد تحويلها لشخص و بكتابة الامر مع معرف الشخص\n\n لاستخدام امر نقل الملكية تحتاج لوضع TG_2STEP_VERIFICATION_CODE و معه رمز حسابك في الفارات \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر السليب$",
    command=("اوامر السليب", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر السليب :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.سليب` + السبب)\nيقوم بادخالك في وضع غير المتصل يقوم بالرد على اي شخص برسالة يقول فيها انك غير متواجد.\n- مثـال : `.سليب نايم`\n\n- ( `.سليب_ميديا` + السبب )\nيقوم بنفس وظيفة الامر العادي غير انه يمكنك ارفاق صورة او متحركة بالرد عليها مع الامر.\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الاسم$",
    command=("اوامر الاسم", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الاسم الوقتي :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.اسم وقتي` )\nبكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها .\n\n- ( `.انهاء اسم وقتي` )\nلانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n- ( `.الصورة الوقتية` )\n لوضع صورة تتغير مع الوقت\n\n- ( `.انهاء الصورة الوقتية` )\n لأنهاء الصورة واسترجاع الصورة الاصلية➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر البايو$",
    command=("اوامر البايو", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر البايو الوقتي :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.بايو وقتي` )\nبكتابة الامر لاضافة بايو وقتي حسب منطقة التي وضعتها .\n\n- ( `.انهاء بايو وقتي` )\nلانهاء البايو الوقتي و ارجاع البايو الطبيعي .\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر التشغيل$",
    command=("اوامر التشغيل", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر التشغيل :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.اعادة التشغيل` )\nلاعادة تشغيل البوت و ارجاعة الى شكله الطبيعي كما كان في الاول فقط ارسل الامر .\n\n- ( `.تحديث` )\nفقط ارسل الامر للتاكد اذا كان هناك تحديثات من مطورين السورس .\n\n- ( `.التحديثات تشغيل` )\nيستخدم هذا الامر لارسال رسالة تجريبية تلقائية لرؤية البوت اذا ما كان شغال بعد اعادة التشغيل او التحديث سيرس امر `.بنك` ولايقافه ارسل `.التحديثات ايقاف` .\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الاطفاء$",
    command=("اوامر الاطفاء", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الاطفاء :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.اطفاء` )\nلالغاء تشغيل البوت و يجب اعادة تشغيله من هيروكو .\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
#@GGGNE  -  @RR9R7
@jmthon.ar_cmd(
    pattern="اوامر الكشف$",
    command=("اوامر الكشف", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الكشف :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.الايدي` )\nبالرد على الشخص او كتابة معرفه مع الامر لعرض معلوماته.\n\n- ( `.ايدي` )\nبالرد على الشخص لعرض معلوماته\n\n- ( `.كشف` )\nبالرد على الشخص لعرض معلوماته بشكل مبسط\n\n- ( `.رابط الحساب` )\nيالرد على الشخص للحصول على رابط حساب الشخص\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="اوامر كوكل$",
    command=("اوامر كوكل", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر كوكل :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.صور +  عدد الصور + نص` )\nللحصول على صور من متصفح كوكل بكتابة الامر وعدد الصور الحد 10 واسم النص\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر الاذاعه$",
    command=("اوامر الاذاعه", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح اوامر الـتوجيه والأذاعـة :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.وجه + نص` )\nلعمـل اذاعـة للـنص في المجـموعـات اكتب الامر ونـصـك\n\n- ( `.حول + نص` )\nلعمـل اذاعـة للـنص للـ الدردشـات الخـاصة اكتب الامر ونـصـك\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)


@jmthon.ar_cmd(
    pattern="امر الصورة الذاتية$",
    command=(" امر الصورة الذاتية", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "شرح امر الصورة الذاتية :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.ذاتية` )\n بالـرد عـلى الصـورة ذاتيـة الـتدمير ليـقوم بـحفظها وارسالـها لك فـي الرسائل الـمحفوظة بسرية وبـدون عـلم الـطرف الأخر\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر التسلية$",
    command=("اوامر التسلية", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"قائمة اوامر التسلية :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.تسلية 1` )\n- ( `.تسلية 2` )\n- ( `.تسلية 3` ) \n- ( `.تسلية 4` )\n- ( `.تسلية 5` )\n- ( `.تسلية 6` )\n- ( `.تسلية 7` )\n- ( `.تسلية 8` ) \n- ( `.فيك typing 300` ) \n- ( `.رفع ادمن` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="اوامر التحشيش$",
    command=("اوامر التحشيش", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"قائمة اوامر التحشيش :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n**جميع اوامـر التحشيش تستخـدم بالـرد عـلى الشخص**\n\n- ( `.رفع تاج` )\n- ( `.رفع بكلبي` )\n- ( `.رفع مطي` )\n- ( `.رفع جلب` ) \n- ( `.رفع قرد` )\n- ( `.رفع مرتي` )\n- ( `.رفع زوجي` )\n- ( `.نسبة الانوثة` )\n- ( `.نسبة الحب` )\n- ( `.نسبة الغباء` ) \n- ( `.رفع زاحف` ) \n- ( `.رفع كحبة` ) \n- ( `.رفع فرخ` ) \n- ( `.رزله` ) \n- ( `.رفع صاك` ) \n- ( `.رفع حاته` ) \n- ( `.رفع بقره` ) \n- ( `.رفع ايجة` )\n- ( `.رفع زبال` )\n- ( `.رفع كواد` )\n- ( `.رفع ديوث` )\n- ( `.رفع مجنب` )\n- ( `.رفع مميز` )\n- ( `.رفع ادمن` )\n- ( `.رفع منشئ` )\n- ( `.رفع مالك` )\n- ( `.رفع وصخ` )\n- ( `.نسبة الكذب` )\n- ( `.نسبة الدياثه` )\n- ( `.نسبة الشذوذ` )\n- ( `.نسبة الجمال` )\n- ( `.نسبة الخيانه` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر التحويل$",
    command=("اوامر التحويل", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"شـرح عـن اوامـر تـحويل الصـيغ :\n➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه الاوامر\n\n- ( `.تحويل صورة` )\n بالرد على الملصق لتحويله الى صورة\n\n- ( `.تحويل ملصق` )\n بالرد على الصورة لتحويلها الى الملصق\n\n- ( `.تحويل voice` )\nبالرد على مقطع اغنية لتحويله على شكل بصمة صوتية\n\n- ( `.تحويل mp3` )\nبالرد على البصمة الصوتية لتحويلها على شكل  مقطع mp3\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر الجهات$",
    command=("اوامر الجهات", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الجهات والاضافة\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.ضيف +  رابط مجموعة` )\n  يستخدم الامر لاخذ اعضاء من مجموعة ثانية واضافتهم في مجموعتك ترسل الامر مع اربط قروب عام في مجموعتك للاضافة \n مثال :  .ضيف https://t.me/JepthonSupport \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر الحساب$",
    command=("اوامر الحساب", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الحساب والقنوات والمجموعات التي تديرها\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.معلوماتي` ) \n( `.قائمه قنواتي` ) \n( `.قائمه كروباتي` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="اوامر الالعاب$",
    command=("اوامر الالعاب", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الالعاب\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.بلي` )\n- ( `.كت` )\n- ( `.خيروك` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)

@jmthon.ar_cmd(
    pattern="بصمات ميمز$",
    command=("بصمات ميمز", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة بصمات الميمز\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.تخوني` )\n- ( `.مستمرة الكلاوات` )\n- ( `.احب العراق` )\n- ( `.احبك` )\n- ( `.اخت التنيج` )\n- ( `.اذا اكمشك` )\n- ( `.اسكت` )\n- ( `.افتهمنا` )\n- ( `.اكل خرا` )\n- ( `.العراق` )\n- ( `.الكعده وياكم` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)

@jmthon.ar_cmd(
    pattern="بصمات ميمز2$",
    command=("بصمات ميمز2", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة بصمات الميمز\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.الكمر اني` )\n- ( `.اللهم لا شماته` )\n- ( `.اني مااكدر` )\n- ( `.بقولك ايه` )\n- ( `.تف على شرفك` )\n- ( `.شجلبت` )\n- ( `.شكد شفت ناس` )\n- ( `.صباح القنادر` )\n- ( `.ضحكة فيطية` )\n- ( `.طار القلب` )\n- ( `.غطيلي` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)

@jmthon.ar_cmd(
    pattern="بصمات ميمز3$",
    command=("بصمات ميمز3", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.في منتصف الجبهة` )\n- ( `.لاتقتل المتعه` )\n- ( `.لا لتغلط` )\n- ( `.لا يمه لا` )\n- ( `.لحد يحجي وياي` )\n- ( `.ماادري يعني` )\n- ( `.منو انت` )\n- ( `.مو صوجكم` )\n- ( `.خوش تسولف` )\n- ( `.يع` )\n- ( `.زيج` )\n- ( `.زيج2` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)

@jmthon.ar_cmd(
    pattern="بصمات ميمز4$",
    command=("بصمات ميمز4", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.يعني مااعرف` )\n- ( `.يامرحبا` )\n- ( `.منو انتة` )\n- ( `.ماتستحي` )\n- ( `.كعدت الديوث` )\n- ( `.عيب` )\n- ( `.عنعانم` )\n- ( `.طبك مرض` )\n- ( `.سييي` )\n- ( `.سبيدر مان` )\n- ( `.خاف حرام` )\n- ( `.تحيه لاختك` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)
	
@jmthon.ar_cmd(
    pattern="بصمات ميمز5$",
    command=("بصمات ميمز5", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر بصمات الميمز\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.امشي كحبة` )\n- ( `.امداك` )\n- ( `.الحس` )\n- ( `.افتهمنا` )\n- ( `.اطلع برا` )\n- ( `.اخت التنيج` )\n- ( `.اوني تشان` )\n- ( `.اوني تشان2` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)
@jmthon.ar_cmd(
    pattern="م21",
    command=("م21", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الفارات\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.وضع توقيت` )\n-بالرد على المنطقة الزمنية \n- ( `.وضع رمز الاسم` )\n- بالرد على الرمز المراد وضعه \n- ( `.وضع البايو` )\n- بالرد على النبذا المراد وضعها \n- ( `.وضع الصورة` )\n- بالرد على الصورة المراد وضعها وكتابة الامر \n- ( `.وضع زخرفة الارقام` )\n- بالرد على الارقام المراد وضعها وكتابة الامر \n- ( `.وضع اسم` )\n- بالرد على الاسم المراد وضعه وكتابة الامر\n- ( `.وضع كروب التخزين` )\n- بالرد على الايدي المحادثة المراد جعلها كروب التخزين \n- ( `.وضع كروب الحفظ` )\n-بالرد على الايدي المحادثة المراد جعلها كروب الحفظ \n- ( `.توقيت العراق` )\n- لوضع الساعة بتوقيت العراق \n- ( `.توقيت السعودية` )\n - لوضع الساعة بتوقيت السعودية \n- ( `.توقيت مصر` )\n -لوضع الساعة بتوقيت مصر \n- ( `.توقيت الاردن` )\n- لوضع الساعة بتوقيت الاردن \n- ( `.توقيت اليمن` )\n- لوضع الساعة بتوقيت اليمن \n- ( `.توقيت سوريا` )\n- لوضع الساعة بتوقيت سوريا\n- تنويه : عندما تريد حذف الفار استعمل الامر (ازالة) بدل كلمة (وضع)\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)
@jmthon.ar_cmd(
    pattern="اوامر الوهمي",
    command=("اوامر الوهمي", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الوهمي\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌯︙اختر احدى هذه الاوامر\n\n- ( `.كتابة` )\n-مثال : .كتابة + عدد الثواني \n- ( `.صوتية` )\n- مثال : .صوتية + عدد الثواني \n- ( `.فيد` )\n- مثال : .فيد + عدد الثواني \n- ( `.لعبة` )\n- مثال : .لعبة + عدد الثواني\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"

)
