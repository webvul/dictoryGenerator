#一个简单的社工字典生成程序，基于python实现

###  各种数据生成策略及参数设置方式

##### 生日 （不可为空）
	（格式为YYYY-MM-DD）（不可为空）
	输入证件上生日数据
	生成生日数据的任意组合，加入birthday list

#####	公历生日（自动生成）
	然后，会根据日期计算公历日期
	同样的，会生成公历日期数据的任意组合，并加入birsthday list
	未来，公历日期会配置成一个模块，可根据选择载入或不载入
	
#####	姓名 （可为空）
	姓名分为名（First Name）和姓（Last Name），格式为每个字中间带空格
	生成名和姓的任意组合，并加入name list
	
#####	英文名 （可为空）
	生成策略与姓名一样
	
#####	昵称 （可为空）
	生成策略与姓名一样
	
#####	手机号（暂时不可为空）（暂时格式为11位手机号码）
	根据生成策略生成手机号码的任意组合，并加入phoneNumer list
	
#####	QQ号（暂时不可为空）（暂时格式为全数字）
	根据生成策略生成QQ号的任意组合，并加入QQ list
	
#####	邮箱账号（可为空）
	邮箱账号的格式分为两种，带域名和不带域名，会根据@符号判断，如果带域名，会先去掉域名
	根据生成策略生成邮箱账号的任意组合，并加入email list
	
#####	其他信息（可为空）
	其他任意信息，目前将其他信息全部视为字符串，根据字符串的生成策略生成
	未来，会判断信息是数字还是字符串，根据不同的生成策略进行运算
	
#####	所有待生成list都定义在variables文件中
	variables还有一些通用数据
	dict_max-组合到任意位置的简单字符串
	tail-组合到结尾的简单字符串
	head-组合到开头的简单字符串
	year-组合到任意位置的年份字符串
	lett-组合到任意位置的字母
	可根据不同情况自行配置

###	setup.py是py2exe的配置文件
	安装py2exe后会编译成exe文件，在windows下运行

###	const是保存常量的文件
	const文件中包括isDebug和isRelease
	只有当isRelease为True时才会生成result文件，否则，只会打印在控制台
	isDebug控制log的输出	

###	程序运行后后在当前文件夹生成result.txt文件
