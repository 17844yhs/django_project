import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import api from '@/apis'
export const cartStore = defineStore('cart', () => {
  const cart = ref([])
  // 获取购物车数据
  async function getcart(){
    cart.value = await api.get_cartall()
  }
  // 清除购物车数据仅仅前端
  function clearCart(){
    cart.value = []
  }
  // 增加购物车商品
  async function addCart(params){
    await api.add_cart(params)
  }
  // 更新购物车数据
  async function updateCart(goodId,params){
    await api.update_cart(goodId,params)
  }
  // 删除购物车数据
  async function deleteCart(goodId){
    await api.delete_cart(goodId)
  }


  return { cart,getcart,clearCart,addCart,updateCart,deleteCart }
}, {
  persist: {
    enabled: true, // 确保启用持久化
    strategies: [
      {
        key: 'cart', // 保存到 localStorage 中的 key
        storage: localStorage, // 或 sessionStorage
      },
    ],
  },
})
