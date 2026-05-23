-- 插入测试用户（手机号：13800138000，密码：123456）
INSERT INTO t_user (
    phone, nick_name, _pwd, gender, introduction, avatar,create_at,update_at
) VALUES (
    '13800138000',  -- 手机号（11位）
    '米粉小王',      -- 昵称
    'e10adc3949ba59abbe56e057f20f883e',  -- MD5加密后的密码（原始密码：123456）
    1,              -- 性别（1=男，0=女）
    '热爱小米生态的数码爱好者',  -- 简介
    '/avatars/user1.jpg'  -- 头像路径
    ,NOW(),NOW()
);

-- 插入第二个用户（用于测试多用户购物车）
INSERT INTO t_user (
    phone, nick_name, _pwd, gender, introduction, avatar,create_at,update_at
) VALUES (
    '13900139000', 
    '科技小周', 
    'e10adc3949ba59abbe56e057f20f883e',  -- 密码：123456
    0, 
    '喜欢追剧的电视党', 
    '/avatars/user2.jpg',
    NOW(),NOW()
);