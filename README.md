# GPA_Calculator
## 计算高校的GPA
目前支持的学校：
西电 安徽大学

## 打包成exe
pip install pyinstaller<br>
pyinstaller -F GPA_Calculator.py<br>
生成的exe在 dist文件夹内部<br>

## 备注
南开的优秀、良好等都对应了好几等百分制成绩和绩点，这里都取最高的；通过和不通过没有给绩点只给了百分制范围，这里分别按照80和0计算；<br>
