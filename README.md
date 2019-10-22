# pytest_ui
基于Pytest+Selenium+Allure的UI自动化开源框架

----
#### 模块类的设计
`data.py` 存放测试用例数据

`config.py`读取配置文件，包括：不同环境的配置，email相关配置

`locators.py`selenium定位文件

`module`页面封装

`case_log.py` 封装记录log方法，分为：debug、info、warning、error、critical

`send_email.py`封装smtplib方法，运行结果发送邮件通知

`db.py`连接数据库

`read_excel.py`读取excel数据

`logs` 日志文件

`cese` 测试用例

----

