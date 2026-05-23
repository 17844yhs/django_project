import instance from "@/utils/http";
import base from '@/apis/base'

const api = {
//      login: function(params) {
//     return instance.post(base.login, params, {
//       withCredentials: true
//     });
//   }
// login: (params) => {
//   return instance.post(base.login, params, { withCredentials: true });
// }
     login(params) {
        return instance.post(base.login, params, {
            withCredentials: true // 仅此接口携带 Cookie
        });
    },
    register(params){
        return instance.post(base.register,params)
    },
    get_userone: (userId) => {
    const url = base.userinfo(userId);  // 生成动态 URL
    return instance.get(url);  // 发送请求
  },
    // get_captcha(params){
    //     return instance.get(base.captcha,{params})
    // }
    get_captcha(params) {
    return instance.get(base.captcha, { 
        params:params, 
        withCredentials: true, // 跨域（含不同端口）必须加！
        responseType: 'arraybuffer'
    });},
    get_category(params){
        return instance.get(base.getcategory,{params})
    },
    get_goodsbycategory(params){
        return instance.get(base.getgoodsbycategory,{params})
    },
    get_goodsbyname(params){
        return instance.get(base.getgoodsbyname,{params})
    },
    get_bannerall(params){
        return instance.get(base.getbanner,{params})
    },
    get_cartall(params){
        return instance.get(base.getcart,{params})
    },
    add_cart(params){
        return instance.post(base.addcart,params)
    },
    update_cart: (ItemId,params) => {
    const url = base.updatecart(ItemId);  // 生成动态 URL
    return instance.put(url,params);  // 发送请求
    },
    delete_cart: (ItemId) => {
    const url = base.deletecart(ItemId);  // 生成动态 URL
    return instance.delete(url);  // 发送请求
    },
    get_addressall(params){
        return instance.get(base.getaddressall)
    },
    add_address(params){
        return instance.post(base.addaddressall,params)
    }
}

export default api