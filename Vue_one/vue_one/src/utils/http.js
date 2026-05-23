import axios from "axios"
import router from "@/router";

// 创建一个 axios 实例
const instance = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 0,
});

// 请求拦截器
instance.interceptors.request.use(
  (config) => {
    // // 在请求发送之前做一些操作，例如添加 token
    const token = sessionStorage.getItem('token')
    if(token){
      // console.log(token);
      config.headers.token = token
    }
    return config;  // 必须返回 config，否则请求无法继续
  },
  (error) => {
    // 请求错误时处理
    return Promise.reject(error);  // 返回一个拒绝的 Promise
  }
);

// 响应拦截器
instance.interceptors.response.use(
  (res) => {
    // 在响应数据返回时做一些操作，例如处理某些特殊的响应结构
    if(res.status == 200){
      if(res.data.code==401){
        sessionStorage.removeItem('token')
        sessionStorage.removeItem('user')
        sessionStorage.removeItem('cart');
        // token失效
        router.push('/login')
      }
    }
    
    return res.data;  // 返回响应数据
  },
  (e) => {
    // 响应错误时处理
    if (e.data) {
        // 统一错误提示
      console.error(e.response.data.message); 
    } else {
      console.error('响应错误数据为空');
    }
    return Promise.reject(e)
    }
);

export default instance