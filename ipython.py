'''
python 系统教程8文本处理
2017.2.2017
author：perl2py
'''
#ipython
Ustr1= u’this is a unicode string’
Ustr2=u’这也是一个字符串’
print ustr2.encode('raw-unicode-escape')
ustr3=unicode('this is a unicode string')
import re 
re_string="{{(.*？)}}"#.匹配任意字符*匹配0次或多次？匹配0次或一次
some_string="this is string with {{word}} embedded {{surly brackets}} to show an {{example}} of {{regular expressions}}"
for match in re.findall(re_string,some_string):#效率低
	print "MATCH->",match
re_obj=re.compile("{{(.*?)}}")
for match in re_obj.findall(some_string):#效率高（适合大文件匹配）
	print "Match->",match
	
#!/usr/bin/env python
#re_loop_nocompile re_loop_compile
import re

def run_re():
	pattren='def'
	re_obj=re.compile(pattern)#add
	infile=open('chatserver.py',r)
	match_count=0
	lines=0
	for line in infile:
	#match=re.search(pattern,line)
	match=re_obj.search(line)#changed
	if match:
		match_count+=1
	lines+=1
	return (lines,match)
	
if __name__=="__main__"
	lines,match_count=run_re()
	print 'Lines:',lines
	print 'Match:',match

#ipython	
import re_loop_nocompile
timeit -n 5 re_loop_nocompile.run_re()
import re_loop_compile
timeit -n 5 re_loop_compile.run_re()

#linux shell
time python re_loop_nocompile.py

#ipython
raw_pattern=r'\b[a-z]+\b' #[a-z]a到z的任意组合 +至少一次以上
some_string='a few little words Application'
re.findall(raw_pattern,some_string)
re_obj=re.compile(r'\bt.*?e\b')#t开头e结尾.匹配任意字符*匹配0次或多次？匹配0次或一次
re_obj.findall("time tame tune tint tire")
re_obj=re.compile(r'\bt\w*?e\b')#\w匹配任意字母数字
re_obj.findall("time tame tune tint tire")
re_obj=re.compile(r"""(A\W\b(big|small)\b\W+\b(brown|purple)\b\W+\b(dog|cow)\b\W+\b(ran|jumped)\b\W+\b(the)\b\W+\b(street|moon).*?\.)""",re.VEROSE) #\W 匹配与\w相反
re_obj.findall('A big brown dog ran down the moon.A small purple cow jumped to the street')#findall
re_iter=re_obj.finditer('A big brown dog ran down the moon.A small purple cow jumped to the street')#finditer
re_iter
for item in re_iter:
	print item
	print item.group()
re_obj=re.compile('Foo')
search_string=' Foo'
re_obj.search(search_string)
re_obj.search(search_string).groups()#移动自动匹配
re_obj.match(search_string,pos=1)#从头开始
re_obj.match(search_string,pos=1,endpos=3)#结束位置不包含的要给4
re_obj.search(search_string,pos=1,endpos=4)#也可以指定匹配
re_obj.search(search_string).start()
re_obj.search(search_string).end()
re_obj.search(search_string).group()
re_obj.search(search_string).dict()
'''
python 系统教程8文本处理标准输入输出
2017.2.21
author：perl2py
'''
#ipython
import sys
!ls
f=open('pytemp.txt')
f
sys.stdin
sys.stdin.seek()

#gedit
#sys_stdin_readline.py
#!/usr/bin/env python
import sys 

counter= 1
while True:
	line=sys.stdin.readline()
	if not line:
		break
	print "%s:%s"(counter,line)
	counter+=1
#linux
who
chmod +x sys_stdin_readline.py
who | ./sys_stdin_readline.py

#getit
#sys_stdin_readline2
import sys
for i,line in enumerate(sys.stdin):
	print "%s:%s"%(i,line)
#linux
chmode +x sys_stdin_readline2.py
who | ./sys_stdin_readline2.py
f=open("foo.txt",w)
f
sys.stout
type(sys.stout)
type(sys.stout)==type(f)
fr=open('pytemp.txt','r')
fr
type(f)==type(fr)
from StringIO import StringIO
file_like_string=StringIO("This is a\nmutiline string.\nreadline() should see\nmutiline lines\ninput")
file_like_string.readline()
dir(file_like_string)
f
fr
from sets import Set
sio_set=Set(dir(file_like_string))
file_sset=Set(dir(fr))
sio_set.difference(file_set)
file_set.sifference(sio_set)
#Firefox
http://www.perl2py.cn:8000/index
import urllib
url_file=urllib.urlopen("http://www.perl2py.cn:8000/index")
url_docs=url_file.read()
len(url_docs)
url_file.close()
print url_docs
'''
python 系统教程10日志解析
2017.2.21
author：perl2py
'''
#getit
#ssh_log_parser.py
#!/usr/bin/env python
"""
apache_log
"""
import sys

def dictify_logline(line):
	split_line=line.split()
	return {'remote_host':split_line[0],'sttus'split_line[8],'bytes_sent':split_line[9]}
	
def gennerate_log_report(logfile):
	report_dict={}
	for line in logfile:
		line_dict_dictify_logline(line)
		print line_dict
		try:
			bytes_sent=int(line_dict['bytes_sent'])
		except ValueError:
			continue
		report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)
	return report_dict
if __name__=='__main__'
	if not len(sys.argv)>1:
		print __doc__
		sys.exit(1)
	infile_name=sys.argv[1]
	try:
		infile=open(infile_name,'r')
	except IOError:
		print "you must specify avalid file to parse"
		print __doc__
		sys.exit(1)
	log_report=generate_log_report(infile)
	print log_report
	infile.close()

#getit
#test_apache_log_parser_split.py 单元测试
#!/usr/bin/env python

import unittest
import ssh_log_parser
class TestApacheLogParser(unittest.TestCase):
		def setUp(self):
			pass
		def testCombinedExaple(self):
			compile_log_entry='hfjkdshajfhdkjsahfdh'#日志一组内容
			self.assertEqual(ssh_log_parser.dictify_logline(compile_log_entry),{'remote_host':fjds,'sttus':fds,'bytes_sent':fds})
			#断言测试
if __name__=='__main__'
	unittest.main()	
	
#linux
python test_apache_log_parser_split.py
# .表示断言通过 F表示断言失败
#getit
apache_log_parser_reser_regex.py #正则表达式
#!/usr/bin/env python
import sys
import re
log_line_re=re.compile(r'''(?P<remote_host>\S+)
							\s+ #whilespace
							\S+ #remote logname
							\s+ #whilespace
							\S+ #remote user
							\s+ #whilespace
							\[[^\[\]+\]] #time
							\s+ #whilespace
							(?P<status>\d+)
							\s+ #whilespace
							(?P<bytes_sent>-|\d+)
							\s* #whilespace
						''',re.VERBOSE)
						
def dictify_logline(line):
	m=log_line_re.match(line)
	if m:
		groupdict=m.groupdict()
		if groupdict['bytes_sent']=='-':
			groupdict['bytes_sent']='0'
		return groupdict
	else:
		return {'remote_host':None,'status':None,'bytes_sent':0,}
def generate_log_report(logfile):
	report_dict={}
	for line in logfile:
		line_dict=dictify_logline(line)
		print line_dict
		try:
			bytes_sent=int(line_dict['bytes_sent'])
		except ValueError:
			continue
		report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)
	return report_dict
if __name__=='__main__'
	if not len(sys.argv)>1:
		print __doc__
		sys.exit(1)
	infile_name=sys.argv[1]
	try:
		infile=open(infile_name,'r')
	except IOError:
		print "you must specify avalid file to parse"
		print __doc__
		sys.exit(1)
	log_report=generate_log_report(infile)
	print log_report
	infile.close()
'''
python 系统教程11文本处理element_tree
2017.2.25
author：perl2py
'''	
#getit
#tomcat-users.xml
<?xml version="1.0"	encoding="UTF-8"?>
<tomcat-users>
	<user name="tomcat" password="tomcat" roles="tomcat"/>
	<user name="role1" password="tomcat" roles="role1"/>
	<user name="both" password="tomcat" roles="tomcat,role1"/>
</tomcat-users>
	
