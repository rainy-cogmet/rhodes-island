
content = open('dashboard/dashboard.html', 'r', encoding='utf-8').read()

# 替换标题
content = content.replace('军机处 · 三省六部总控台', '罗德岛控制中心')
content = content.replace('皇上视角 · 实时旨意追踪', '博士视角 · 实时任务追踪')

# 替换角色
content = content.replace('皇上', '博士')
content = content.replace('太子', '阿米娅')
content = content.replace('中书省', '特蕾西娅')
content = content.replace('门下省', '凯尔希')
content = content.replace('尚书省', 'Mon3tr')
content = content.replace('礼部', '赫墨')
content = content.replace('户部', '可露希尔')
content = content.replace('兵部', '逻各斯')
content = content.replace('刑部', '塞雷娅')
content = content.replace('工部', '德克萨斯')
content = content.replace('吏部', '华法林')
content = content.replace('钦天监', '能天使')

# 替换任务ID前缀
content = content.replace('JJC-', 'RHI-')

# 替换 Tab 标签
content = content.replace('旨意看板', '任务看板')
content = content.replace('省部调度', '罗德岛调度')
content = content.replace('官员总览', '干员总览')
content = content.replace('奏折阁', '报告阁')
content = content.replace('旨库', '任务库')
content = content.replace('天下要闻', '罗德岛通讯')

# 替换其他关键词
content = content.replace('旨意', '任务')
content = content.replace('下旨', '发布任务')
content = content.replace('回奏', '回复')
content = content.replace('御批', '批准')
content = content.replace('准奏', '批准')
content = content.replace('封驳', '驳回')
content = content.replace('早朝', '晨会')
content = content.replace('各部听旨', '各干员就位')

# 写入新文件
open('dashboard/dashboard.html', 'w', encoding='utf-8').write(content)
print('替换完成！')
