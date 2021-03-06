#!/usr/bin/env python
# coding=utf-8

# K-近邻算法

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
# 读取文件中的数据
Wdata = pd.read_csv('F:\learningsources\graduation project\dataset\depth_train.csv', sep=' ', header=None,
                    names=["weibo_id", "user_id", "time", "emotional_level", "fans_num", "at_flag", "topic_flag",
                           "url_flag", "content_length", 'time_step', 'follow_num', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6',
                           'd7', 'd8', 'd9'])
# 定义训练模型时使用的特征
predictors = ["emotional_level", "fans_num", "at_flag", "topic_flag", "url_flag", "content_length", "time_step", "d1",
              "d2"]

# 定义训练数据的自变量和目标变量不能
train_x = Wdata[predictors][:7000]
train_y = Wdata['d9'][:7000]

# 定义测试数据的自变量和目标变量
groud_truth = Wdata[predictors][7000:]
true_value = Wdata['d9'][7000:]
# 建立模型
model = KNeighborsRegressor(leaf_size=5000,n_neighbors=5,p=1)

# 训练模型 模型拟合
model.fit(train_x, train_y)

# # 模型预测
pre_value = model.predict(groud_truth)



# # 计算平均绝对百分比误差
a = (abs(pre_value - true_value) / true_value).sum()
average_error = a / len(pre_value)
average_precision=1-average_error
# print('K-邻近算法的平均绝对百分比误差为：', average_error)
# print('K-邻近算法的平均绝对百分比精度为：', average_precision)


fig=plt.figure('KNN：50条微博', figsize=(7, 5))
ax1 = fig.add_subplot(111)
ax1.set_title('KNN_average_precision=34.46%')
x1 = x2 = range(0, 50)
y1 = true_value[0:50]
y2 = pre_value[0:50]
plt.plot(x1,y1,c='r', label ='true_value')
plt.plot(x2,y2,"b--",  label='pre_value')
plt.ylabel('Depth')
plt.xlabel('WeiBo_Number')
plt.legend()
# plt.savefig('F:/learningsources/graduation project/result_images/KNN/KNN_LINE.png')
plt.show()




