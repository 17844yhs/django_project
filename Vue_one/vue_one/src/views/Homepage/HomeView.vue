<script setup>
import Topnav from './components/topnav.vue'; // 注意：大写首字母
import Header from './components/header.vue'; // 同样大写 
import Banner from './components/banner.vue';
import Banner2 from './components/banner2.vue';
import Main from './components/main.vue';
import Footer from './components/footer.vue';
import Rm from './components/rm.vue';
</script>

<template>
  <!-- 页头 -->
  <Topnav></Topnav>
  <!-- 顶部导航 -->
  <Header></Header>
  <!-- 横幅 -->
  <Banner></Banner>
  <!-- 横幅2 -->
  <Banner2></Banner2>
  <!-- 主区域 -->
  <Main></Main>
  <!-- 页脚区域 -->
  <Footer></Footer>
  <!-- 测导航 -->
  <Rm></Rm>
</template>
