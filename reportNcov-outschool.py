#!/usr/bin/python
# Automatic upload your health situation outside school. For xidian.
# Based on "health-card-checkin" by hawa130, which could be found at
# https://github.com/hawa130/health-card-checkin
# Copyright 2022 SuperBart. Released under Unlicense.

import asyncio
import pyppeteer

# USERNAME 输入你的学号 PASSWORD 输入你的统一认证密码(一定要输入在双引号内，这是个字符串)
USERNAME = ""
PASSWORD = ""
LOGIN = "https://xxcapp.xidian.edu.cn/ncov/wap/default/index"
REPORT = "https://xxcapp.xidian.edu.cn/ncov/wap/default/save"

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
    # 获取位置信息，执行完那个函数后，等待2秒钟
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
