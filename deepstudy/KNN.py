from numpy import *
import operator

'''
KNN分类算法
出现问题
AttributeError: 'dict' object has no attribute 'iteritems'
Python3.5中：iteritems变为items
'''

def createDataSet():
    #创建数据集
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#print(group)
#print(labels)

def classify0(intX,dataSet,labels,k):
    #距离计算
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    #选择距离最小的K个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    #排序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

group,labels = createDataSet()

print("输入:[1.2,0]")
print("输出:"+classify0([1.2,0],group,labels,3))

print("输入:[1.5,1]")
print("输出:"+classify0([1.5,1],group,labels,3))

print("输入:[0,0.5]")
print("输出:"+classify0([0,0.5],group,labels,3))