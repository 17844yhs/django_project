<script setup>
import router from '@/router';

</script>

<template>
        <!-- 右侧固定菜单 -->
      <div class="rm">
          <a href="" class="rm-item">
                <i class="iconfont i-tel"></i>
                <span class="rm-title">手机APP</span>
            <div class="rm-mention">
                <img src="@/styles/img/qrcode.png" alt="">
                <p>扫码领取新
                    <br>
                    人百元礼包</p>
            </div>
          </a>
          <a  href="" class="rm-item" @click.prevent="router.push('/my')">
            <i class="iconfont i-yonghu"></i>
            <span class="rm-title">个人中心</span>
          </a>
          <a  href="" class="rm-item">
            <i class="iconfont i-weixiu1"></i>
            <span class="rm-title">售后服务</span>
          </a>
          <a  href="" class="rm-item">
            <i class="iconfont i-kefu"></i>
            <span class="rm-title">人工客服</span>
          </a>
          <a  href="" class="rm-item">
            <i class="iconfont i-car"></i>
            <span class="rm-title">购物车</span>
          </a> 
          <a  href="javascript:scrollTo(0,0)" class="rm-item to-top">
            <i class="iconfont i-dingbu"></i>
            <span class="rm-title">回到顶部</span>
          </a>
     </div>
</template>