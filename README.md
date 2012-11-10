# 萌姬 -- 开源可扩展的日萌计票器

## 说明

这是个命令行界面使用简单到爆的计票器，自带简单的去低级伪功能。图线生成
功能在 OO 重构之后暂时没有调整，这些留待明年再解决吧（如果明年还有萌战
的话）。

2012 日萌已经结束，本计票器将于明年战期重新启动开发。代码里大部分注释
都是英汉双语的，有想研究的可以瞄一两眼，但是就别把这堆东西当作什么宝贝了。


## 支持平台

装有 Python 的系统。因为各种原因我很长一段时间不能主要使用 Windows 进行
日常活动；但是 Windows 是目前常见操作系统里唯一没有自带 Python 的，所以
这部分（我承认是大部分）用户是暂时悲剧了，因为我没有办法在 Windows 环境
下测试和打包。其他的平台，像 Mac OS X 和 Linux, BSD 系的操作系统都是
支持的。

Windows 环境的测试我会在进入 Windows 环境之后第一时间着手进行，之后将
择机发布绿色运行包。大家都不喜欢安装程序，对吧？


## 使用方法

以Linux 系统为例，假设你已经可以使用 pip 和 git 了。如果没有的话，参照
发行版的说明先装上，类似这样：

    $ sudo apt-get install pip git  # Debian/Ubuntu 系
    $ sudo emerge pip git  # Gentoo
    $ sudo yum install pip git  # RH 系

安装 virtualenv 虚拟环境，避免影响系统全局的包版本：

    $ pip install virtualenv

接下来其实是下载软件和部署依赖关系的步骤：

    $ mkdir path/to/install/into  # 换成你想安装的目录位置
    $ cd path/to/install/into
    $ virtualenv moehime
    $ cd moehime
    $ git clone https://github.com/xen0n/moehime.git  # 拉下整个版本库
    $ pip install -r moehime/requirements.txt  # 安装依赖关系
    $ mkdir configs  # 建立一个 config 文件目录
    $ ln -s moehime/scripts/driver\_cli.py driver.py

安装完成。使用方法：

    $ cd path/to/install/into/moehime  # 进入安装位置的 moehime 目录
    $ . bin/activate  # 激活虚拟环境

以上两步不必每次都做，激活虚拟环境之后只要执行

    $ ./driver.py

就可以了。


## 开发路线图

第一步，整理架构：从面向过程到适当的面向对象。这一步已经在国庆完成了。

第二步，完善核心功能：页面缓存，自动票箱地址获取；

第三步，图形界面：初步打算用 PySide 或者 PyQt 实现（其实差不多），初期
界面要简洁，减少维护负担，皮肤之类的功能不要在这时候实现，网络并发模型
可以先用着线程什么的（可惜因为要支持 Windows 的原因 gevent 用不成了）；

第四步，进阶核心功能：实现常见的易于操作的去伪过滤器，比如综合了票尾和
投票时间的去伪，重复 code 时萌文的判断之类，这些是计票器的招牌功能；

第五步，进阶界面功能：换肤什么的，然后是对网络并发的改进。

先写这么多，后面的路谁知道能走到什么程度，等到那个时候也许萌战就不办了
也说不定……就先这样吧
