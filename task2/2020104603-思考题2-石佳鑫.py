data_row = [] # 定义空列表存储整个数据集
file = open('part.tbl','r')
for line in file: # 逐行读取文件并存储
    row = line.rsplit(sep = '|')
    data_row.append(tuple(row))
    
dict_row = {"partkey":0, #定义目录映射不同变量位置
            "name":1,
            "mfgr":2,
            "brand":3,
            "type":4,
            "size":5,
            "container":6,
            "retailprice":7,
            "comment":8}
    
print(len(data_row))
print("查看第一行数据: ",data_row[0])

#统计`P_SIZE<15`并且`P_CONTAINER='WRAP BOX'`的P_RETAILPRICE累加和
retailprice_sum = 0
# 查找不同变量的存储索引
p_size = dict_row["size"]
p_container = dict_row["container"]
p_retailprice = dict_row["retailprice"]

for t in data_row: 
    if (int(t[p_size]) < 15) and (t[p_container] == 'WRAP BOX'):
        retailprice_sum += float(t[p_retailprice])

print("统计结果:", round(retailprice_sum,2))
