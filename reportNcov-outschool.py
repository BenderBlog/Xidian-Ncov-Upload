#!/usr/bin/python
'''
Automatic upload your health situation outside school. For xidian.
Based on "health-card-checkin" by hawa130, which could be found at
https://github.com/hawa130/health-card-checkin

2022 SuperBart, released under SuperBart Public Domain Software License

SuperBart Public Domain Software License

Following are non-additional terms:

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

Two additional terms:

1. As long as you use this software, you acknowledge that the author of
the software strongly against improper competition and labour, for
example, 996 working schedule. And he or she dislike anything which are
bureaucratization, such as meaningless meeting and courses.

2. The additional terms have no mandatory in either laws, or other fields.
You don't need to agree with the additional terms in order to use this
software. And you may delete the additional terms when using this software,
'''

import asyncio
import pyppeteer

# USERNAME 输入你的学号 PASSWORD 输入你的统一认证密码(一定要输入在双引号内，这是个字符串)
USERNAME = ""
PASSWORD = ""
LOGIN = "https://xxcapp.xidian.edu.cn/ncov/wap/default/index"
REPORT = "https://xxcapp.xidian.edu.cn/ncov/wap/default/save"
# 如果定位很不好用的话，可以从 http://geoinfo.hawa130.com/ 获取信息并贴在三个引号中间
PLACE = ‘’‘ ’‘’

async def commit(username, password):
    # 贴士 查阅一下你电脑的Chrome/Chromium安装地址 然后上网搜怎么加参数
    # 否则他会自动下载个新的chromium:-P
    browser = await pyppeteer.launcher.launch(executablePath="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    page = await browser.newPage()
    await page.goto(LOGIN)
    await page.evaluate("vm.username = " + str(username) + ";")
    await page.evaluate("vm.password = \"" + password + "\";")
    await page.evaluate("vm.login()")
    await page.waitForNavigation({ "waitUntil": "domcontentloaded" })
    print("登陆成功，并已经跳转到填报界面")
    if PLACE != " ":
        print("填报用户信息")
        # 现在可以伪造信息啦
        await page.evaluate("(pl) => vm.locatComplete(pl)", json.loads(PLACE))
    else:
        print("直接获取信息")
        await page.evaluate("vm.getLocation()")
        await asyncio.sleep(2)
    print("位置信息已经获取，你目前在:",await page.evaluate("vm.info.province"),await page.evaluate("vm.info.city"))
    await page.evaluate("() => vm.save()")
    situation = await page.waitForResponse(REPORT)
    toPrint = await situation.json()
    print("信息已经上报完毕，你的情况是:",toPrint['m'])
    await browser.close()

if __name__ == "__main__":
    asyncio.run(commit(USERNAME, PASSWORD))

## Got to get her into my life!
