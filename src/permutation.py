# -*- coding:utf-8 -*-
'''
  Copyright (C) 2015 Eric Zhang, China
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as
  published by the Free Software Foundation, either version 3 of
  the License, or (at your option) any later version.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.
 
  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
  Created on 2015-9-21
  @author: eric.zhang
  @contact: zgzczzw@163.com
  
'''
from const import const

class Permutation:
    words = ["1", "2", "3"]
    result = []
    length = len(words)
    
    def __init__(self):
        self.result = []
    
    def permutationList(self):
        while '' in self.words:
            self.words.remove('')
        while ' ' in self.words:
            self.words.remove(' ')
        self.result = []
        self.length = len(self.words)
        
        new_list = list(set(self.words))
        if len(new_list) <= 1:
            self.output()
            return self.result
    
        fromIndex = 0
        endIndex = 0
        changeIndex = 0
        if(len(self.words) <= 0):
            return
        if const.isDebug:
            print self.words
        self.sort(0, self.length - 1)
        
        while True:
            #输出一种全排列
            self.output();
            fromIndex = endIndex = self.length - 1
            #向前查找第一个变小的元素
            while (fromIndex > 0 and self.words[fromIndex] < self.words[fromIndex - 1]):
                fromIndex -= 1
                
            changeIndex = fromIndex;
            
            if (fromIndex == 0):
                break;
            #向后查找最后一个大于words[fromIndex - 1]的元素
            while (changeIndex + 1 < self.length and self.words[changeIndex + 1] > self.words[fromIndex - 1]):
                changeIndex += 1
                
            self.swap(fromIndex - 1, changeIndex)#交换两个值
            
            self.invertArray(fromIndex, endIndex) #对后面的所有值进行反向处理
            
        return self.result
            
    def output(self):
        rst = "";
        for index in range(0, len(self.words)):
            rst += str(self.words[index])
        if(const.isDebug):
            print rst
        self.result.append(rst)
            
    def sort(self, fromIndex, endIndex):
                self.words.sort();
                
    def swap(self, indexX, indexY):
        if ((indexX != indexY) and indexX >= 0 \
            and indexY >= 0 and len(self.words) \
            > indexX and len(self.words) > indexY):
            ch = self.words[indexX]
            self.words[indexX] = self.words[indexY]
            self.words[indexY] = ch
            
    def invertArray(self, fromIndex, endIndex):
        while fromIndex < endIndex:
            fromIndex += 1
            endIndex -= 1
            self.swap(fromIndex, endIndex)

