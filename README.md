# 西电健康卡脚本

## 执行要求
1. 仅本地运行，包括你的电脑/路由器/手机。本人不打算支持Github Action等在云端功能。
2. 电脑不能挂全局代理，要不然你会被定位到外国。

## 如何运行(Windows)
1. 先按照官方步骤，用手机填报一遍：西电企业号->移动门户->健康卡
2. 将脚本文件放在一个重要的，不易发现的位置上。在脚本第10行和第11行的引号里，填入自己的一站式账户和密码(没有加密啊，一定要藏好了！)
3. 下载python：请去[官网](https://www.python.org/downloads/windows/)下载，选择最新版的"Windows installer (64-bit)"。安装的时候，一定要选上"ADD TO PATH"选项。
4. 在存放脚本的位置，打开**管理员权限**的Powershell。
![这么打开啊](https://legacy.superbart.xyz/picture/Upload%20Health%20Situation/Screenshot_20220209_162424.jpg)  
5. 在打开的窗口中，分别输入以下两个命令：
```powershell
pip install pyppeteer
python .\reportNcov-outschool.py
```
如果出现以下字样，你成功了
```powershell
登陆成功，并已经跳转到填报界面
位置信息已经获取，你目前在: 幻想乡 红魔馆
信息已经上报完毕，你的情况是: 今天已经填报了
```
**各位一定要注意你的位置信息是不是显示正确了！**
5. Windows计划任务配置
    1. 同时按下Win+R，弹出的窗口中输入`taskschd.msc`
    2. 打开“计划任务”，右面找"创建基本任务"，点击之。
    ![](https://legacy.superbart.xyz/picture/Upload%20Health%20Situation/Screenshot_20220209_162838.jpg)
    3. 打开的窗口中，起名字不说了。触发器选"每天"，自己选个合适的时间(电脑在那时一定是开机状态)。
    ![](https://legacy.superbart.xyz/picture/Upload%20Health%20Situation/Screenshot_20220209_163117.jpg)
    4. 在执行程序的时候写python可执行文件的安装路径，参数就是你脚本的所在路径。最后完成的时候，选择"打开此任务属性的对话框"。
    ![](https://legacy.superbart.xyz/picture/Upload%20Health%20Situation/Screenshot_20220209_163426.jpg)
    5. 在新打开的窗口中，选择"条件"，然后把电源选项更改，之后保存。
    ![](https://legacy.superbart.xyz/picture/Upload%20Health%20Situation/Screenshot_20220209_164304.jpg)

## 在Linux上运行的提示
1. 安装软件包`python-pyppeteer`。
2. 确保电脑有chromium内核的浏览器，要不然本脚本会自己下载一个浏览器。
3. 一定要修改第19行，浏览器可执行文件的位置。
4. 安装`cronie`软件包来配置自动运行。

## 本人不建议配置Github Action
1. 你的一站式帐号和密码存在了Github，很容易就泄露了，现在信息泄露的很厉害！
2. 本人的脚本每次运行，都要根据你电脑的ip地址获取定位信息。你要是放在Github上，你就出国啦！

如果你真的不希望在本地跑，请使用[hawa130](https://github.com/hawa130/health-card-checkin)或者[Robotxm](https://github.com/Robotxm/AutoXduNCovReport)的方案，这俩是专门为Github Action设计的。

## 感谢和敬仰
[python代码的启发](https://github.com/hawa130/health-card-checkin)  
[yaml文件的启发](https://github.com/Robotxm/AutoXduNCovReport)  
[超级简洁的晨午晚检脚本](https://github.com/inkhog/xdncov)  
[xidian-script的晨午晚检脚本](https://github.com/xdlinux/xidian-scripts/blob/master/Python/check_in.py)

## 本脚本授权协议翻译
Unlicense授权协议

本软件自由，无约束地，向公有领域发布。<br>
This is free and unencumbered software released into the public domain.

每个人都可以出于各种目的(商业或非商业目的)，以任何手段，自由地复制，更改，发布，使用，编译，售卖，这个软件。或以源代码的形式，或以编译过的二进制文件形式。<br>
Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

在承认版权法的司法管辖区内，软件的作者(们)愿向公有领域奉献出在该软件里的所有版权权益。我们为了社会大局的利益，舍弃了作者(们)的下一代们的好处。我们在此开诚布公地向各位奉献，即永久性地放弃该软件在版权法下的现有权利和将来权利。<br>
In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

**本软件是"按原样"提供，不做任何明示或暗示的保证，包括但不限于对适销性、定用途适用性和非侵权性的保证。在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，作者均不承担因本字幕或本字幕的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任。**<br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

欲知更多信息，请访问 https://unlicense.org<br>
For more information, please refer to <https://unlicense.org>

附带条款两则：
1. 如使用本软件，即表示您知晓(acknowledge)：
	* 作者反对996等不合理竞争和劳动。
    * 作者反感官僚化的任何东西，包括无意义的会议，课程等。
2. 本附带条款不具有强制性，无论是法律上的，还是其他方面。你在发行时可以删除附带条款。

Two additional terms：

1. As long as you use this software, you acknowledge:
	* The author against improper competition and labour, for example,996 working schedule.
    * The author dislike anything which are bureaucratization, such as meaningless meeting and courses.

2. These additional terms have no mandatory in either laws, or other fields. You may delete additional terms when distriubuing this software.