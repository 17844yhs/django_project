<script setup>
import { onMounted, ref, computed,onUnmounted } from 'vue';
import api from '@/apis';
const categorys = ref()
const goodsbycategory = ref()
const slicedCategorys = computed(() => {
    return categorys.value?.slice(0, 9) || [];
});

const getbanner =async ()=>{
    const res = await api.get_bannerall()
    slides.value = res.data
    console.log( slides.value);
    
}
// 初始化左侧分类数据 和轮播图数据
onMounted(async () => {
    const res = await api.get_category()
    categorys.value = res
    getbanner()
    
})
// 滑到分类时调用接口
const hoverHandle = async (e) => {
    // 根据分类id获取下面的商品信息
    const res = await api.get_goodsbycategory({ id: e.id })
    goodsbycategory.value = res.data
    console.log(goodsbycategory.value);
}

// 轮播图数据（可替换为API请求）
const slides = ref([
  { pic: "src/styles/img/banner.jpeg",  title: "促销活动1" },
  { pic: "src/styles/img/banner1.jpg",  title: "促销活动2" },
  { pic: "src/styles/img/banner2.jpg",  title: "促销活动3" }
]);


const currentIndex = ref(0);
let timer = null;

// 切换到下一张
const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % slides.value.length;
};

// 切换到上一张
const prevSlide = () => {
  currentIndex.value = (currentIndex.value - 1 + slides.value.length) % slides.value.length;
};

// 跳转到指定幻灯片
const goToSlide = (index) => {
  currentIndex.value = index;
};

// 自动轮播
const startAutoPlay = () => {
  timer = setInterval(nextSlide, 3000);
};

// 暂停自动轮播
const pauseAutoPlay = () => {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
};

// 初始化
onMounted(() => {
  startAutoPlay();
});

// 清理
onUnmounted(() => {
  pauseAutoPlay();
});
</script>

<template>
    <!-- 轮播图容器 -->
    <div class="banner container" @mouseenter="pauseAutoPlay" @mouseleave="startAutoPlay">
        <!-- 动态轮播图片 -->
        <div class="banner-slides">
            <a v-for="(slide, index) in slides" :key="index" class="slide"
                :class="{ active: currentIndex === index }">
                <img :src="'http://localhost:8000/static' + slide.pic" :alt="slide.title || 'Banner'">
            </a>
        </div>

        <!-- 左右箭头（绑定点击事件） -->
        <div class="banner-pointer banner-pointer-left" @click="prevSlide">
            <i class="iconfont i-left"></i>
        </div>
        <div class="banner-pointer banner-pointer-right" @click="nextSlide">
            <i class="iconfont i-right"></i>
        </div>

        <!-- 动态圆点指示器 -->
        <div class="banner-dots">
            <span v-for="(_, index) in slides" :key="index" :class="{ 'banner-dots-selected': currentIndex === index }"
                @click="goToSlide(index)"></span>
        </div>
        <!-- 横幅-菜单 -->
        <ul class="banner-menu">
            <li v-for="category in slicedCategorys" :key="category.id">
                <div class="banner-menu-item clearfix" @mouseenter="hoverHandle(category)">
                    <span class="fl">{{ category.name }}</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu" v-for="good in goodsbycategory" :key="good.id">
                    <a href="" class="fl">
                        <img :src="'http://localhost:8000/static' + good.pic" alt="" class="fl" />
                        <span class="fl">{{ good.name }}</span>
                    </a>
                </div>
            </li>
            <!-- 
            <li>
                <div class="banner-menu-item clearfix" >
                    <span class="fl">手机</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/mobile.webp" alt="" class="fl" />
                        <span class="fl">Note 11 Pro 系列</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/mobile.webp" alt="" class="fl" />
                        <span class="fl">Note 11 Pro 系列</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">电视</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/tv.webp" alt="" class="fl" />
                        <span class="fl">Redmi 智能电视X65 2022款</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/tv.webp" alt="" class="fl" />
                        <span class="fl">Redmi 智能电视X65 2022款</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">笔记本 平板</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/notebook.webp" alt="" class="fl" />
                        <span class="fl">小米笔记本 Pro 14 锐龙版</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/notebook.webp" alt="" class="fl" />
                        <span class="fl">小米笔记本 Pro 14 锐龙版</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">家电</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/fridge.webp" alt="" class="fl" />
                        <span class="fl">冰箱</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/fridge.webp" alt="" class="fl" />
                        <span class="fl">冰箱</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">出行 穿戴</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/watch.webp" alt="" class="fl" />
                        <span class="fl">Redmi 手表 2</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/watch.webp" alt="" class="fl" />
                        <span class="fl">Redmi 手表 2</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">智能 路由器</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">

                    <a href="" class="fl">
                        <img src="./img/ai.webp" alt="" class="fl" />
                        <span class="fl">CyberDog</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/ai.webp" alt="" class="fl" />
                        <span class="fl">CyberDog</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">电源 配件</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">

                    <a href="" class="fl">
                        <img src="./img/power.webp" alt="" class="fl" />
                        <span class="fl">移动电源</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/power.webp" alt="" class="fl" />
                        <span class="fl">移动电源</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">健康 儿童</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/health.webp" alt="" class="fl" />
                        <span class="fl">米家跑步机</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/health.webp" alt="" class="fl" />
                        <span class="fl">米家跑步机</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">耳机 音箱</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/earphone.webp" alt="" class="fl" />
                        <span class="fl">Redmi Buds 3 青春版</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/earphone.webp" alt="" class="fl" />
                        <span class="fl">Redmi Buds 3 青春版</span>
                    </a>
                </div>
            </li>
            <li>
                <div class="banner-menu-item clearfix">
                    <span class="fl">生活 箱包</span>
                    <i class="iconfont i-right fr"></i>
                </div>
                <div class="banner-sub-menu">
                    <a href="" class="fl">
                        <img src="./img/bag.webp" alt="" class="fl" />
                        <span class="fl">小背包</span>
                    </a>
                    <a href="" class="fl">
                        <img src="./img/bag.webp" alt="" class="fl" />
                        <span class="fl">小背包</span>
                    </a>
                </div>
            </li> -->
        </ul>

    </div>

</template>