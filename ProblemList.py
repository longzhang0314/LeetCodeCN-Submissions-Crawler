# -*- coding: utf-8 -*-
def GetProblemId (string):
    mapping = {'两数之和': '1', '两数相加': '2', '无重复字符的最长子串': '3', '寻找两个正序数组的中位数': '4', '最长回文子串': '5', 'Z字形变换': '6', '整数反转': '7', '字符串转换整数(atoi)': '8', '回文数': '9', '正则表达式匹配': '剑指Offer19', '盛最多水的容器': '11', '整数转罗马数字': '12', '罗马数字转整数': '13', '最长公共前缀': '14', '三数之和': '15', '最接近的三数之和': '16', '电话号码的字母组合': '17', '四数之和': '18', '删除链表的倒数第N个节点': '19', '有效的括号': '20', '合并两个有序链表': '21', '括号生成': '22', '合并K个排序链表': '23', '两两交换链表中的节点': '24', 'K个一组翻转链表': '25', '删除排序数组中的重复项': '26', '移除元素': '27', '实现strStr()': '28', '两数相除': '29', '串联所有单词的子串': '30', '下一个排列': '31', '最长有效括号': '32', '搜索旋转排序数组': '33', '在排序数组中查找元素的第一个和最后一个位置': '34', '搜索插入位置': '35', '有效的数独': '36', '解数独': '37', '外观数列': '38', '组合总和': '39', '组合总和II': '40', '缺失的第一个正数': '41', '接雨水': '42', '字符串相乘': '43', '通配符匹配': '44', '跳跃游戏II': '45', '全排列': '46', '全排列II': '47', '旋转图像': '48', '字母异位词分组': '49', 'Pow(x,n)': '50', 'N皇后': '51', 'N皇后II': '52', '最大子序和': '53', '螺旋矩阵': '54', '跳跃游戏': '55', '合并区间': '56', '插入区间': '57', '最后一个单词的长度': '58', '螺旋矩阵II': '59', '第k个排列': '60', '旋转链表': '61', '不同路径': '62', '不同路径II': '63', '最小路径和': '64', '有效数字': '65', '加一': '66', '二进制求和': '67', '文本左右对齐': '68', 'x的平方根': '69', '爬楼梯': '70', '简化路径': '71', '编辑距离': '72', '矩阵置零': '73', '搜索二维矩阵': '74', '颜色分类': '75', '最小覆盖子串': '76', '组合': '77', '子集': '78', '单词搜索': '79', '删除排序数组中的重复项II': '80', '搜索旋转排序数组II': '81', '删除排序链表中的重复元素II': '82', '删除排序链表中的重复元素': '83', '柱状图中最大的矩形': '84', '最大矩形': '85', '分隔链表': '725', '扰乱字符串': '87', '合并两个有序数组': '88', '格雷编码': '89', '子集II': '90', '解码方法': '91', '反转链表II': '92', '复原IP地址': '93', '二叉树的中序遍历': '94', '不同的二叉搜索树II': '95', '不同的二叉搜索树': '96', '交错字符串': '97', '验证二叉搜索树': '98', '恢复二叉搜索树': '99', '相同的树': '100', '对称二叉树': '101', '二叉树的层序遍历': '102', '二叉树的锯齿形层次遍历': '103', '二叉树的最大深度': '104', '从前序与中序遍历序列构造二叉树': '105', '从中序与后序遍历序列构造二叉树': '106', '二叉树的层次遍历II': '107', '将有序数组转换为二叉搜索树': '108', '有序链表转换二叉搜索树': '109', '平衡二叉树': '剑指Offer55-II', '二叉树的最小深度': '111', '路径总和': '112', '路径总和II': '113', '二叉树展开为链表': '114', '不同的子序列': '115', '填充每个节点的下一个右侧节点指针': '116', '填充每个节点的下一个右侧节点指针II': '117', '杨辉三角': '118', '杨辉三角II': '119', '三角形最小路径和': '120', '买卖股票的最佳时机': '121', '买卖股票的最佳时机II': '122', '买卖股票的最佳时机III': '123', '二叉树中的最大路径和': '124', '验证回文串': '125', '单词接龙II': '126', '单词接龙': '127', '最长连续序列': '128', '求根到叶子节点数字之和': '129', '被围绕的区域': '130', '分割回文串': '131', '分割回文串II': '132', '克隆图': '133', '加油站': '134', '分发糖果': '135', '只出现一次的数字': '136', '只出现一次的数字II': '137', '复制带随机指针的链表': '138', '单词拆分': '139', '单词拆分II': '140', '环形链表': '141', '环形链表II': '142', '重排链表': '143', '二叉树的前序遍历': '144', '二叉树的后序遍历': '145', 'LRU缓存机制': '146', '对链表进行插入排序': '147', '排序链表': '148', '直线上最多的点数': '149', '逆波兰表达式求值': '150', '翻转字符串里的单词': '151', '乘积最大子数组': '152', '寻找旋转排序数组中的最小值': '153', '寻找旋转排序数组中的最小值II': '154', '最小栈': '155', '上下翻转二叉树': '156', '用Read4读取N个字符': '157', '用Read4读取N个字符II': '158', '至多包含两个不同字符的最长子串': '159', '相交链表': '160', '相隔为1的编辑距离': '161', '寻找峰值': '162', '缺失的区间': '163', '最大间距': '164', '比较版本号': '165', '分数到小数': '166', '两数之和II-输入有序数组': '167', 'Excel表列名称': '168', '多数元素': '169', '两数之和III-数据结构设计': '170', 'Excel表列序号': '171', '阶乘后的零': '172', '二叉搜索树迭代器': '173', '地下城游戏': '174', '组合两个表': '175', '第二高的薪水': '176', '第N高的薪水': '177', '分数排名': '178', '最大数': '179', '连续出现的数字': '180', '超过经理收入的员工': '181', '查找重复的电子邮箱': '182', '从不订购的客户': '183', '部门工资最高的员工': '184', '部门工资前三高的所有员工': '185', '翻转字符串里的单词II': '186', '重复的DNA序列': '187', '买卖股票的最佳时机IV': '188', '旋转数组': '189', '颠倒二进制位': '190', '位1的个数': '191', '统计词频': '192', '有效电话号码': '193', '转置文件': '194', '第十行': '195', '删除重复的电子邮箱': '196', '上升的温度': '197', '打家劫舍': '198', '二叉树的右视图': '199', '岛屿数量': '200', '数字范围按位与': '201', '快乐数': '202', '移除链表元素': '203', '计数质数': '204', '同构字符串': '205', '反转链表': '剑指Offer24', '课程表': '207', '实现Trie(前缀树)': '208', '长度最小的子数组': '209', '课程表II': '210', '添加与搜索单词-数据结构设计': '211', '单词搜索II': '212', '打家劫舍II': '213', '最短回文串': '214', '数组中的第K个最大元素': '215', '组合总和III': '216', '存在重复元素': '217', '天际线问题': '218', '存在重复元素II': '219', '存在重复元素III': '220', '最大正方形': '221', '完全二叉树的节点个数': '222', '矩形面积': '1459', '基本计算器': '224', '用队列实现栈': '225', '翻转二叉树': '226', '基本计算器II': '227', '汇总区间': '228', '求众数II': '229', '二叉搜索树中第K小的元素': '230', '2的幂': '231', '用栈实现队列': '232', '数字1的个数': '233', '回文链表': '面试题02.06', '二叉搜索树的最近公共祖先': '剑指Offer68-I', '二叉树的最近公共祖先': '剑指Offer68-II', '删除链表中的节点': '237', '除自身以外数组的乘积': '238', '滑动窗口最大值': '239', '搜索二维矩阵II': '240', '为运算表达式设计优先级': '241', '有效的字母异位词': '242', '最短单词距离': '243', '最短单词距离II': '244', '最短单词距离III': '245', '中心对称数': '246', '中心对称数II': '247', '中心对称数III': '248', '移位字符串分组': '249', '统计同值子树': '250', '展开二维向量': '251', '会议室': '252', '会议室II': '253', '因子的组合': '254', '验证前序遍历序列二叉搜索树': '255', '粉刷房子': '256', '二叉树的所有路径': '257', '各位相加': '258', '较小的三数之和': '259', '只出现一次的数字III': '260', '以图判树': '261', '行程和用户': '262', '丑数': '剑指Offer49', '丑数II': '264', '粉刷房子II': '265', '回文排列': '面试题01.04', '回文排列II': '267', '缺失数字': '268', '火星词典': '269', '最接近的二叉搜索树值': '270', '字符串的编码与解码': '271', '最接近的二叉搜索树值II': '272', '整数转换英文表示': '273', 'H指数': '274', 'H指数II': '275', '栅栏涂色': '276', '搜寻名人': '277', '第一个错误的版本': '278', '完全平方数': '279', '摆动排序': '280', '锯齿迭代器': '281', '给表达式添加运算符': '282', '移动零': '283', '顶端迭代器': '284', '二叉搜索树中的顺序后继': '285', '墙与门': '286', '寻找重复数': '287', '单词的唯一缩写': '288', '生命游戏': '289', '单词规律': '290', '单词规律II': '291', 'Nim游戏': '292', '翻转游戏': '293', '翻转游戏II': '294', '数据流的中位数': '295', '最佳的碰头地点': '296', '二叉树的序列化与反序列化': '297', '二叉树最长连续序列': '298', '猜数字游戏': '299', '最长上升子序列': '300', '删除无效的括号': '301', '包含全部黑色像素的最小矩形': '302', '区域和检索-数组不可变': '303', '二维区域和检索-矩阵不可变': '304', '岛屿数量II': '305', '累加数': '306', '区域和检索-数组可修改': '307', '二维区域和检索-可变': '308', '最佳买卖股票时机含冷冻期': '309', '最小高度树': '面试题04.02', '稀疏矩阵的乘法': '311', '戳气球': '312', '超级丑数': '313', '二叉树的垂直遍历': '314', '计算右侧小于当前元素的个数': '315', '去除重复字母': '316', '离建筑物最近的距离': '317', '最大单词长度乘积': '318', '灯泡开关': '319', '列举单词的全部缩写': '320', '拼接最大数': '321', '零钱兑换': '322', '无向图中连通分量的数目': '323', '摆动排序II': '324', '和等于k的最长子数组长度': '325', '3的幂': '326', '区间和的个数': '327', '奇偶链表': '328', '矩阵中的最长递增路径': '329', '按要求补齐数组': '330', '验证二叉树的前序序列化': '331', '重新安排行程': '332', '最大BST子树': '333', '递增的三元子序列': '334', '路径交叉': '335', '回文对': '336', '打家劫舍III': '337', '比特位计数': '338', '嵌套列表权重和': '339', '至多包含K个不同字符的最长子串': '340', '扁平化嵌套列表迭代器': '341', '4的幂': '342', '整数拆分': '343', '反转字符串': '344', '反转字符串中的元音字母': '345', '数据流中的移动平均值': '346', '前K个高频元素': '347', '判定井字棋胜负': '348', '两个数组的交集': '349', '两个数组的交集II': '350', '安卓系统手势解锁': '351', '将数据流变为多个不相交区间': '352', '贪吃蛇': '353', '俄罗斯套娃信封问题': '354', '设计推特': '355', '直线镜像': '356', '计算各个位数不同的数字个数': '357', 'K距离间隔重排字符串': '358', '日志速率限制器': '359', '有序转化数组': '360', '轰炸敌人': '361', '敲击计数器': '362', '矩形区域不超过K的最大数值和': '363', '加权嵌套序列和II': '364', '水壶问题': '365', '寻找二叉树的叶子节点': '366', '有效的完全平方数': '367', '最大整除子集': '368', '给单链表加一': '369', '区间加法': '370', '两整数之和': '371', '超级次方': '372', '查找和最小的K对数字': '373', '猜数字大小': '374', '猜数字大小II': '375', '摆动序列': '376', '组合总和Ⅳ': '377', '有序矩阵中第K小的元素': '378', '电话目录管理系统': '379', '常数时间插入、删除和获取随机元素': '380', 'O(1)时间插入、删除和获取随机元素-允许重复': '381', '链表随机节点': '382', '赎金信': '383', '打乱数组': '384', '迷你语法分析器': '385', '字典序排数': '386', '字符串中的第一个唯一字符': '387', '文件的最长绝对路径': '388', '找不同': '389', '消除游戏': '390', '完美矩形': '391', '判断子序列': '392', 'UTF-8编码验证': '393', '字符串解码': '394', '至少有K个重复字符的最长子串': '395', '旋转函数': '396', '整数替换': '397', '随机数索引': '398', '除法求值': '399', '第N个数字': '400', '二进制手表': '401', '移掉K位数字': '402', '青蛙过河': '403', '左叶子之和': '404', '数字转换为十六进制数': '405', '根据身高重建队列': '406', '接雨水II': '407', '有效单词缩写': '408', '最长回文串': '409', '分割数组的最大值': '410', '最短特异单词缩写': '411', 'FizzBuzz': '412', '等差数列划分': '413', '第三大的数': '414', '字符串相加': '415', '分割等和子集': '416', '太平洋大西洋水流问题': '417', '屏幕可显示句子的数量': '418', '甲板上的战舰': '419', '强密码检验器': '420', '数组中两个数的最大异或值': '421', '有效的单词方块': '422', '从英文中重建数字': '423', '替换后的最长重复字符': '424', '单词方块': '425', '将二叉搜索树转化为排序的双向链表': '426', '建立四叉树': '427', '序列化和反序列化N叉树': '428', 'N叉树的层序遍历': '429', '扁平化多级双向链表': '430', '将N叉树编码为二叉树': '431', '全O(1)的数据结构': '432', '最小基因变化': '433', '字符串中的单词数': '434', '无重叠区间': '435', '寻找右区间': '436', '路径总和III': '437', '找到字符串中所有字母异位词': '438', '三元表达式解析器': '439', '字典序的第K小数字': '440', '排列硬币': '441', '数组中重复的数据': '442', '压缩字符串': '443', '序列重建': '444', '两数相加II': '445', '等差数列划分II-子序列': '446', '回旋镖的数量': '447', '找到所有数组中消失的数字': '448', '序列化和反序列化二叉搜索树': '449', '删除二叉搜索树中的节点': '450', '根据字符出现频率排序': '451', '用最少数量的箭引爆气球': '452', '最小移动次数使数组元素相等': '453', '四数相加II': '454', '分发饼干': '455', '132模式': '456', '环形数组循环': '457', '可怜的小猪': '458', '重复的子字符串': '459', 'LFU缓存': '460', '汉明距离': '461', '最少移动次数使数组元素相等II': '462', '岛屿的周长': '463', '我能赢吗': '464', '最优账单平衡': '465', '统计重复个数': '466', '环绕字符串中唯一的子字符串': '467', '验证IP地址': '468', '凸多边形': '469', '用Rand7()实现Rand10()': '470', '编码最短长度的字符串': '471', '连接词': '472', '火柴拼正方形': '473', '一和零': '474', '供暖器': '475', '数字的补数': '476', '汉明距离总和': '477', '在圆内随机生成点': '478', '最大回文数乘积': '479', '滑动窗口中位数': '480', '神奇字符串': '481', '密钥格式化': '482', '最小好进制': '483', '寻找排列': '484', '最大连续1的个数': '485', '预测赢家': '486', '最大连续1的个数II': '487', '祖玛游戏': '488', '扫地机器人': '489', '迷宫': '490', '递增子序列': '491', '构造矩形': '492', '翻转对': '493', '目标和': '494', '提莫攻击': '495', '下一个更大元素I': '496', '非重叠矩形中的随机点': '497', '对角线遍历': '498', '迷宫III': '499', '键盘行': '500', '二叉搜索树中的众数': '501', 'IPO': '502', '下一个更大元素II': '503', '七进制数': '504', '迷宫II': '505', '相对名次': '506', '完美数': '507', '出现次数最多的子树元素和': '508', '斐波那契数': '509', '二叉搜索树中的中序后继II': '510', '游戏玩法分析I': '511', '游戏玩法分析II': '512', '找树左下角的值': '513', '自由之路': '514', '在每个树行中找最大值': '515', '最长回文子序列': '516', '超级洗衣机': '517', '零钱兑换II': '518', '随机翻转矩阵': '519', '检测大写字母': '520', '最长特殊序列Ⅰ': '521', '最长特殊序列II': '522', '连续的子数组和': '523', '通过删除字母匹配到字典里最长单词': '524', '连续数组': '525', '优美的排列': '526', '单词缩写': '527', '按权重随机选择': '528', '扫雷游戏': '529', '二叉搜索树的最小绝对差': '530', '孤独像素I': '531', '数组中的K-diff数对': '532', '孤独像素II': '533', '游戏玩法分析III': '534', 'TinyURL的加密与解密': '535', '从字符串生成二叉树': '536', '复数乘法': '537', '把二叉搜索树转换为累加树': '538', '最小时间差': '539', '有序数组中的单一元素': '540', '反转字符串II': '541', '01矩阵': '542', '二叉树的直径': '543', '输出比赛匹配对': '544', '二叉树的边界': '545', '移除盒子': '546', '朋友圈': '547', '将数组分割成和相等的子数组': '548', '二叉树中最长的连续序列': '549', '游戏玩法分析IV': '550', '学生出勤记录I': '551', '学生出勤记录II': '552', '最优除法': '553', '砖墙': '554', '分割连接字符串': '555', '下一个更大元素III': '556', '反转字符串中的单词III': '557', '四叉树交集': '558', 'N叉树的最大深度': '559', '和为K的子数组': '560', '数组拆分I': '561', '矩阵中最长的连续1线段': '562', '二叉树的坡度': '563', '寻找最近的回文数': '564', '数组嵌套': '565', '重塑矩阵': '566', '字符串的排列': '剑指Offer38', '最大休假天数': '568', '员工薪水中位数': '569', '至少有5名直接下属的经理': '570', '给定数字的频率查询中位数': '571', '另一个树的子树': '572', '松鼠模拟': '573', '当选者': '574', '分糖果': '575', '出界的路径数': '576', '员工奖金': '577', '查询回答率最高的问题': '578', '查询员工的累计薪水': '579', '统计各专业学生人数': '580', '最短无序连续子数组': '581', '杀死进程': '582', '两个字符串的删除操作': '583', '寻找用户推荐人': '584', '2016年的投资': '585', '订单最多的客户': '586', '安装栅栏': '587', '设计内存文件系统': '588', 'N叉树的前序遍历': '589', 'N叉树的后序遍历': '590', '标签验证器': '591', '分数加减运算': '592', '有效的正方形': '593', '最长和谐子序列': '594', '大的国家': '595', '超过5名学生的课': '596', '好友申请I：总体通过率': '597', '范围求和II': '598', '两个列表的最小索引总和': '599', '不含连续1的非负整数': '600', '体育馆的人流量': '601', '好友申请II：谁有最多的好友': '602', '连续空余座位': '603', '迭代压缩字符串': '604', '种花问题': '605', '根据二叉树创建字符串': '606', '销售员': '607', '树节点': '608', '在系统中查找重复文件': '609', '判断三角形': '610', '有效三角形的个数': '611', '平面上的最近距离': '612', '直线上的最近距离': '613', '二级关注者': '614', '平均工资：部门与公司比较': '615', '给字符串添加加粗标签': '616', '合并二叉树': '617', '学生地理信息报告': '618', '只出现一次的最大数字': '619', '有趣的电影': '620', '任务调度器': '621', '设计循环队列': '622', '在二叉树中增加一行': '623', '数组列表中的最大距离': '624', '最小因式分解': '625', '换座位': '626', '交换工资': '627', '三个数的最大乘积': '628', 'K个逆序对数组': '629', '课程表III': '630', '设计Excel求和公式': '631', '最小区间': '632', '平方数之和': '633', '寻找数组的错位排列': '634', '设计日志存储系统': '635', '函数的独占时间': '636', '二叉树的层平均值': '637', '大礼包': '638', '解码方法2': '639', '求解方程': '640', '设计循环双端队列': '641', '设计搜索自动补全系统': '642', '子数组最大平均数I': '643', '最大平均子段和II': '644', '错误的集合': '645', '最长数对链': '646', '回文子串': '647', '单词替换': '648', 'Dota2参议院': '649', '只有两个键的键盘': '650', '4键键盘': '651', '寻找重复的子树': '652', '两数之和IV-输入BST': '653', '最大二叉树': '654', '输出二叉树': '655', '金币路径': '656', '机器人能否返回原点': '657', '找到K个最接近的元素': '658', '分割数组为连续子序列': '659', '移除9': '660', '图片平滑器': '661', '二叉树最大宽度': '662', '均匀树划分': '663', '奇怪的打印机': '664', '非递减数列': '665', '路径和IV': '666', '优美的排列II': '667', '乘法表中第k小的数': '668', '修剪二叉搜索树': '669', '最大交换': '670', '二叉树中第二小的节点': '671', '灯泡开关Ⅱ': '672', '最长递增子序列的个数': '673', '最长连续递增序列': '674', '为高尔夫比赛砍树': '675', '实现一个魔法字典': '676', '键值映射': '677', '有效的括号字符串': '678', '24点游戏': '679', '验证回文字符串Ⅱ': '680', '最近时刻': '681', '棒球比赛': '682', 'K个空花盆': '683', '冗余连接': '684', '冗余连接II': '685', '重复叠加字符串匹配': '686', '最长同值路径': '687', '“马”在棋盘上的概率': '688', '三个无重叠子数组的最大和': '689', '员工的重要性': '690', '贴纸拼词': '691', '前K个高频单词': '692', '交替位二进制数': '693', '不同岛屿的数量': '694', '岛屿的最大面积': '695', '计数二进制子串': '696', '数组的度': '697', '划分为k个相等的子集': '698', '掉落的方块': '699', '二叉搜索树中的搜索': '700', '二叉搜索树中的插入操作': '701', '搜索长度未知的有序数组': '702', '数据流中的第K大元素': '703', '二分查找': '704', '设计哈希集合': '705', '设计哈希映射': '706', '设计链表': '707', '循环有序列表的插入': '708', '转换成小写字母': '709', '黑名单中的随机数': '710', '不同岛屿的数量II': '711', '两个字符串的最小ASCII删除和': '712', '乘积小于K的子数组': '713', '买卖股票的最佳时机含手续费': '714', 'Range模块': '715', '最大栈': '716', '1比特与2比特字符': '717', '最长重复子数组': '718', '找出第k小的距离对': '719', '词典中最长的单词': '720', '账户合并': '721', '删除注释': '722', '粉碎糖果': '723', '寻找数组的中心索引': '724', '原子的数量': '726', '最小窗口子序列': '727', '自除数': '728', '我的日程安排表I': '729', '统计不同回文子序列': '730', '我的日程安排表II': '731', '我的日程安排表III': '732', '图像渲染': '733', '句子相似性': '734', '行星碰撞': '735', 'Lisp语法解析': '736', '句子相似性II': '737', '单调递增的数字': '738', '每日温度': '739', '删除与获得点数': '740', '摘樱桃': '741', '二叉树最近的叶节点': '742', '网络延迟时间': '743', '寻找比目标字母大的最小字母': '744', '前缀和后缀搜索': '745', '使用最小花费爬楼梯': '746', '至少是其他数字两倍的最大数': '747', '最短完整词': '748', '隔离病毒': '749', '角矩形的数量': '750', 'IP到CIDR': '751', '打开转盘锁': '752', '破解保险箱': '753', '到达终点数字': '754', '倒水': '755', '金字塔转换矩阵': '756', '设置交集大小至少为2': '757', '字符串中的加粗单词': '758', '员工空闲时间': '759', '找出变位映射': '760', '特殊的二进制序列': '761', '二进制表示中质数个计算置位': '762', '划分字母区间': '763', '最大加号标志': '764', '情侣牵手': '765', '托普利茨矩阵': '766', '重构字符串': '767', '最多能完成排序的块II': '768', '最多能完成排序的块': '769', '基本计算器IV': '770', '宝石与石头': '771', '基本计算器III': '772', '滑动谜题': '773', '最小化去加油站的最大距离': '774', '全局倒置与局部倒置': '775', '拆分二叉搜索树': '776', '在LR字符串中交换相邻字符': '777', '水位上升的泳池中游泳': '778', '第K个语法符号': '779', '到达终点': '780', '森林中的兔子': '781', '变为棋盘': '782', '二叉搜索树节点最小距离': '783', '字母大小写全排列': '784', '判断二分图': '785', '第K个最小的素数分数': '786', 'K站中转内最便宜的航班': '787', '旋转数字': '788', '逃脱阻碍者': '789', '多米诺和托米诺平铺': '790', '自定义字符串排序': '791', '匹配子序列的单词数': '792', '阶乘函数后K个零': '793', '有效的井字游戏': '794', '区间子数组个数': '795', '旋转字符串': '796', '所有可能的路径': '797', '得分最高的最小轮调': '798', '香槟塔': '799', '相似RGB颜色': '800', '使序列递增的最小交换次数': '801', '找到最终的安全状态': '802', '打砖块': '803', '唯一摩尔斯密码词': '804', '数组的均值分割': '805', '写字符串需要的行数': '806', '保持城市天际线': '807', '分汤': '808', '情感丰富的文字': '809', '黑板异或游戏': '810', '子域名访问计数': '811', '最大三角形面积': '812', '最大平均值和的分组': '813', '二叉树剪枝': '814', '公交路线': '815', '模糊坐标': '816', '链表组件': '817', '赛车': '818', '最常见的单词': '819', '单词的压缩编码': '820', '字符的最短距离': '821', '翻转卡片游戏': '822', '带因子的二叉树': '823', '山羊拉丁文': '824', '适龄的朋友': '825', '安排工作以达到最大收益': '826', '最大人工岛': '827', '统计子串中的唯一字符': '828', '连续整数求和': '829', '较大分组的位置': '830', '隐藏个人信息': '831', '翻转图像': '832', '字符串中的查找与替换': '833', '树中距离之和': '834', '图像重叠': '835', '矩形重叠': '836', '新21点': '837', '推多米诺': '838', '相似字符串组': '839', '矩阵中的幻方': '840', '钥匙和房间': '841', '将数组拆分成斐波那契序列': '842', '猜猜这个单词': '843', '比较含退格的字符串': '844', '数组中的最长山脉': '845', '一手顺子': '846', '访问所有节点的最短路径': '847', '字母移位': '848', '到最近的人的最大距离': '849', '矩形面积II': '850', '喧闹和富有': '851', '山脉数组的峰顶索引': '852', '车队': '853', '相似度为K的字符串': '854', '考场就座': '855', '括号的分数': '856', '雇佣K名工人的最低成本': '857', '镜面反射': '858', '亲密字符串': '859', '柠檬水找零': '860', '翻转矩阵后的得分': '861', '和至少为K的最短子数组': '862', '二叉树中所有距离为K的结点': '863', '获取所有钥匙的最短路径': '864', '具有所有最深结点的最小子树': '865', '回文素数': '866', '转置矩阵': '867', '二进制间距': '868', '重新排序得到2的幂': '869', '优势洗牌': '870', '最低加油次数': '871', '叶子相似的树': '872', '最长的斐波那契子序列的长度': '873', '模拟行走机器人': '874', '爱吃香蕉的珂珂': '875', '链表的中间结点': '876', '石子游戏': '877', '第N个神奇数字': '878', '盈利计划': '879', '索引处的解码字符串': '880', '救生艇': '881', '细分图中的可到达结点': '882', '三维形体投影面积': '883', '两句话中的不常见单词': '884', '螺旋矩阵III': '885', '可能的二分法': '886', '鸡蛋掉落': '887', '公平的糖果交换': '888', '根据前序和后序遍历构造二叉树': '889', '查找和替换模式': '890', '子序列宽度之和': '891', '三维形体的表面积': '892', '特殊等价字符串组': '893', '所有可能的满二叉树': '894', '最大频率栈': '895', '单调数列': '896', '递增顺序查找树': '897', '子数组按位或操作': '898', '有序队列': '899', 'RLE迭代器': '900', '股票价格跨度': '901', '最大为N的数字组合': '902', 'DI序列的有效排列': '903', '水果成篮': '904', '按奇偶排序数组': '905', '超级回文数': '906', '子数组的最小值之和': '907', '最小差值I': '908', '蛇梯棋': '909', '最小差值II': '910', '在线选举': '911', '排序数组': '912', '猫和老鼠': '913', '卡牌分组': '914', '分割数组': '915', '单词子集': '916', '仅仅反转字母': '917', '环形子数组的最大和': '918', '完全二叉树插入器': '919', '播放列表的数量': '920', '使括号有效的最少添加': '921', '按奇偶排序数组II': '922', '三数之和的多种可能': '923', '尽量减少恶意软件的传播': '924', '长按键入': '925', '将字符串翻转到单调递增': '926', '三等分': '927', '尽量减少恶意软件的传播II': '928', '独特的电子邮件地址': '929', '和相同的二元子数组': '930', '下降路径最小和': '931', '漂亮数组': '932', '最近的请求次数': '933', '最短的桥': '934', '骑士拨号器': '935', '戳印序列': '936', '重新排列日志文件': '937', '二叉搜索树的范围和': '938', '最小面积矩形': '939', '不同的子序列II': '940', '有效的山脉数组': '941', '增减字符串匹配': '942', '最短超级串': '943', '删列造序': '944', '使数组唯一的最小增量': '945', '验证栈序列': '946', '移除最多的同行或同列石头': '947', '令牌放置': '948', '给定数字能组成的最大时间': '949', '按递增顺序显示卡牌': '950', '翻转等价二叉树': '951', '按公因数计算最大组件大小': '952', '验证外星语词典': '953', '二倍数对数组': '954', '删列造序II': '955', '最高的广告牌': '956', 'N天后的牢房': '957', '二叉树的完全性检验': '958', '由斜杠划分区域': '959', '删列造序III': '960', '重复N次的元素': '961', '最大宽度坡': '962', '最小面积矩形II': '963', '表示数字的最少运算符': '964', '单值二叉树': '965', '元音拼写检查器': '966', '连续差相同的数字': '967', '监控二叉树': '968', '煎饼排序': '969', '强整数': '970', '翻转二叉树以匹配先序遍历': '971', '相等的有理数': '972', '最接近原点的K个点': '973', '和可被K整除的子数组': '974', '奇偶跳': '975', '三角形的最大周长': '976', '有序数组的平方': '977', '最长湍流子数组': '978', '在二叉树中分配硬币': '979', '不同路径III': '980', '基于时间的键值存储': '981', '按位与为零的三元组': '982', '最低票价': '983', '不含AAA或BBB的字符串': '984', '查询后的偶数和': '985', '区间列表的交集': '986', '二叉树的垂序遍历': '987', '从叶结点开始的最小字符串': '988', '数组形式的整数加法': '989', '等式方程的可满足性': '990', '坏了的计算器': '991', 'K个不同整数的子数组': '992', '二叉树的堂兄弟节点': '993', '腐烂的橘子': '994', 'K连续位的最小翻转次数': '995', '正方形数组的数目': '996', '找到小镇的法官': '997', '最大二叉树II': '998', '可以被一步捕获的棋子数': '999', '合并石头的最低成本': '1000', '网格照明': '1001', '查找常用字符': '1002', '检查替换后的词是否有效': '1003', '最大连续1的个数III': '1004', 'K次取反后最大化的数组和': '1005', '笨阶乘': '1006', '行相等的最少多米诺旋转': '1007', '先序遍历构造二叉树': '1008', '十进制整数的反码': '1009', '总持续时间可被60整除的歌曲': '1010', '在D天内送达包裹的能力': '1011', '至少有1位重复的数字': '1012', '将数组分成和相等的三个部分': '1013', '最佳观光组合': '1014', '可被K整除的最小整数': '1015', '子串能表示从1到N数字的二进制串': '1016', '负二进制转换': '1017', '可被5整除的二进制前缀': '1018', '链表中的下一个更大节点': '1019', '飞地的数量': '1020', '删除最外层的括号': '1021', '从根到叶的二进制数之和': '1022', '驼峰式匹配': '1023', '视频拼接': '1024', '除数博弈': '1025', '节点与其祖先之间的最大差值': '1026', '最长等差数列': '1027', '从先序遍历还原二叉树': '1028', '两地调度': '1029', '距离顺序排列矩阵单元格': '1030', '两个非重叠子数组的最大和': '1031', '字符流': '1032', '移动石子直到连续': '1033', '边框着色': '1034', '不相交的线': '1035', '逃离大迷宫': '1036', '有效的回旋镖': '1037', '从二叉搜索树到更大和树': '1038', '多边形三角剖分的最低得分': '1039', '移动石子直到连续II': '1040', '困于环中的机器人': '1041', '不邻接植花': '1042', '分隔数组以得到最大和': '1043', '最长重复子串': '1062', '买下所有产品的客户': '1045', '最后一块石头的重量': '1046', '删除字符串中的所有相邻重复项': '1047', '最长字符串链': '1048', '最后一块石头的重量II': '1049', '合作过至少三次的演员和导演': '1050', '高度检查器': '1051', '爱生气的书店老板': '1052', '交换一次的先前排列': '1053', '距离相等的条形码': '1054', '形成字符串的最短路径': '1055', '易混淆数': '1056', '校园自行车分配': '1057', '最小化舍入误差以满足目标': '1058', '从始点到终点的所有路径': '1059', '有序数组中的缺失元素': '1060', '按字典序排列最小的等效字符串': '1061', '有效子数组的数目': '1063', '不动点': '1064', '字符串的索引对': '1065', '校园自行车分配II': '1066', '范围内的数字计数': '1067', '产品销售分析I': '1068', '产品销售分析II': '1069', '产品销售分析III': '1070', '字符串的最大公因子': '1071', '按列翻转得到最大值等行数': '1072', '负二进制数相加': '1073', '元素和为目标值的子矩阵数量': '1074', '项目员工I': '1075', '项目员工II': '1076', '项目员工III': '1077', 'Bigram分词': '1078', '活字印刷': '1079', '根到叶路径上的不足节点': '1080', '不同字符的最小子序列': '1081', '销售分析I': '1082', '销售分析II': '1083', '销售分析III': '1084', '最小元素各数位之和': '1085', '前五科的均分': '1086', '字母切换': '1087', '易混淆数II': '1088', '复写零': '1089', '受标签影响的最大值': '1090', '二进制矩阵中的最短路径': '1091', '最短公共超序列': '1092', '大样本统计': '1093', '拼车': '1094', '山脉数组中查找目标值': '1095', '花括号展开II': '1096', '游戏玩法分析V': '1097', '小众书籍': '1098', '小于K的两数之和': '1099', '长度为K的无重复字符子串': '1100', '彼此熟识的最早时间': '1101', '得分最高的路径': '1102', '分糖果II': '1103', '二叉树寻路': '1104', '填充书架': '1105', '解析布尔表达式': '1106', '每日新用户统计': '1107', 'IP地址无效化': '1108', '航班预订统计': '1109', '删点成林': '1110', '有效括号的嵌套深度': '1111', '每位学生的最高成绩': '1112', '报告的记录': '1113', '按序打印': '1114', '交替打印FooBar': '1115', '打印零与奇偶数': '1116', 'H2O生成': '1117', '一月有多少天': '1118', '删去字符串中的元音': '1119', '子树的最大平均值': '1120', '将数组分成几个递增序列': '1121', '数组的相对排序': '1122', '最深叶节点的最近公共祖先': '1123', '表现良好的最长时间段': '1124', '最小的必要团队': '1125', '查询活跃业务': '1126', '用户购买平台': '1127', '等价多米诺骨牌对的数量': '1128', '颜色交替的最短路径': '1129', '叶值的最小代价生成树': '1130', '绝对值表达式的最大值': '1131', '报告的记录II': '1132', '最大唯一数': '1133', '阿姆斯特朗数': '1134', '最低成本联通所有城市': '1135', '平行课程': '1136', '第N个泰波那契数': '1137', '字母板上的路径': '1138', '最大的以1为边界的正方形': '1139', '石子游戏II': '1140', '查询近30天活跃用户数': '1141', '过去30天的用户活动II': '1142', '最长公共子序列': '1143', '递减元素使数组呈锯齿状': '1144', '二叉树着色游戏': '1145', '快照数组': '1146', '段式回文': '1147', '文章浏览I': '1148', '文章浏览II': '1149', '检查一个数是否在数组中占绝大多数': '1150', '最少交换次数来组合所有的1': '1151', '用户网站访问行为分析': '1152', '字符串转化': '1153', '一年中的第几天': '1154', '掷骰子的N种方法': '1155', '单字符重复子串的最大长度': '1156', '子数组中占绝大多数的元素': '1157', '市场分析I': '1158', '市场分析II': '1159', '拼写单词': '1160', '最大层内元素和': '1161', '地图分析': '1162', '按字典序排在最后的子串': '1163', '指定日期的产品价格': '1164', '单行键盘': '1165', '设计文件系统': '1166', '连接棒材的最低费用': '1167', '水资源分配优化': '1168', '查询无效交易': '1169', '比较字符串最小字母出现频次': '1170', '从链表中删去总和值为零的连续节点': '1171', '餐盘栈': '1172', '即时食物配送I': '1173', '即时食物配送II': '1174', '质数排列': '1175', '健身计划评估': '1176', '构建回文串检测': '1177', '猜字谜': '1178', '重新格式化部门表': '1179', '统计只含单一字母的子串': '1180', '前后拼接': '1181', '与目标颜色间的最短距离': '1182', '矩阵中1的最大数量': '1183', '公交站间的距离': '1184', '一周中的第几天': '1185', '删除一次得到子数组最大和': '1186', '使数组严格递增': '1187', '设计有限阻塞队列': '1188', '“气球”的最大数量': '1189', '反转每对括号间的子串': '1190', 'K次串联后最大子数组之和': '1191', '查找集群内的「关键连接」': '1192', '每月交易I': '1193', '锦标赛优胜者': '1194', '交替打印字符串': '1195', '最多可以买到的苹果数量': '1196', '进击的骑士': '1197', '找出所有行中最小公共元素': '1198', '建造街区的最短时间': '1199', '最小绝对差': '1200', '丑数III': '1201', '交换字符串中的元素': '1202', '项目管理': '1203', '最后一个能进入电梯的人': '1204', '每月交易II': '1205', '设计跳表': '1206', '独一无二的出现次数': '1207', '尽可能使字符串相等': '1208', '删除字符串中的所有相邻重复项II': '1209', '穿过迷宫的最少移动次数': '1210', '查询结果的质量和占比': '1211', '查询球队积分': '1212', '三个有序数组的交集': '1213', '查找两棵二叉搜索树之和': '1214', '步进数': '1215', '验证回文字符串III': '1216', '玩筹码': '1217', '最长定差子序列': '1218', '黄金矿工': '1219', '统计元音字母序列的数目': '1220', '分割平衡字符串': '1221', '可以攻击国王的皇后': '1222', '掷骰子模拟': '1223', '最大相等频率': '1224', '报告系统状态的连续日期': '1225', '哲学家进餐': '1226', '飞机座位分配概率': '1227', '等差数列中缺失的数字': '1228', '安排会议日程': '1229', '抛掷硬币': '1230', '分享巧克力': '1231', '缀点成线': '1232', '删除子文件夹': '1233', '替换子串得到平衡字符串': '1234', '规划兼职工作': '1235', '网络爬虫': '1236', '找出给定方程的正整数解': '1237', '循环码排列': '1238', '串联字符串的最大长度': '1239', '铺瓷砖': '1240', '每个帖子的评论数': '1241', '多线程网页爬虫': '1242', '数组变换': '1243', '力扣排行榜': '1244', '树的直径': '1245', '删除回文子数组': '1246', '交换字符使得字符串相同': '1247', '统计「优美子数组」': '1248', '移除无效的括号': '1249', '检查「好数组」': '1250', '平均售价': '1251', '奇数值单元格的数目': '1252', '重构2行二进制矩阵': '1253', '统计封闭岛屿的数目': '1254', '得分最高的单词集合': '1255', '加密数字': '1256', '最小公共区域': '1257', '近义词句子': '1258', '不相交的握手': '1259', '二维网格迁移': '1260', '在受污染的二叉树中查找元素': '1261', '可被三整除的最大和': '1262', '推箱子': '1263', '页面推荐': '1264', '逆序打印不可变链表': '1265', '访问所有点的最小时间': '1266', '统计参与通信的服务器': '1267', '搜索推荐系统': '1268', '停在原地的方案数': '1269', '向公司CEO汇报工作的所有人': '1270', '十六进制魔术数字': '1271', '删除区间': '1272', '删除树节点': '1273', '矩形内船只的数目': '1274', '找出井字棋的获胜者': '1275', '不浪费原料的汉堡制作方案': '1276', '统计全为1的正方形子矩阵': '1277', '分割回文串III': '1278', '红绿灯路口': '1279', '学生们参加各科测试的次数': '1280', '整数的各位积和之差': '1281', '用户分组': '1282', '使结果不超过阈值的最小除数': '1283', '转化为全零矩阵的最少反转次数': '1284', '找到连续区间的开始和结束数字': '1285', '字母组合迭代器': '1286', '有序数组中出现次数超过25%的元素': '1287', '删除被覆盖区间': '1288', '下降路径最小和II': '1289', '二进制链表转整数': '1290', '顺次数': '1291', '元素和小于等于阈值的正方形的最大边长': '1292', '网格中的最短路径': '1293', '不同国家的天气类型': '1294', '统计位数为偶数的数字': '1295', '划分数组为连续数字的集合': '1296', '子串的最大出现次数': '1297', '你能从盒子里获得的最大糖果数': '1298', '将每个元素替换为右侧最大元素': '1299', '转变数组后最接近目标值的数组和': '1300', '最大得分的路径数目': '1301', '层数最深叶子节点的和': '1302', '求团队人数': '1303', '和为零的N个唯一整数': '1304', '两棵二叉搜索树中的所有元素': '1305', '跳跃游戏III': '1306', '口算难题': '1307', '不同性别每日分数总计': '1308', '解码字母到整数映射': '1309', '子数组异或查询': '1310', '获取你好友已观看的视频': '1311', '让字符串成为回文串的最少插入次数': '1312', '解压缩编码列表': '1313', '矩阵区域和': '1314', '祖父节点值为偶数的节点和': '1315', '不同的循环子字符串': '1316', '将整数转换为两个无零整数的和': '1317', '或运算的最小翻转次数': '1318', '连通网络的操作次数': '1319', '二指输入的的最小距离': '1320', '餐馆营业额变化增长': '1321', '广告效果': '1322', '6和9组成的最大数字': '1323', '竖直打印单词': '1324', '删除给定值的叶子节点': '1325', '灌溉花园的最少水龙头数目': '1326', '列出指定时间段内所有的下单产品': '1327', '破坏回文串': '1328', '将矩阵按对角线排序': '1329', '翻转子数组得到最大的数组值': '1330', '数组序号转换': '1331', '删除回文子序列': '1332', '餐厅过滤器': '1333', '阈值距离内邻居最少的城市': '1334', '工作计划的最低难度': '1335', '每次访问的交易次数': '1336', '方阵中战斗力最弱的K行': '1337', '数组大小减半': '1338', '分裂二叉树的最大乘积': '1339', '跳跃游戏V': '1340', '电影评分': '1341', '将数字变成0的操作次数': '1342', '大小为K且平均值大于等于阈值的子数组数目': '1343', '时钟指针的夹角': '1344', '跳跃游戏IV': '1345', '检查整数及其两倍数是否存在': '1346', '制造字母异位词的最小步骤数': '1347', '推文计数': '1348', '参加考试的最大学生数': '1349', '院系无效的学生': '1350', '统计有序矩阵中的负数': '1351', '最后K个数的乘积': '1352', '最多可以参加的会议数目': '1353', '多次求和构造目标数组': '1354', '活动参与者': '1355', '根据数字二进制下1的数目排序': '1356', '每隔n个顾客打折': '1357', '包含所有三种字符的子字符串数目': '1358', '有效的快递序列数目': '1359', '日期之间隔几天': '1360', '验证二叉树': '1361', '最接近的因数': '1362', '形成三的最大倍数': '1363', '顾客的可信联系人数量': '1364', '有多少小于当前数字的数字': '1365', '通过投票对团队排名': '1366', '二叉树中的列表': '1367', '使网格图至少有一条有效路径的最小代价': '1368', '获取最近第二次的活动': '1369', '上升下降字符串': '1370', '每个元音包含偶数次的最长子字符串': '1371', '二叉树中的最长交错路径': '1372', '二叉搜索子树的最大键值和': '1373', '生成每种字符都是奇数个的字符串': '1374', '灯泡开关III': '1375', '通知所有员工所需的时间': '1376', 'T秒后青蛙的位置': '1377', '使用唯一标识码替换员工ID': '1378', '找出克隆二叉树中的相同节点': '1379', '矩阵中的幸运数': '1380', '设计一个支持增量操作的栈': '1381', '将二叉搜索树变平衡': '1382', '最大的团队表现值': '1383', '按年度列出销售总额': '1384', '两个数组间的距离值': '1385', '安排电影院座位': '1386', '将整数按权重排序': '1387', '3n块披萨': '1388', '按既定顺序创建目标数组': '1389', '四因数': '1390', '检查网格中是否存在有效路径': '1391', '最长快乐前缀': '1392', '股票的资本损益': '1393', '找出数组中的幸运数': '1394', '统计作战单位数': '1395', '设计地铁系统': '1396', '找到所有好字符串': '1397', '购买了产品A和产品B却没有购买产品C的顾客': '1398', '统计最大组的数目': '1399', '构造K个回文字符串': '1400', '圆和矩形是否有重叠': '1401', '做菜顺序': '1402', '非递增顺序的最小子序列': '1403', '将二进制表示减到1的步骤数': '1404', '最长快乐字符串': '1405', '石子游戏III': '1406', '排名靠前的旅行者': '1407', '数组中的字符串匹配': '1408', '查询带键的排列': '1409', 'HTML实体解析器': '1410', '给Nx3网格图涂色的方案数': '1411', '查找成绩处于中游的的学生': '1412', '逐步求和得到正数的最小值': '1413', '和为K的最少斐波那契数字数目': '1414', '长度为n的开心字符串中字典序第k小的字符串': '1415', '恢复数组': '1416', '重新格式化字符串': '1417', '点菜展示表': '1418', '数青蛙': '1419', '生成数组': '1420', '净现值查询': '1421', '分割字符串的最大得分': '1422', '可获得的最大点数': '1423', '对角线遍历II': '1424', '带限制的子序列和': '1425', '数元素': '1426', '字符串的左右移': '1427', '至少有一个1的最左端列': '1428', '第一个唯一数字': '1429', '判断给定的序列是否是二叉树从根到叶的路径': '1430', '拥有最多糖果的孩子': '1431', '改变一个整数能得到的最大差值': '1432', '检查一个字符串是否可以打破另一个字符串': '1433', '每个人戴不同帽子的方案数': '1434', '制作会话柱状图': '1435', '旅行终点站': '1436', '是否所有1都至少相隔k个元素': '1437', '绝对差不超过限制的最长连续子数组': '1438', '有序矩阵中的第k个最小数组和': '1439', '计算布尔表达式的值': '1440', '用栈操作构建数组': '1441', '形成两个异或相等数组的三元组数目': '1442', '收集树上所有苹果的最少时间': '1443', '切披萨的方案数': '1444', '苹果和桔子': '1445', '连续字符': '1446', '最简分数': '1447', '统计二叉树中好节点的数目': '1448', '数位成本和为目标值的最大数字': '1449', '在既定时间做作业的学生人数': '1450', '重新排列句子中的单词': '1451', '收藏清单': '1452', '圆形靶内的最大飞镖数量': '1453', '活跃用户': '1454', '检查单词是否为句中其他单词的前缀': '1455', '定长子串中元音的最大数目': '1456', '二叉树中的伪回文路径': '1457', '两个子序列的最大点积': '1458', '通过翻转子数组使两个数组相等': '1460', '检查一个字符串是否包含所有长度为K的二进制子串': '1461', '课程安排IV': '1462', '摘樱桃II': '1463', '数组中两元素的最大乘积': '1464', '切割后面积最大的蛋糕': '1465', '重新规划路线': '1466', '两个盒子中球的颜色数相同的概率': '1467', '计算税后工资': '1468', '寻找所有的独生节点': '1469', '重新排列数组': '1470', '数组中的k个最强值': '1471', '设计浏览器历史记录': '1472', '给房子涂色III': '1473', '删除链表M个节点之后的N个节点': '1474', '商品折扣后的最终价格': '1475', '子矩形查询': '1476', '找两个和为目标值且不重叠的子数组': '1477', '安排邮筒': '1478', '一维数组的动态和': '1480', '不同整数的最少数目': '1481', '制作m束花所需的最少天数': '1482', '树节点的第K个祖先': '1483', '克隆含随机指针的二叉树': '1484', '按日期分组销售产品': '1485', '数组异或操作': '1486', '保证文件名唯一': '1487', '避免洪水泛滥': '1488', '找到最小生成树里的关键边和伪关键边': '1489', '克隆N叉树新': '1490', '去掉最低工资和最高工资后的工资平均值': '1491', 'n的第k个因子': '1492', '删掉一个元素以后全为1的最长子数组': '1493', '并行课程II': '1494', 'FriendlyMoviesStreamedLastMonth新': '1495', '判断路径是否相交': '1496', '检查数组对是否可以被k整除': '1497', '满足条件的子序列数目': '1498', '满足不等式的最大值': '1499', 'DesignaFileSharingSystem': '1500', 'CountriesYouCanSafelyInvestIn': '1501', '判断能否形成等差数列': '1502', '所有蚂蚁掉下来前的最后一刻': '1503', '统计全1子矩形': '1504', '最多K次交换相邻数位后得到的最小整数': '1505', 'FindRootofN-AryTree新': '1506', '转变日期格式': '1507', '子数组和排序后的区间和': '1508', '三次操作后最大值与最小值的最小差': '1509', '石子游戏IV': '1510', 'CustomerOrderFrequency新': '1511', '猜数字': 'LCP01', '分式化简': 'LCP02', '机器人大冒险': 'LCP03', '覆盖': 'LCP04', '发LeetCoin': 'LCP05', '拿硬币': 'LCP06', '传递信息': 'LCP07', '剧情触发时间': 'LCP08', '最小跳跃次数': 'LCP09', '二叉树任务调度': 'LCP10', '期望个数统计': 'LCP11', '小张刷题计划': 'LCP12', '寻宝': 'LCP13', '切分数组': 'LCP14', '游乐园的迷宫': 'LCP15', '游乐园的游览计划': 'LCP16', '数组中重复的数字': '剑指Offer03', '二维数组中的查找': '剑指Offer04', '替换空格': '剑指Offer05', '从尾到头打印链表': '剑指Offer06', '重建二叉树': '剑指Offer07', '用两个栈实现队列': '剑指Offer09', '斐波那契数列': '剑指Offer10-I', '青蛙跳台阶问题': '剑指Offer10-II', '旋转数组的最小数字': '剑指Offer11', '矩阵中的路径': '剑指Offer12', '机器人的运动范围': '剑指Offer13', '剪绳子': '剑指Offer14-I', '剪绳子II': '剑指Offer14-II', '二进制中1的个数': '剑指Offer15', '数值的整数次方': '剑指Offer16', '打印从1到最大的n位数': '剑指Offer17', '删除链表的节点': '剑指Offer18', '表示数值的字符串': '剑指Offer20', '调整数组顺序使奇数位于偶数前面': '剑指Offer21', '链表中倒数第k个节点': '剑指Offer22', '合并两个排序的链表': '剑指Offer25', '树的子结构': '剑指Offer26', '二叉树的镜像': '剑指Offer27', '对称的二叉树': '剑指Offer28', '顺时针打印矩阵': '剑指Offer29', '包含min函数的栈': '剑指Offer30', '栈的压入、弹出序列': '剑指Offer31', '从上到下打印二叉树': '剑指Offer32-I', '从上到下打印二叉树II': '剑指Offer32-II', '从上到下打印二叉树III': '剑指Offer32-III', '二叉搜索树的后序遍历序列': '剑指Offer33', '二叉树中和为某一值的路径': '剑指Offer34', '复杂链表的复制': '剑指Offer35', '二叉搜索树与双向链表': '剑指Offer36', '序列化二叉树': '剑指Offer37', '数组中出现次数超过一半的数字': '剑指Offer39', '最小的k个数': '剑指Offer40', '数据流中的中位数': '剑指Offer41', '连续子数组的最大和': '剑指Offer42', '1～n整数中1出现的次数': '剑指Offer43', '数字序列中某一位的数字': '剑指Offer44', '把数组排成最小的数': '剑指Offer45', '把数字翻译成字符串': '剑指Offer46', '礼物的最大价值': '剑指Offer47', '最长不含重复字符的子字符串': '剑指Offer48', '第一个只出现一次的字符': '剑指Offer50', '数组中的逆序对': '剑指Offer51', '两个链表的第一个公共节点': '剑指Offer52', '在排序数组中查找数字I': '剑指Offer53-I', '0～n-1中缺失的数字': '剑指Offer53-II', '二叉搜索树的第k大节点': '剑指Offer54', '二叉树的深度': '剑指Offer55-I', '数组中数字出现的次数': '剑指Offer56-I', '数组中数字出现的次数II': '剑指Offer56-II', '和为s的两个数字': '剑指Offer57', '和为s的连续正数序列': '剑指Offer57-II', '翻转单词顺序': '剑指Offer58-I', '左旋转字符串': '剑指Offer58-II', '滑动窗口的最大值': '剑指Offer59-I', '队列的最大值': '剑指Offer59-II', 'n个骰子的点数': '剑指Offer60', '扑克牌中的顺子': '剑指Offer61', '圆圈中最后剩下的数字': '剑指Offer62', '股票的最大利润': '剑指Offer63', '求1+2+…+n': '剑指Offer64', '不用加减乘除做加法': '剑指Offer65', '构建乘积数组': '剑指Offer66', '把字符串转换成整数': '剑指Offer67', '判定字符是否唯一': '面试题01.01', '判定是否互为字符重排': '面试题01.02', 'URL化': '面试题01.03', '一次编辑': '面试题01.05', '字符串压缩': '面试题01.06', '旋转矩阵': '面试题01.07', '零矩阵': '面试题01.08', '字符串轮转': '面试题01.09', '移除重复节点': '面试题02.01', '返回倒数第k个节点': '面试题02.02', '删除中间节点': '面试题02.03', '分割链表': '面试题02.04', '链表求和': '面试题02.05', '链表相交': '面试题02.07', '环路检测': '面试题02.08', '三合一': '面试题03.01', '栈的最小值': '面试题03.02', '堆盘子': '面试题03.03', '化栈为队': '面试题03.04', '栈排序': '面试题03.05', '动物收容所': '面试题03.06', '节点间通路': '面试题04.01', '特定深度节点链表': '面试题04.03', '检查平衡性': '面试题04.04', '合法二叉搜索树': '面试题04.05', '后继者': '面试题04.06', '首个共同祖先': '面试题04.08', '二叉搜索树序列': '面试题04.09', '检查子树': '面试题04.10', '求和路径': '面试题04.12', '插入': '面试题05.01', '二进制数转字符串': '面试题05.02', '翻转数位': '面试题05.03', '下一个数': '面试题05.04', '整数转换': '面试题05.06', '配对交换': '面试题05.07', '绘制直线': '面试题05.08', '三步问题': '面试题08.01', '迷路的机器人': '面试题08.02', '魔术索引': '面试题08.03', '幂集': '面试题08.04', '递归乘法': '面试题08.05', '汉诺塔问题': '面试题08.06', '无重复字符串的排列组合': '面试题08.07', '有重复字符串的排列组合': '面试题08.08', '括号': '面试题08.09', '颜色填充': '面试题08.10', '硬币': '面试题08.11', '八皇后': '面试题08.12', '堆箱子': '面试题08.13', '布尔运算': '面试题08.14', '合并排序的数组': '面试题10.01', '变位词组': '面试题10.02', '搜索旋转数组': '面试题10.03', '稀疏数组搜索': '面试题10.05', '排序矩阵查找': '面试题10.09', '数字流的秩': '面试题10.10', '峰与谷': '面试题10.11', '交换数字': '面试题16.01', '单词频率': '面试题16.02', '交点': '面试题16.03', '井字游戏': '面试题16.04', '阶乘尾数': '面试题16.05', '最小差': '面试题16.06', '最大数值': '面试题16.07', '整数的英语表示': '面试题16.08', '运算': '面试题16.09', '生存人数': '面试题16.10', '跳水板': '面试题16.11', '平分正方形': '面试题16.13', '最佳直线': '面试题16.14', '珠玑妙算': '面试题16.15', '部分排序': '面试题16.16', '连续数列': '面试题16.17', '模式匹配': '面试题16.18', '水域大小': '面试题16.19', 'T9键盘': '面试题16.20', '交换和': '面试题16.21', '兰顿蚂蚁': '面试题16.22', '数对和': '面试题16.24', 'LRU缓存': '面试题16.25', '计算器': '面试题16.26', '不用加号的加法': '面试题17.01', '消失的数字': '面试题17.04', '字母与数字': '面试题17.05', '2出现的次数': '面试题17.06', '婴儿名字': '面试题17.07', '马戏团人塔': '面试题17.08', '第k个数': '面试题17.09', '主要元素': '面试题17.10', '单词距离': '面试题17.11', 'BiNode': '面试题17.12', '恢复空格': '面试题17.13', '最小K个数': '面试题17.14', '最长单词': '面试题17.15', '按摩师': '面试题17.16', '多次搜索': '面试题17.17', '最短超串': '面试题17.18', '消失的两个数字': '面试题17.19', '连续中值': '面试题17.20', '直方图的水量': '面试题17.21', '单词转换': '面试题17.22', '最大黑方阵': '面试题17.23', '最大子矩阵': '面试题17.24', '单词矩阵': '面试题17.25', '稀疏相似度': '面试题17.26'}
    
    return mapping.get(string, "0") #返回”0“代表失败
