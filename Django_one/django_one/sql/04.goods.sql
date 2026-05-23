-- 7. 小米平板7 Pro（分类：笔记本 平板→平板电脑，ID=18）

INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米平板7 Pro', 2999.00, 
    '11英寸2.8K屏 | 骁龙8+ Gen1 | 四扬声器',
    0, 120, '/images/mi_pad7_pro.jpg', '小米科技园', 18, NOW(), NOW()
);

-- 8. Redmi Pad 6（分类：笔记本 平板→平板电脑，ID=18）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    'Redmi Pad 6', 1299.00, 
    '10.95英寸2K屏 | 联发科G99 | 续航12小时',
    0, 200, '/images/redmi_pad6.jpg', '小米科技园', 18, NOW(), NOW()
);

-- 9. 小米空气净化器4 Pro（分类：家电，ID=4）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米空气净化器4 Pro', 899.00, 
    'H13级HEPA | 500m³/h CADR值 | 智能控制',
    0, 90, '/images/mi_air_purifier.jpg', '小米科技园', 4, NOW(), NOW()
);

-- 10. 米家扫地机器人Ultra（分类：家电，ID=4）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '米家扫地机器人Ultra', 4799.00, 
    '全场景导航 | 5000Pa吸力 | 自动集尘',
    1, 0, '/images/mi_robot_vacuum.jpg', '小米科技园', 4, NOW(), NOW()  -- 缺货
);

-- 11. 小米手表S3（分类：出行穿戴，ID=5）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米手表S3', 1599.00, 
    'AMOLED大屏 | 14天续航 | 5ATM防水',
    0, 75, '/images/mi_watch_s3.jpg', '小米科技园', 5, NOW(), NOW()
);



-- 14. 小米路由器AX9000（分类：智能路由器，ID=6）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米路由器AX9000', 999.00, 
    'Wi-Fi 6 | 5400Mbps速率 | 12根天线',
    0, 100, '/images/mi_router_ax9000.jpg', '小米科技园', 6, NOW(), NOW()
);

-- 15. 小米移动电源3 20000mAh（分类：电源配件，ID=7）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米移动电源3', 199.00, 
    '20000mAh | 65W双向快充 | 数显屏',
    0, 400, '/images/mi_power_bank3.jpg', '小米科技园', 7, NOW(), NOW()
);

-- 16. 小米手环8 NFC版（分类：出行穿戴，ID=5）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米手环8 NFC版', 299.00, 
    '1.62英寸屏 | 14天续航 | 门禁卡/公交卡',
    0, 300, '/images/mi_band8_nfc.jpg', '小米科技园', 5, NOW(), NOW()
);

-- 17. 米家冰箱十字门506L（分类：家电，ID=4）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '米家冰箱十字门506L', 3299.00, 
    '一级能效 | 双变频 | 母婴专属空间',
    0, 30, '/images/mi_fridge_506l.jpg', '小米科技园', 4, NOW(), NOW()
);

-- 18. 小米微波炉20L（分类：家电，ID=4）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米微波炉20L', 399.00, 
    '平板加热 | 智能菜单 | 一键启动',
    0, 180, '/images/mi_microwave.jpg', '小米科技园', 4, NOW(), NOW()
);

-- 19. Redmi 显示器27英寸4K（分类：笔记本 平板→笔记本电脑配件，ID=17）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    'Redmi显示器27英寸4K', 1599.00, 
    '4K分辨率 | 99%sRGB色域 | HDR400',
    0, 60, '/images/redmi_monitor_27.jpg', '小米科技园', 17, NOW(), NOW()
);


-- 21. 小米体重秤2（分类：健康儿童，ID=8）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米体重秤2', 59.00, 
    '10项身体数据 | 蓝牙连接 | 高精度传感器',
    0, 500, '/images/mi_scale2.jpg', '小米科技园', 8, NOW(), NOW()
);

-- 22. 小米儿童手表9C（分类：健康儿童，ID=8）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米儿童手表9C', 399.00, 
    '4G全网通 | 1.52英寸屏 | 九重定位',
    0, 90, '/images/mi_kid_watch9c.jpg', '小米科技园', 8, NOW(), NOW()
);

-- 23. 小米旅行箱20英寸（分类：生活箱包，ID=10）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米旅行箱20英寸', 299.00, 
    'PC耐磨材质 | 万向轮 | TSA密码锁',
    0, 120, '/images/mi_suitcase_20.jpg', '小米科技园', 10, NOW(), NOW()
);

-- 24. 小米数据线Type-C（分类：电源配件，ID=7）
INSERT INTO t_goods (
    name, price, description, status, stock, pic, address, category_id,
    created_at, updated_at
) VALUES (
    '小米数据线Type-C', 29.90, 
    '6A快充 | 1.5米长 | 耐用编织线',
    0, 1000, '/images/mi_type_c_cable.jpg', '小米科技园', 7, NOW(), NOW()
);