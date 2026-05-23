-- 用户1的购物车项（购物车ID=1，对应 user_id=1）
-- 1. 小米平板7 Pro x1（商品ID=1，单价2999 → 小计2999）
INSERT INTO t_cartitem (carts_id, goods_id, quantity, added_at) VALUES (
    1, 1, 1, NOW()
);
-- 2. 小米手环8 NFC版 x2（商品ID=8，单价299 → 小计598）
INSERT INTO t_cartitem (carts_id, goods_id, quantity, added_at) VALUES (
    1, 8, 2, NOW()
);

-- 用户2的购物车项（购物车ID=2，对应 user_id=2）
-- 1. Redmi Pad 6 x1（商品ID=2，单价1299 → 小计1299）
INSERT INTO t_cartitem (carts_id, goods_id, quantity, added_at) VALUES (
    2, 2, 1, NOW()
);
-- 2. 小米空气净化器4 Pro x1（商品ID=3，单价899 → 小计899）
INSERT INTO t_cartitem (carts_id, goods_id, quantity, added_at) VALUES (
    2, 3, 2, NOW()
);
