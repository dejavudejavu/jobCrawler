# 导入Flask类
from flask import Flask,make_response,send_file, send_from_directory
from flask import render_template,request,jsonify,redirect

from crawler import crawler

# 实例化，可视为固定格式
app = Flask(__name__)

# route()方法用于设定路由；类似spring路由配置
@app.route('/')
def hello():
    return render_template('/web/html/index.html')

@app.route('/ajaxtest')
def hello_world():
    key = request.values.get("key")
    city = request.values.get("city")
    min = request.values.get("min")
    max = request.values.get("max")
    field = request.values.get("field")
    Liepin=crawler(2,key,city,min,max,field)
    Liepin.start()
    #以下是测试用
    # Liepin=crawler(40,key,city,min,max,field)
#     Liepin.countList=[ 
# {'职责': 1, '描述': 1, '参与': 1, '平台': 2, '核心': 1, '机器': 2, '学习': 3, '算法': 5, '设计': 2, '开发': 1, '成果': 1, '业务': 3, '打造': 1, '智能化': 1, '金融': 1, '场景': 2, '建设': 1, '抽象': 1, '建模': 1, '持续': 1, '优化': 1, '构建': 1, '维护': 1, '智能': 2, '系统': 1, '企业': 1, '画像': 2, '推荐': 1, '用户': 1, '搜索引擎': 1, '任职': 1, '熟练掌握': 1, 'C++': 1, 'java': 1, 'python': 1, '一种': 1, '几种': 1, '编程语言': 1, '熟练': 1, '数据结构': 1, '常用': 2, '能力': 2, '熟悉': 1, '自然语言': 1, '深度': 1, '实践': 1, '技术': 2, '攻关': 1, '跟进': 1, '领域': 1, '最新': 1, '研究成果': 1, '快速': 1, '实验': 1, '调优': 1},
# {'岗位职责': 1, key: 8, '项目': 1, '客户': 2, '情况': 1, '提炼': 2, '需求': 1, '梳理': 1, '整合': 1, '数据': 3, '资源': 1, '创新': 1, '数据挖掘': 5, '能力': 2, 'SaaS': 1, '产品': 2, '解决': 2, '价值': 2, '胜任': 1, '硕士': 1, '统计': 1, '数学': 1, '计算机': 1, '相关': 4, '专业': 1, '工作': 2, '经验': 4, '熟练掌握': 1, 'SQL': 1, '熟悉': 2, '常用': 1, '数据库': 1, 'Hadoop': 1, '生态': 2, 'ODPS': 1, '优先': 5, '编程语言': 1, 'Java': 1, 'Python': 1, '精通': 1, '工具': 1, '算法': 2, '自然语言': 1, '或图': 1, '敏感度': 1, '特定': 1, '场景': 1, '基础': 1, '信息': 1, '特征': 1, '主动': 1, '挖掘': 1, '擅长': 1, '经理': 1, '运营': 1, '人员': 1, '沟通': 1, '团队': 2, '协调': 1, '互联网': 1, '各类': 1, '风控': 1, '模型': 1, '互联网安全': 1, '公共安全': 1, '管理': 1}
#                     ]
#     Liepin.genaImage()
    return 'ok'

@app.route('/showImage')
def showImage():
    return render_template('/web/html/showImage.html')



    


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="127.0.0.1", port=8080)


