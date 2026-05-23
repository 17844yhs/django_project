<script setup>
import { onMounted, ref } from 'vue';
import api from '@/apis';
import router from '@/router';
const goods = ref('')
// 获取后端随机九个商品
const get_goods =async ()=>{
    const res = await api.get_goodsbyname()
    // 打乱数组顺序
    const shuffledArray = res.data.sort(() => Math.random() - 0.5);
    goods.value = shuffledArray.slice(0,8)
}
onMounted(()=>{
    get_goods()
})
</script> 

<template>
       <!-- 主区域 -->
    <div class="main">
        <!-- 广告 -->
     <a href="" class="banner3  container">
        <img src="@/styles/img/full-banner.webp" alt="">
     </a>    
     <!-- 橱窗 -->
      <div class="sc container">
        <div class="sc-top clearfix">
            <h2 class="sc-title fl">部分商品</h2>
            <a href="" class="sc-more fr" @click.prevent="router.push('/goods')" >查看更多
                <i class="iconfont i-right" ></i>
            </a>
        </div>
        <div class="sc-container clearfix">
          <div class="sc-item-first fl">
            <a href="">
                <img src="@/styles/img/mobile-first.webp" alt="">
            </a>
          </div>
          <div class="sc-item-list fl">
            <a href="" class="sc-item fl" v-for="good in goods" :key="good.id">
                <img :src="'http://localhost:8000/static' + good.pic" alt="">
                <p class="sc-name">{{good.name}}</p>
                <p class="sc-desc">{{good.description}}</p>
                <p class="price">{{good.price}}元起</p>
            </a>
          </div>
        </div>
      </div>
    </div>
</template>