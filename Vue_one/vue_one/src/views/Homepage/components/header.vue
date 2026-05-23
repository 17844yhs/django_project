<script setup>
import { onMounted, ref,computed } from 'vue';
import api from '@/apis';
// 获取后的分类数据
const categorys = ref([])
// 模糊查询的name
const name = ref([])
// 计算属性添加空值检查
const slicedCategorys = computed(() => {
  return categorys.value?.slice(10, 15) || [];
});
// 初始化分类
onMounted(async()=>{
    categorys.value = await api.get_category()
})
// 根据分类id获取下面的商品数据
const hoverHandle =async (e)=>{
    const res = await api.get_goodsbycategory({id:e.id})
    console.log(e.id,res);
    
}
// 根据name模糊查询商品
const SearchHandle = async(e)=>{
    const res = await api.get_goodsbyname({name:name.value})
    console.log(name.value,res);
}
// 根据关键字 nmae 查询商品
const setSearchName  = async (e)=>{
    name.value = e
    await SearchHandle()
}
</script>

<template>
    <!-- 页头 -->
    <div class="header">
        <div class="container clearfix">
            <a href="" class="header-logo fl">
                <h1>小米商城</h1>
            </a>
            <div class="header-menu fl">
                <a @click.prevent="" @mouseenter="hoverHandle(category)" class="fl" href="" v-for="category in slicedCategorys" :key="category.id">{{ category.name }}</a>
                <a class="fl" href="">服务</a>
                <a class="fl" href="">社区</a>
                <!-- 二级菜单 -->
                <div class="header-submenu">
                    <div class="container clearfix">
                        <a href="" class="fl">
                            <div class="header-cover">
                                <img src="@/styles/img/product.webp" alt="">
                            </div>
                            <div class="header-name">Redmi Note 11 5G</div>
                            <div class="header-price">1199元起</div>
                        </a>
                        <a href="" class="fl">
                            <div class="header-cover">
                                <img src="@/styles/img/product.webp" alt="">
                            </div>
                            <div class="header-name">Redmi Note 11 5G</div>
                            <div class="header-price">1199元起</div>
                        </a>
                    </div>
                </div>
            </div>
            <!-- 搜索 -->
            <form class="header-search fr clearfix">
                <input v-model="name" class="fl" type="text" placeholder="手机" />
                <button class="header-searchicon fl" @click.prevent="SearchHandle">
                    <i class="iconfont i-fangdajing"></i>
                </button>
                <div class="header-suggest">
                    <a href="" @click.prevent="setSearchName('')">全部商品</a>
                    <a href="" @click.prevent="setSearchName('手机')">手机</a>
                    <a href="" @click.prevent="setSearchName('耳机')">耳机</a>
                    <a href="" @click.prevent="setSearchName('小米平板5 Pro')">小米平板5 Pro</a>
                    <a href="" @click.prevent="setSearchName('加湿器')">加湿器</a>
                    <a href="" @click.prevent="setSearchName('笔记本')">笔记本</a>
                </div>
            </form>
        </div>
    </div>
</template>