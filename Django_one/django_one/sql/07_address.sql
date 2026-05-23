-- 插入第一条数据，isDefault 设置为 1（表示默认地址）
INSERT INTO t_address (name, phone, province, city, district, detail, isDefault)
VALUES ('张先生', '138****8888', '北京市', '北京市', '海淀区', '中关村大街88号小米科技园', 1);

-- 插入第二条数据，isDefault 设置为 0（表示不是默认地址）
INSERT INTO t_address (name, phone, province, city, district, detail, isDefault)
VALUES ('李女士', '139****9999', '上海市', '上海市', '浦东新区', '陆家嘴环路100号', 0);

-- 插入第三条数据，isDefault 设置为 0（表示不是默认地址）
INSERT INTO t_address (name, phone, province, city, district, detail, isDefault)
VALUES ('王小明', '137****5555', '广东省', '深圳市', '南山区', '科技园南路3号腾讯大厦', 0);
