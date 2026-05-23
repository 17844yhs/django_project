const base = {
    login:'/api/login/', // 登录接口
    captcha:'/api/captcha/', // 获取验证码
    register:'/api/register/', // 注册接口
    userinfo: (userId) => `/api/user/${userId}/`,  // 动态生成 URL // 获取用户信息
    getcategory:'/apit/category/', // 获取分类
    getgoodsbycategory:'/apit/goodsbycategory/', // 根据分类id获取商品信息
    getgoodsbyname:'/apit/goodsbyname/', // 根据模糊查询获取商品信息
    getbanner:'/banner/all/', // 获取所有轮播图信息
    getcart:'apit/cart/', // 获取购物车信息
    addcart:'apit/cart/item/create/', // 增加购物车商品
    updatecart:(ItemId) =>`apit/cart/item/update/${ItemId}`, // 更新购物车商品
    deletecart:(ItemId) =>`apit/cart/item/delete/${ItemId}`, // 删除购物车商品
    getaddressall:'address/all', // 获取地址信息
    addaddressall:'address/add/', // 增加地址信息

}

export default base






// 假设 userId 是从某个地方获取到的（例如，来自 Vuex、props 或路由参数）
// const userId = 123; // 这里需要根据实际情况传递 userId
// const userInfoUrl = base.userinfo(userId);

// console.log(userInfoUrl);  // 输出: /api/user/123/