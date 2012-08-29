---
layout: post
title: "Octopress安装"
date: 2012-08-29 16:56
comments: true
categories: 
---
##Octopress基于Ruby,需要Ruby环境.
1.  Windows下,下载[RubyInstaller](http://rubyforge.org/frs/?group_id=167)，[Development Kit](https://github.com/oneclick/rubyinstaller/wiki/development-kit)
2.  默认安装完ruby后，需要确保`C:\Ruby192\bin`在windows当前用户的`path`环境变量下
3.  安装Development Kit
*   将 DevKit 自解压包释放到 `C:\DevKit` 
*   在 Windows CMD 窗口中执行 `ruby dk.rb init`
*   在 Windows CMD 窗口中执行 `ruby dk.rb install`
4.  因为ttp://rubygems.org可能被墙，换成国内源

            gem sources -l  #查看源地址
            gem sources -a http://ruby.taobao.org/ #添加淘宝的   ruby源地址
            gem sources --remove http://rubygems.org/ #删除rubygems源
            gem sources -l #再查看一下源地址,确保只有http://ruby.taobao.org/一个源
            gem update --system
            gem update
            gem install rdoc bundler


## Octopress 使用 Python 编写的代码加亮系统 pygments，需要安装 python
1.  默认安装python
2.  安装easy_install
    *   下载[setuptools](http://pypi.python.org/pypi/setuptools)并安装
    *   在其目录下用cmd使用`easy_install pygments`

## 软件安装后的 Windows 7 环境说明和配置
1.  两种命令行环境 
    *   Windows 7 自己的 CMD窗口，用于输入 DOS 类命令
    *   MINGW/Git Bash 窗口启动了 bash，可以输入 Linux 类命令
2.  环境变量
    *   在 Windows 的 “高级系统设置” 中设置的 环境变量 可以被 MINGW 窗口继承
        *  设置 LANG 和 LC_ALL 两个环境变量，其值均设置为 `zh_CN.UTF-8`
        *  在 CMD 窗口中测试： `echo %LANG% %LC_ALL%`
        *  在 MINGW 窗口中测试： `echo $LANG $LC_ALL`
    *   MINGW/Git Bash 窗口启动了 bash，可以使用 ~/.bash_profile 环境设置文件设置环境变量、命令别名等

            $ echo "export LANG LC_ALL" > ~/.bash_profile
            $ echo "alias ll='ls -l --color=tty'" >> ~/.bash_profile
            $ echo "alias ls='ls --color=tty'" >> ~/.bash_profile

    *   注意：若希望~/.bash_profile中的设置生效，请启动MINGW/Git Bash窗口，而不是Windows的CMD窗口

## 安装Octopress

            # 1. 克隆 Octopress
            $ cd ~/Documents
            $ git clone git://github.com/imathis/octopress.git lwd2136.github.com
            $ cd ~/Documents/lwd2136.github.com
            # 2. 修改 Octopress 的 GEM 源
            $ notepad Gemfile #修改你的ruby索取地址
            将行 ： source "http://rubygems.org/"
            改为 ： source "http://ruby.taobao.org/"
            # 3. 安装 Octopress 所需的GEM组件
            $ bundle install
            $ rake install #安装预设的Octopress theme

##    git
1.  注册[github](https://github.com/)
2.  建立`lwd2136.github.com`的`repo`
3.  下载安装[git](http://git-scm.com/downloads)
4.  ssh-key
https://help.github.com/articles/generating-ssh-keys
5.  在本地版本库中设置远程版本库的别名
`$ git remote add myblog git@github.com:lwd2136/lwd2136.github.com.git`

## 配置和使用Octopress
*   编辑 _config.yml 文件 ，根据您自己的需要修改其值, [参考](http://octopress.org/docs/configuring/)
*   首次提交`rake setup_github_pages`后，需要输入github pages的repo地址，格式是`git@github.com:lwd2136/lwd2136.github.com.git`
1.  `rake generate` ： 生成静态文件
2.  `rake preview` ： 在本机4000端口生成访问内容
3.  `rake deploy` ： 发布文件到 github

**使用rake deploy后，会将public活页夹下的所有文件拷贝到分支管理目录_deploy活页夹中，也即是<yourname>.github.com的master分支目录，然后上传到github。如需对源代码进行版本管理，需要另外建立source分支，并使用基本的git命令进行版本管理。**

## 更新管理源码的仓库分支
因为发布的只是生成的静态页面，需要在项目里建立source分支用于保存整个项目源代码（配置、markdown文件等）。

            git add .
            git commit -m "add some changes"
            git push myblog source
