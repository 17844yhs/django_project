-- Active: 1719634468171@@127.0.0.1@3306@xiaomishopper
-- 顶级分类：手机
INSERT INTO t_category (name, parent_id) VALUES ('手机', NULL);
-- 顶级分类：电视
INSERT INTO t_category (name, parent_id) VALUES ('电视', NULL);
-- 顶级分类：笔记本 平板
INSERT INTO t_category (name, parent_id) VALUES ('笔记本 平板', NULL);
-- 顶级分类：家电
INSERT INTO t_category (name, parent_id) VALUES ('家电', NULL);
-- 顶级分类：出行穿戴
INSERT INTO t_category (name, parent_id) VALUES ('出行穿戴', NULL);
-- 顶级分类：智能路由器
INSERT INTO t_category (name, parent_id) VALUES ('智能路由器', NULL);
-- 顶级分类：电源配件
INSERT INTO t_category (name, parent_id) VALUES ('电源配件', NULL);
-- 顶级分类：健康儿童
INSERT INTO t_category (name, parent_id) VALUES ('健康儿童', NULL);
-- 顶级分类：耳机音箱
INSERT INTO t_category (name, parent_id) VALUES ('耳机音箱', NULL);
-- 顶级分类：生活箱包
INSERT INTO t_category (name, parent_id) VALUES ('生活箱包', NULL);

-- 手机子分类（顶级分类ID=1）
INSERT INTO t_category (name, parent_id) VALUES ('小米手机', 1);
INSERT INTO t_category (name, parent_id) VALUES ('Redmi手机', 1);
INSERT INTO t_category (name, parent_id) VALUES ('黑鲨手机', 1);

-- 电视子分类（顶级分类ID=2）
INSERT INTO t_category (name, parent_id) VALUES ('小米电视', 2);
INSERT INTO t_category (name, parent_id) VALUES ('Redmi电视', 2);
INSERT INTO t_category (name, parent_id) VALUES ('激光电视', 2);

-- 笔记本 平板子分类（顶级分类ID=3）
INSERT INTO t_category (name, parent_id) VALUES ('笔记本电脑', 3);
INSERT INTO t_category (name, parent_id) VALUES ('平板电脑', 3);

