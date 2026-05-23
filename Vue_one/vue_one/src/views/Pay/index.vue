<script setup>
import api from '@/apis';
import { cartStore } from '@/stores/cartStore';
import router from '@/router';
import { ref, reactive, onMounted } from 'vue';

// 订单商品数据
const orderItems = ref([]);
const cart = cartStore()

// 收货地址数据
const addresses = ref([
    {
        id: 1,
        name: "张先生",
        phone: "138****8888",
        province: "北京市",
        city: "北京市",
        district: "海淀区",
        detail: "中关村大街88号小米科技园",
        isDefault: true
    }
]);

// 新增地址相关状态
const showAddAddressModal = ref(false);
const newAddress = reactive({
    name: '',
    phone: '',
    province: '',
    city: '',
    district: '',
    detail: '',
    isDefault: false
});

// 选中的地址
const selectedAddress = ref(1);

// 支付方式
const paymentMethod = ref("alipay");

// 订单摘要
const summary = reactive({
    subtotal: 6196,
    shipping: 0,
    discount: 200,
    total: 5996
});

// 选择地址
const selectAddress = (id) => {
    selectedAddress.value = id;
};

// 立即支付
const payNow = () => {
    alert(`正在跳转到${paymentMethod.value === 'alipay' ? '支付宝' :
        paymentMethod.value === 'wechat' ? '微信支付' :
            paymentMethod.value === 'bank' ? '银行卡' : '货到付款'}支付页面`);
};

// 获取商品数据
const get_data = ()=>{
    summary.subtotal = cart.cart.data.total_price
    summary.total = summary.subtotal-summary.discount
    orderItems.value = cart.cart.data.items
}

// 获取地址数据
const get_address = async ()=>{
    const res = await api.get_addressall()
    addresses.value = res.data
}

// 添加新地址
const addNewAddress = async () => {
    try {
        if(newAddress.isDefault==true){
            newAddress.isDefault=1
        }
        else{
            newAddress.isDefault=0
        }
        const params = newAddress
        
        const res = await api.add_address(params);
        await get_address()
        // 重置表单
        Object.assign(newAddress, {
            name: '',
            phone: '',
            province: '',
            city: '',
            district: '',
            detail: '',
            isDefault: false
        });
        showAddAddressModal.value = false;
    } catch (error) {
        console.error('添加地址失败:', error);
    }
};

onMounted(async () => {
    await get_data()
    await get_address()
})
</script>

<template>
    <div class="container">
        <!-- 头部 -->
        <header class="header">
            <div class="logo">
                <i class="fas fa-fire"></i>
                <a href="" @click.prevent="router.push('/')"><span><-小米商城</span></a>
            </div>
            <div class="nav">
                <span>订单支付</span>
            </div>
        </header>

        <!-- 步骤条 -->
        <div class="step-bar">
            <div class="step active">
                <div class="step-circle">1</div>
                <div class="step-text">确认订单</div>
            </div>
            <div class="step active">
                <div class="step-circle">2</div>
                <div class="step-text">支付订单</div>
            </div>
            <div class="step">
                <div class="step-circle">3</div>
                <div class="step-text">支付完成</div>
            </div>
        </div>

        <div class="main-content">
            <!-- 左侧内容 -->
            <div class="left-column">
                <!-- 订单信息 -->
                <div class="order-section">
                    <div class="section-title">
                        <i class="fas fa-shopping-bag"></i>
                        订单商品
                    </div>

                    <div class="order-item" v-for="item in orderItems" :key="item.id">
                        <div class="item-img">
                            <img :src="'http://localhost:8000/static' + item.goods.pic" :alt="item.goods.name">
                        </div>
                        <div class="item-info">
                            <div class="item-name">{{ item.goods.name }}</div>
                            <div class="item-spec">{{ item.goods.description }}</div>
                            <div class="item-price">¥{{ item.goods.price }}</div>
                        </div>
                        <div class="item-quantity">x{{ item.quantity }}</div>
                    </div>
                </div>

                <!-- 收货地址 -->
                <div class="order-section">
                    <div class="section-title">
                        <i class="fas fa-map-marker-alt"></i>
                        收货地址
                    </div>

                    <div class="address-card" v-for="address in addresses" :key="address?.id"
                        :class="{ selected: address?.id === selectedAddress }" @click="selectAddress(address?.id)">
                        <div class="address-header">
                            <div class="user-info">
                                <span class="user-name">{{ address?.name }}</span>
                                <span class="user-phone">{{ address?.phone }}</span>
                            </div>
                            <div v-if="address?.isDefault" class="default-tag">默认</div>
                        </div>
                        <div class="address-detail">
                            {{ address?.province }}{{ address?.city }}{{ address?.district }}{{ address?.detail }}
                        </div>
                    </div>

                    <div class="add-address" @click="showAddAddressModal = true">
                        <i class="fas fa-plus"></i> 添加新地址
                    </div>
                </div>

                <!-- 支付方式 -->
                <div class="order-section">
                    <div class="section-title">
                        <i class="fas fa-credit-card"></i>
                        支付方式
                    </div>

                    <div class="payment-methods">
                        <div class="payment-method" :class="{ selected: paymentMethod === 'alipay' }"
                            @click="paymentMethod = 'alipay'">
                            <div class="payment-icon alipay">
                                <i class="fab fa-alipay"></i>
                            </div>
                            <div class="payment-name">支付宝</div>
                        </div>

                        <div class="payment-method" :class="{ selected: paymentMethod === 'wechat' }"
                            @click="paymentMethod = 'wechat'">
                            <div class="payment-icon wechat">
                                <i class="fab fa-weixin"></i>
                            </div>
                            <div class="payment-name">微信支付</div>
                        </div>

                        <div class="payment-method" :class="{ selected: paymentMethod === 'bank' }"
                            @click="paymentMethod = 'bank'">
                            <div class="payment-icon bank">
                                <i class="fas fa-credit-card"></i>
                            </div>
                            <div class="payment-name">银行卡支付</div>
                        </div>

                        <div class="payment-method" :class="{ selected: paymentMethod === 'cash' }"
                            @click="paymentMethod = 'cash'">
                            <div class="payment-icon cash">
                                <i class="fas fa-money-bill-wave"></i>
                            </div>
                            <div class="payment-name">货到付款</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 右侧订单摘要 -->
            <div class="right-column">
                <div class="order-summary">
                    <div class="section-title">
                        <i class="fas fa-receipt"></i>
                        订单摘要
                    </div>

                    <div class="summary-row">
                        <span>商品总额</span>
                        <span>¥{{ summary.subtotal }}</span>
                    </div>
                    <div class="summary-row">
                        <span>运费</span>
                        <span>+ ¥{{ summary.shipping }}</span>
                    </div>
                    <div class="summary-row">
                        <span>优惠</span>
                        <span>- ¥{{ summary.discount }}</span>
                    </div>

                    <div class="coupon-box">
                        <input type="text" class="coupon-input" placeholder="输入优惠码">
                        <button class="apply-btn">应用</button>
                    </div>

                    <div class="summary-row total">
                        <span>应付总额</span>
                        <span>¥{{ summary.total }}</span>
                    </div>

                    <button class="pay-btn" @click="payNow">
                        立即支付
                    </button>

                    <div class="agreement">
                        <input type="checkbox" id="agreement" checked>
                        <label for="agreement">我已阅读并同意 <a href="#">《小米商城支付协议》</a></label>
                    </div>
                </div>
            </div>
        </div>

        <!-- 添加地址模态框 -->
        <div class="modal-overlay" v-if="showAddAddressModal" @click.self="showAddAddressModal = false">
            <div class="modal-content">
                <div class="modal-header">
                    <h3>添加新地址</h3>
                    <button class="close-btn" @click="showAddAddressModal = false">&times;</button>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <label>收货人</label>
                        <input type="text" v-model="newAddress.name" placeholder="请输入收货人姓名">
                    </div>
                    <div class="form-group">
                        <label>手机号码</label>
                        <input type="text" v-model="newAddress.phone" placeholder="请输入手机号码">
                    </div>
                    <div class="form-group">
                        <label>省份</label>
                        <input type="text" v-model="newAddress.province" placeholder="请输入省份">
                    </div>
                    <div class="form-group">
                        <label>城市</label>
                        <input type="text" v-model="newAddress.city" placeholder="请输入城市">
                    </div>
                    <div class="form-group">
                        <label>区县</label>
                        <input type="text" v-model="newAddress.district" placeholder="请输入区县">
                    </div>
                    <div class="form-group">
                        <label>详细地址</label>
                        <input type="text" v-model="newAddress.detail" placeholder="请输入详细地址">
                    </div>
                    <div class="form-group checkbox-group">
                        <input type="checkbox" id="defaultAddress" v-model="newAddress.isDefault">
                        <label for="defaultAddress">设为默认地址</label>
                    </div>
                </div>
                <div class="modal-footer">
                    <button class="cancel-btn" @click="showAddAddressModal = false">取消</button>
                    <button class="confirm-btn" @click="addNewAddress">确认添加</button>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
/* 添加模态框样式 */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    border-radius: 8px;
    width: 500px;
    max-width: 90%;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.modal-header {
    padding: 15px 20px;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.modal-header h3 {
    margin: 0;
    font-size: 18px;
}

.close-btn {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #999;
}

.modal-body {
    padding: 20px;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input[type="text"] {
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

.checkbox-group {
    display: flex;
    align-items: center;
}

.checkbox-group input {
    margin-right: 8px;
}

.modal-footer {
    padding: 15px 20px;
    border-top: 1px solid #eee;
    display: flex;
    justify-content: flex-end;
}

.cancel-btn, .confirm-btn {
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.cancel-btn {
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    margin-right: 10px;
}

.confirm-btn {
    background-color: #ff6700;
    color: white;
    border: none;
}

.confirm-btn:hover {
    background-color: #ff8533;
}
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
}

body {
    background-color: #f5f5f5;
    color: #333;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* 头部样式 */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
    border-bottom: 1px solid #eee;
    background: white;
    padding: 0 20px;
}

.logo {
    font-size: 28px;
    font-weight: bold;
    color: #ff6700;
    display: flex;
    align-items: center;
}

.logo i {
    margin-right: 8px;
    font-size: 32px;
}

.step-bar {
    display: flex;
    margin: 30px 0;
    justify-content: center;
}

.step {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    width: 180px;
}

.step:not(:last-child)::after {
    content: "";
    position: absolute;
    top: 20px;
    left: 90px;
    width: 180px;
    height: 2px;
    background: #ddd;
    z-index: 1;
}

.step-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #ddd;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 18px;
    z-index: 2;
}

.step.active .step-circle {
    background: #ff6700;
}

.step-text {
    margin-top: 10px;
    color: #999;
}

.step.active .step-text {
    color: #ff6700;
    font-weight: bold;
}

/* 主要内容 */
.main-content {
    display: flex;
    gap: 20px;
    margin-bottom: 40px;
}

.order-section,
.payment-section {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 20px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 18px;
    font-weight: bold;
    padding-bottom: 15px;
    margin-bottom: 20px;
    border-bottom: 1px solid #eee;
    color: #333;
    display: flex;
    align-items: center;
}

.section-title i {
    margin-right: 10px;
    color: #ff6700;
}

.left-column {
    flex: 3;
}

.right-column {
    flex: 2;
}

/* 订单商品 */
.order-item {
    display: flex;
    padding: 15px 0;
    border-bottom: 1px solid #f5f5f5;
}

.item-img {
    width: 80px;
    height: 80px;
    border: 1px solid #f5f5f5;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 15px;
    background: #fafafa;
}

.item-img img {
    max-width: 90%;
    max-height: 90%;
}

.item-info {
    flex: 1;
}

.item-name {
    font-size: 16px;
    margin-bottom: 5px;
}

.item-spec {
    font-size: 13px;
    color: #999;
    margin-bottom: 8px;
}

.item-price {
    font-size: 16px;
    color: #ff6700;
    font-weight: bold;
}

.item-quantity {
    color: #666;
    font-size: 14px;
}

/* 地址样式 */
.address-card {
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 15px;
    margin-bottom: 15px;
    cursor: pointer;
    transition: all 0.3s;
}

.address-card:hover {
    border-color: #ff6700;
}

.address-card.selected {
    border: 2px solid #ff6700;
    background: #fffaf7;
}

.address-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
}

.user-info {
    display: flex;
    align-items: center;
}

.user-name {
    font-weight: bold;
    margin-right: 15px;
}

.user-phone {
    color: #666;
}

.default-tag {
    background: #ff6700;
    color: white;
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 3px;
}

.address-detail {
    color: #666;
    line-height: 1.5;
}

.add-address {
    text-align: center;
    color: #ff6700;
    padding: 15px;
    border: 1px dashed #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s;
}

.add-address:hover {
    border-color: #ff6700;
    background: #fffaf7;
}

.add-address i {
    margin-right: 5px;
}

/* 支付方式 */
.payment-methods {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

.payment-method {
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 15px;
    cursor: pointer;
    transition: all 0.3s;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.payment-method:hover {
    border-color: #ff6700;
}

.payment-method.selected {
    border: 2px solid #ff6700;
    background: #fffaf7;
}

.payment-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.payment-name {
    font-size: 14px;
    font-weight: bold;
}

.alipay {
    color: #009fe8;
}

.wechat {
    color: #09bb07;
}

.bank {
    color: #ff6700;
}

.cash {
    color: #666;
}

/* 订单摘要 */
.order-summary {
    background: #fafafa;
    border-radius: 8px;
    padding: 20px;
    margin-top: 30px;
}

.summary-row {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    color: #666;
}

.summary-row.total {
    font-size: 18px;
    color: #ff6700;
    font-weight: bold;
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #eee;
}

.coupon-box {
    display: flex;
    gap: 10px;
    margin: 15px 0;
}

.coupon-input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    outline: none;
}

.apply-btn {
    background: #eee;
    border: none;
    padding: 0 15px;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.3s;
}

.apply-btn:hover {
    background: #ddd;
}

/* 支付按钮 */
.pay-btn {
    background: #ff6700;
    color: white;
    border: none;
    width: 100%;
    padding: 16px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 2px 10px rgba(255, 103, 0, 0.3);
    margin-top: 20px;
}

.pay-btn:hover {
    background: #e25807;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 103, 0, 0.4);
}

.pay-btn:active {
    transform: translateY(0);
}

.agreement {
    display: flex;
    align-items: center;
    font-size: 13px;
    color: #666;
    margin-top: 15px;
}

.agreement input {
    margin-right: 8px;
}

.agreement a {
    color: #ff6700;
    text-decoration: none;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .main-content {
        flex-direction: column;
    }

    .step-bar {
        flex-wrap: wrap;
    }

    .step:not(:last-child)::after {
        display: none;
    }

    .payment-methods {
        grid-template-columns: 1fr;
    }
}

/* 动画效果 */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.order-section,
.payment-section,
.order-summary {
    animation: fadeIn 0.5s ease-out;
}

.order-summary {
    animation-delay: 0.2s;
}
</style>