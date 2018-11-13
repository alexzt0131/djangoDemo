# python3.6+django2.0-xadmin-imooc学习记录 #

# 一、开发基础环境搭建 #

	python与模块版本：
		python==3.6.4
		django==2.0.1
		pip 最新
## 1安装python3.6 ##
	下载地址：https://www.python.org/downloads/release/python-364/
	直接安装即可
## 2设置环境变量 ##
	python3 安装文件点击设置环境变量即可
	python2 在PATH中最后添加新安装python的路径如（c:\python27;C:\Python27\Scripts;）Scriptsm目录是模块执行的目录如virtualenv 模块pip、mkvirtualenv等，分号别忘记。
## 3先安装setuptools ##
	python3安装包集成
	下载地址：https://pypi.python.org/pypi/setuptools#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令：python setup.py install
## 4安装pip ##
	python3安装包集成
	下载地址：https://pypi.python.org/pypi/pip#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令:python setup.py install 
## 5安装virtualenv ##
	执行命令 pip install virtualenv
	如果找不到文件或者网络慢可使用国内的pip源地址
		
	阿里云 http://mirrors.aliyun.com/pypi/simple/
	
	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	
	豆瓣(douban) http://pypi.douban.com/simple/
	
	清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
	
	中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

	使用命令：pip install web.py -i http://pypi.douban.com/simple

	如果报错使用：pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

	如果想配置成默认的源，方法如下：
	
		需要创建或修改配置文件（一般都是创建），
		
		linux的文件在~/.pip/pip.conf，
		
		windows在%HOMEPATH%\pip\pip.ini），
		
		修改内容为：
		
		[global]
		index-url = http://pypi.douban.com/simple
		[install]
		trusted-host=pypi.douban.com
	
	
	新建虚拟环境：virtualenv d:\test4 提示结束后转到 test4目录下Script目录运行active激活当前虚拟环境，控制台符号变为(test4) d:\test4\Scripts>，如需退出执行deactive命令即可。
## 6安装virtualenvwrapper ##
	由于virtualenv每次都要进入虚拟环境目录这样很麻烦所以需要安装virtualenvwrapper模块
	
	安装及使用方法：

	0.首先需要在系统变量中指定一个默认的WORKON_HOME的变量，即所有创建的虚拟环境的存放目录，如：d:\virtualnevs 注意不加冒号。（如果不能正常运行，就讲python安装目录中Script目录中的所有文件copy到指定的workon目录中）。
	
	1.安装虚拟环境

	pip install virtualenvwrapper-win ，linux可以去掉-win
	
	2.创建虚拟环境
	会在你当前用户下创建一个Env的文件夹，然后将这个虚拟环境安装到这个目录下
	
	mkvirtualenv 环境名称
	
	3.进入某个虚拟环境
	
	workon 环境名称
	
	4.退出当前环境
	
	deactivate
	
	5.列出全部虚拟环境
	
	lsvirtualenv
	
	6.删除某个虚拟环境
	
	rmvirtualenv 环境名称
	
	7.进入到虚拟环境所在的目录
	
	cdvirtualenv

	不知道你注意没有，这个dajngoTest是灰色的，
	我们可以右键mark为source Root目录，就变成了蓝色，
	这样做的好处就是可以避免包的导入问题，我们在import模块时pycharm会根据设置从而智能提示。如果不mark可能会出现很多我们在pycharm中报红色，但是cmd可以运行的情况。

# 二、Django基础知识 #
## Django的目录结构 ##
	需要新建几个目录：
		0.与工程名相同	存放工程文件的文件夹
		1.apps	  		存放web应用的文件夹
		2.log 	  		存放日志文件的文件夹
		3.static  		存放js、css及图片的文件夹
		4.media			存放用户上传文件的文件夹
		5.template		存放静态页面的文件夹

	在pycharm中可以将apps markdirectory as sourceroot，这样就可以在引入app中文件时不用添加apps了，不过在命令行中就会报错，解决方法是在settings.py中将apps文件夹插入进来加入一下代码即可：
	sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
	
## Django与mysql的链接 ##

	settings.py中设置：
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': '你的库名',
	        'USER': '账号',
	        'PASSWORD': '密码',
	        'HOST': '127.0.0.1',#本机可不改
	    }
	}
	数据库需要自己创建，django只会生成表。
	建好数据库使用manager命令 makemigrations -> migration来生成数据表
	报错的话需要安装mysqlclient，最好下载到本地安装，地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
	页面上面的cp36代表Python3.6的版本，cp37代表Python3.7 的版本！
	然后在虚拟环境安装：pip install mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl（随着更新可能会不一样版本）
	
	**运行django工程时可能会发生的错误**
	#链接mysql数据库时报错，django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named MySQLdb
	#如果pip安装后还是提示这个错误，一定要先注意看安装MySQLdb用的是否是venv的python pip 不要用环境变量中的pip那样不会装到venv中，这个问题坑了我半个多小时。
	#win7下有可能会需要这两个dll拷贝到system32中：libguide40.dll、libmmd.dll
	#提供一个驱动下载的地址以防网络不好或者提示没有对应版本，注意python27 32位选win32的64选amd64的
	#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
	
	

## 静态文件的处理 ##
	
	在settings中debug为true的情况下：
		例如引用static文件夹中的style.css文件页面上直接写入/static/css/style.css是无效的，需要在settings文件中增加一个列表
		STATICFILES_DIRS = [
		    os.path.join(BASE_DIR, 'static')
		]
		重启django这样就可以访问静态文件了。
	在settings.py中如果写了中文注释，python3没问题，python27需要再第一行加上#coding:utf-8	


# 三、留言板app #
	创建app liuyan拷贝到apps文件夹中并生成数据库表makemigrations， migrate。
	拷贝start.html文件，设置路由
	