<script setup>
import { useRouter } from 'vue-router';
import { userStore } from '@/stores/userStore'
import { cartStore } from '@/stores/cartStore';
import loout from '@/components/loout.vue';
import { onMounted, ref } from 'vue';
import api from '@/apis';
// 控制退出弹窗
const showLogoutModal = ref(false)
const router = useRouter()
const store = userStore()
const cart = cartStore()
const cartList = ref({})
const handleLogout = () => {
    // 执行退出登录逻辑
    store.quituser() // 假设你的 store 有 logout 方法
    cart.clearCart()
    showLogoutModal.value = false
}
// 获取购物车数据
const get_cart = async () => {
    // 判断是否登录
    if (sessionStorage.getItem('token')) {
        await cart.getcart()
        cartList.value = cart.cart.data
    }
    else {
        store.quituser()
    }
}
onMounted(async () => {
    console.log(sessionStorage.getItem('token'));

    await get_cart()
})
const DeleteCart =async (ItemId)=>{
    await api.delete_cart(ItemId)
    get_cart()   
     
}

</script>
<template>
    <!-- 退出登录弹窗 -->
    <loout :show="showLogoutModal" @close="showLogoutModal = false" @confirm="handleLogout"/>
    <!-- 顶部导航 -->
    <div class="topnav">
        <div class="container clearfix">
            <ul class="fl topnav-menu clearfix">
                <li class="fl"><a href="">小米商城</a></li>
                <li class="fl"><a href="">MIUI</a></li>
                <li class="fl"><a href="">loT</a></li>
                <li class="fl"><a href="">云服务</a></li>
                <li class="fl"><a href="">天星数科</a></li>
                <li class="fl"><a href="">有品</a></li>
                <li class="fl"><a href="">小爱开放平台</a></li>
                <li class="fl"><a href="">企业团购</a></li>
                <li class="fl"><a href="">资质证照</a></li>
                <li class="fl"><a href="">协议规则</a></li>
                <li class="fl"><a href="">下载app</a></li>
                <li class="fl"><a href="">智能生活</a></li>
                <li class="fl"><a href="">SelectLocation</a></li>
            </ul>
            <div class="fr">

                <!-- 登录，注册，消息通知 -->
                <ul class="topnav-menu fl" v-if="store.userinfo">
                    <li class="fl user-info">
                        <a href="/" @click.prevent="">
                            <img class="user-avatar" :src="'http://localhost:8000/static' + store.userinfo.avatar"
                                alt="">
                            <span class="user-name">{{ store.userinfo.nick_name }}</span>
                        </a>
                    </li>
                    <li class="fl"><a href="" @click.prevent="">消息通知</a></li>
                    <li class="fl"><a href="" @click.prevent="showLogoutModal = true">退出登录</a></li>
                </ul>
                <ul class="topnav-menu fl" v-else>
                    <li class="fl"><a href="/" @click.prevent="router.push('/login')">登录</a></li>
                    <li class="fl"><a href="" @click.prevent="router.push('/register')">注册</a></li>
                    <li class="fl"><a href="">消息通知</a></li>
                </ul>
                <!-- 购物车 -->
                <div class="fl topnav-car">
                    <a class="topnav-link" href="">
                        <i class="i-car iconfont"></i>

                        <span v-if="store.userinfo && cartList">购物车({{ cartList.total_items }})</span>
                        <span v-else>购物车(0)</span>
                    </a>
                    <!-- 购物车详情 - 有商品 -->
                    <div class="topnav-detail">
                        <div class="cart-content">
                            <div class="cart-items" v-for="item in cartList.items" :key="item.goods.id">
                                <div class="cart-item">
                                    <div class="item-img">
                                        <img :src="'http://localhost:8000/static' + item.goods.pic" alt="小米手机">
                                    </div>
                                    <div class="item-info">
                                        <div class="item-name">{{ item.goods.name }}</div>
                                        <div class="item-details">
                                            <div class="item-price">{{ item.goods.price }}元 * {{ item.quantity }}</div>
                                            <div class="multiply-symbol animated" @click="DeleteCart(item.id)">x</div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="cart-footer">
                                <div class="total-price">
                                    <span>共{{ cartList.total_items }}件 合计：</span>¥{{ cartList.total_price }}
                                </div>
                                <button class="btn-checkout" @click="router.push('/pay')">去结算</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>