import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import api from '@/apis'
import { cartStore } from './cartStore'
export const userStore = defineStore('user', () => {
  const userinfo = ref('')
  const cart = cartStore()
  // 获取用户信息
  async function getuserinfo(userid) {
      userinfo.value = await api.get_userone(userid);
  }
  // 前端退出时清除用户信息 
  function quituser(){
    sessionStorage.removeItem('token') // 清除 token
    userinfo.value = ''
    // 清除购物车数据
    cart.clearCart()
  }
  // 以对象的格式把state和action return
  return { userinfo, getuserinfo,quituser }
}, {
  persist: {
    enabled: true, // 确保启用持久化
    strategies: [
      {
        key: 'user', // 保存到 localStorage 中的 key
        storage: localStorage, // 或 sessionStorage
      },
    ],
  },
})
