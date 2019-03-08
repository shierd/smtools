OSS小工具
=========
主要为了解决需要上传网站静态资源目录到oss。
还是因为太懒了~~~

Env
----
pip install oss2

Usage
------
1. 编辑 upload.py 填上 accessKeyId, accessKeySecret, bucket, endpoint 四个配置项
2. python upload.py -p <需要上传的目录>

Notice
-------
如: python upload.py -p E:\py\smtools\osstool
在oss上保存为 osstool/*

ChangeLog
----------
version 0.0.2 支持单文件上传 -f
version 0.0.1 暂仅支持上传目录