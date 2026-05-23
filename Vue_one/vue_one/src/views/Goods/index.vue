<script setup>
import api from '@/apis';
import router from '@/router';
import { ref, reactive, computed, onMounted } from 'vue';
import { cartStore } from '@/stores/cartStore';
import { userStore } from '@/stores/userStore';
const cart = cartStore()
const user = userStore()
const searchQuery = ref('');
const activeCategory = ref(null);
const minPrice = ref(500);
const maxPrice = ref(3000);
const categories = reactive([]);
const flag = ref('true')
// 获取分类信息e
const get_categories = async () => {
  const res = await api.get_category()
  res.forEach(e => {
    categories.push({
      id: e.id,
      name: e.name,
      count: e.count
    })
  });
}
// 获取所有商品信息
const get_goods = async () => {
  const res = await api.get_goodsbyname()
  res.data.forEach(e => {
    products.push({
      id: e.id,
      name: e.name,
      desc: e.description,
      price: e.price,
      badgeType: e.badgeType,
      stockText: '现货',
      categoryId: e.category.id,
      image: e.pic
    })
    console.log(e.badgeType);

  })

}
onMounted(() => {
  get_categories()
  get_goods()
})

const products = reactive([{}]);

const filteredProducts = computed(() => {
  return products.filter(product => {
    // 按类别过滤 如果activeCategory.value=false就是没有分类选择 则categoryMatch通过
    const categoryMatch = !activeCategory.value || product.categoryId === activeCategory.value;

    // 按价格过滤
    const priceMatch = product.price >= minPrice.value && product.price <= maxPrice.value;

    // 按搜索词过滤
    const searchMatch = searchQuery.value === '' ||
      product.name?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      product.desc?.toLowerCase().includes(searchQuery.value.toLowerCase());

    return categoryMatch && priceMatch && searchMatch;
  });
});
// 依靠分类搜索 点击当前搜索会取消当前下划线
const setActiveCategory = (categoryId) => {
  if (activeCategory.value === categoryId) {
    activeCategory.value = null;
  } else {
    activeCategory.value = categoryId;
  }
};
// 更改价格范围的最低值
const updateMinPrice = (value) => {
  minPrice.value = parseInt(value);
  if (minPrice.value > maxPrice.value) {
    maxPrice.value = minPrice.value;
  }
};
// 更改价格范围的最高值
const updateMaxPrice = (value) => {
  maxPrice.value = parseInt(value);
  if (maxPrice.value < minPrice.value) {
    minPrice.value = maxPrice.value;
  }
};
// 通过字符串返回新品等一系列标签
const productBadgeText = (type) => {
  const badgeTextMap = {
    'hot': '热卖',
    'new': '新品',
    'sale': '特惠'
  };
  return badgeTextMap[type] || '';
};
// 添加到购物车
const addToCart = async (product) => {
  // console.log(product);
  flag.value = true
  // 遍历购物车商品，检查是否已经添加过该商品
  cart.cart.data?.items.forEach(item => {
    if (item.goods.id === product.id) {
      alert('该商品已经在购物车');
      flag.value = false;  // 商品已经存在，设置 flag 为 false
    } 
  });
  if(!sessionStorage.getItem('token')){

  }

  // 如果商品不在购物车中，执行添加操作
  if (flag.value === true) {
    const params = {
      "goods_id": product.id,
      "quantity": 1,
      "phone": user.userinfo.phone
    };
    try{
      const res1 = await cart.addCart(params);  // 调用添加购物车的函数
      
      await cart.getcart() // 重新获取购物车数据
      alert(`已将 ${product.name} 加入到用户 ${user.userinfo.nick_name} 购物车！`);
      }
      catch(error){
       if(error.response.request.status==401){
        alert('用户需要登录')
        router.push('/login')
       }
        

      }
    
  }
};
// 搜索功能
const InputHandler = () =>{
  console.log(searchQuery.value);
  
}
  
</script>

<template>
  <!-- 头部 -->
  <header>
    <div class="container">
      <div class="header-content">
        <a href="#" class="logo">
          <i class="fas fa-fire"></i>
          <span>小米商城</span>
        </a>

        <div class="search-bar">
          <input  type="text" placeholder="搜索商品..." v-model="searchQuery">
          <button type="submit">
            <i class="fas fa-search"></i>
          </button>
        </div>

        <ul class="nav-links">
          <li>
            <a href="#">
              <i class="fas fa-home"></i>
              <span @click="router.push('/')">首页</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fas fa-heart"></i>
              <span>收藏</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fas fa-user"></i>
              <span @click="router.push('/my')">我的</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </header>

  <div class="container">
    <!-- 主要内容 -->
    <div class="main-content">
      <!-- 侧边栏筛选 -->
      <div class="sidebar">
        <h3><i class="fas fa-filter"></i> 商品分类</h3>
        <ul class="category-list">
          <li v-for="category in categories" :key="category.id">
            <a href="#" :class="{ active: activeCategory === category.id }"
              @click.prevent="setActiveCategory(category.id)">
              <span>{{ category.name }}</span>
              <span class="count">{{ category.count }}</span>
            </a>
          </li>
        </ul>

        <div class="price-filter">
          <h3><i class="fas fa-tag"></i> 价格范围</h3>
          <div class="price-slider">
            <div class="progress"
              :style="{ left: (minPrice / 5000 * 100) + '%', right: (100 - maxPrice / 5000 * 100) + '%' }">
            </div>
            <div class="range-input">
              <input type="range" min="0" max="5000" :value="minPrice" step="100"
                @input="updateMinPrice($event.target.value)">
              <input type="range" min="0" max="5000" :value="maxPrice" step="100"
                @input="updateMaxPrice($event.target.value)">
            </div>
          </div>
          <div class="price-values">
            <div class="price-field">
              <span>¥</span>
              <input type="number" v-model.number="minPrice" min="0" :max="maxPrice">
            </div>
            <span>-</span>
            <div class="price-field">
              <span>¥</span>
              <input type="number" v-model.number="maxPrice" :min="minPrice" max="5000">
            </div>
          </div>
        </div>
      </div>

      <!-- 商品网格 -->
      <div class="products-grid">
        <!-- 商品卡片 -->
        <div class="product-card" v-for="product in filteredProducts" :key="product.id">
          <span class="product-badge" :class="product.badgeType" v-if="product.badgeType">
            {{ productBadgeText(product.badgeType) }}
          </span>
          <div class="product-img">
            <img :src="'http://localhost:8000/static' + product.image" :alt="product.name">
          </div>
          <div class="product-info">
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-desc">{{ product.desc }}</p>
            <div class="product-meta">
              <div class="product-price">¥{{ product.price }}</div>
              <div class="product-stock">
                <i :class="product.stockIcon"></i>
                {{ product.stockText }}
              </div>
            </div>
          </div>
          <div class="product-actions">
            <button class="cart-btn" @click="addToCart(product)">
              <i class="fas fa-shopping-cart"></i>
              加入购物车
            </button>
            <button class="view-btn">查看详情</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 页脚 -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-column">
          <h4>帮助中心</h4>
          <ul>
            <li><a href="#">账户管理</a></li>
            <li><a href="#">购物指南</a></li>
            <li><a href="#">订单操作</a></li>
            <li><a href="#">配送方式</a></li>
            <li><a href="#">支付方式</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h4>服务支持</h4>
          <ul>
            <li><a href="#">售后政策</a></li>
            <li><a href="#">自助服务</a></li>
            <li><a href="#">相关下载</a></li>
            <li><a href="#">维修网点</a></li>
            <li><a href="#">预约维修</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h4>关于小米</h4>
          <ul>
            <li><a href="#">小米简介</a></li>
            <li><a href="#">加入小米</a></li>
            <li><a href="#">投资者关系</a></li>
            <li><a href="#">企业社会责任</a></li>
            <li><a href="#">廉洁举报</a></li>
          </ul>
        </div>

        <div class="footer-column">
          <h4>关注我们</h4>
          <ul>
            <li><a href="#">新浪微博</a></li>
            <li><a href="#">官方微信</a></li>
            <li><a href="#">联系我们</a></li>
            <li><a href="#">公益基金会</a></li>
          </ul>
        </div>
      </div>

      <div class="copyright">
        <p>小米公司 版权所有 京ICP备10046444号 | 京公网安备11010802020134号 | 京ICP证110507号</p>
        <p>小米商城 | MIUI | 米家 | 米聊 | 多看 | 游戏 | 政企服务 | 小米天猫店 | 小米集团隐私政策 | 小米商城用户协议 | 问题反馈</p>
      </div>
    </div>
  </footer>
</template>



<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
}

body {
  background-color: #f5f5f5;
  color: #333;
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* 头部样式 */
header {
  background: linear-gradient(#ff6700, #ff8d3f);
  padding: 15px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  font-size: 28px;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.logo i {
  margin-right: 10px;
  font-size: 32px;
}

.search-bar {
  flex: 1;
  max-width: 600px;
  margin: 0 30px;
  position: relative;
}

.search-bar input {
  width: 100%;
  padding: 12px 45px 12px 20px;
  border: none;
  border-radius: 30px;
  font-size: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.search-bar button {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #ff6700;
  font-size: 18px;
  cursor: pointer;
}

.nav-links {
  display: flex;
  list-style: none;
}

.nav-links li {
  margin-left: 25px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav-links i {
  font-size: 22px;
  margin-bottom: 5px;
}

/* 主要内容 */
.main-content {
  display: flex;
  margin: 30px 0;
  gap: 20px;
}

/* 侧边栏筛选 */
.sidebar {
  width: 250px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  padding: 20px;
  align-self: flex-start;
}

.sidebar h3 {
  font-size: 18px;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
  color: #333;
}

.category-list {
  list-style: none;
}

.category-list li {
  margin-bottom: 15px;
}

.category-list a {
  text-decoration: none;
  color: #666;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.3s;
}

.category-list a:hover {
  color: #ff6700;
}

.category-list .active {
  color: #ff6700;
  font-weight: 500;
}

.category-list .count {
  background: #f5f5f5;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 10px;
}

.price-filter {
  margin-top: 30px;
}

.price-slider {
  width: 100%;
  height: 5px;
  background: #ddd;
  border-radius: 5px;
  margin: 20px 0;
  position: relative;
}

.price-slider .progress {
  height: 100%;
  left: 25%;
  right: 25%;
  background: #ff6700;
  position: absolute;
  border-radius: 5px;
}

.range-input {
  position: relative;
}

.range-input input {
  position: absolute;
  top: -5px;
  height: 5px;
  width: 100%;
  background: none;
  pointer-events: none;
}

input[type="range"]::-webkit-slider-thumb {
  height: 17px;
  width: 17px;
  border-radius: 50%;
  background: #ff6700;
  pointer-events: auto;
  -webkit-appearance: none;
}

.price-values {
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

.price-field {
  display: flex;
  align-items: center;
  width: 45%;
}

.price-field span {
  font-size: 14px;
  color: #666;
}

.price-field input {
  width: 80px;
  margin-left: 10px;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

/* 商品网格 */
.products-grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 25px;
}

.product-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  position: relative;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.product-badge {
  position: absolute;
  top: 10px;
  left: 0;
  background: #ff6700;
  color: white;
  font-size: 12px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 0 4px 4px 0;
  z-index: 2;
}

.product-img {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background: linear-gradient(to bottom, #fafafa, white);
  border-bottom: 1px solid #f5f5f5;
}

.product-img img {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
  transition: transform 0.3s;
}

.product-card:hover .product-img img {
  transform: scale(1.05);
}

.product-info {
  padding: 20px;
}

.product-name {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 8px;
  height: 44px;
  overflow: hidden;
}

.product-desc {
  color: #999;
  font-size: 14px;
  margin-bottom: 15px;
  height: 40px;
  overflow: hidden;
}

.product-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
}

.product-price {
  font-size: 20px;
  font-weight: bold;
  color: #ff6700;
}

.product-stock {
  font-size: 13px;
  color: #666;
  display: flex;
  align-items: center;
}

.product-stock i {
  margin-right: 5px;
  color: #52c41a;
}

.product-actions {
  display: flex;
  border-top: 1px solid #f5f5f5;
}

.cart-btn {
  flex: 1;
  background: #f8f8f8;
  border: none;
  padding: 12px;
  color: #ff6700;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cart-btn i {
  margin-right: 8px;
}

.cart-btn:hover {
  background: #ff6700;
  color: white;
}

.view-btn {
  flex: 1;
  background: white;
  border: none;
  border-left: 1px solid #f5f5f5;
  padding: 12px;
  color: #666;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.view-btn:hover {
  color: #ff6700;
  background: #fdf6f2;
}

/* 页脚 */
footer {
  background: #333;
  color: #aaa;
  padding: 40px 0;
  margin-top: 50px;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.footer-column {
  flex: 1;
  min-width: 200px;
  margin-bottom: 30px;
}

.footer-column h4 {
  color: white;
  margin-bottom: 20px;
  font-size: 16px;
}

.footer-column ul {
  list-style: none;
}

.footer-column ul li {
  margin-bottom: 12px;
}

.footer-column a {
  color: #aaa;
  text-decoration: none;
  transition: all 0.3s;
  font-size: 14px;
}

.footer-column a:hover {
  color: #ff6700;
}

.copyright {
  text-align: center;
  padding-top: 20px;
  margin-top: 20px;
  border-top: 1px solid #444;
  font-size: 14px;
}

/* 响应式设计 */
@media (max-width: 900px) {
  .main-content {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    margin-bottom: 20px;
  }
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
  }

  .logo {
    margin-bottom: 15px;
  }

  .search-bar {
    margin: 15px 0;
    max-width: 100%;
  }

  .nav-links {
    width: 100%;
    justify-content: space-around;
  }

  .nav-links li {
    margin: 0;
  }

  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 480px) {
  .products-grid {
    grid-template-columns: 1fr;
  }
}
</style>