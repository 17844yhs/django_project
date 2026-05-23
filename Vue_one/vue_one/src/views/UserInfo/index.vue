<script setup>
import { ref, onMounted } from 'vue';
import { userStore } from '@/stores/userStore';
import router from '@/router';
// 用户数据
const user = ref({})
const userinfo = userStore()
// 当前日期
const currentDate = ref('');
// Toast提示
const showToast = ref(false);
const toastMessage = ref('');

// 初始化日期
const initDate = () => {
    const now = new Date();
    currentDate.value = now.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
};

// 格式化手机号
const formatPhone = (phone) => {
    if (!phone) return '';
    return phone.replace(/(\d{3})(\d{4})(\d{4})/, '$1****$3');
};

// 显示Toast提示
const showNotification = (message) => {
    toastMessage.value = message;
    showToast.value = true;
    setTimeout(() => {
        showToast.value = false;
    }, 2000);
};

// 编辑个人信息
const editProfile = () => {
    showNotification('进入编辑模式，可以修改个人信息');
};

// 更换头像
const changeAvatar = () => {
    showNotification('打开头像选择器，选择新的头像');
};

// 下载资料
const downloadProfile = () => {
    showNotification('开始下载个人资料PDF文件');
};

// 展示活动记录
const showActivities = () => {
    showNotification('展示用户活动记录');
};

// 展示用户等级
const showLevel = () => {
    showNotification('展示用户等级详情');
};

// 展示用户成就
const showAchievements = () => {
    showNotification('展示用户成就列表');
};

const get_data = () =>{
    user.value = userinfo.userinfo
    
}
// 组件挂载时初始化日期
onMounted(() => {
    initDate();
    get_data()
});



</script>

<template>
    <div class="container">
        <div class="profile-header">
            <h3><a href="" @click="router.push('/')">主页</a></h3>
            <h1>个人信息中心</h1>
            <p>在这里管理您的个人资料和账号信息</p>
            <div class="edit-icon" @click="editProfile">
                <i class="fas fa-edit">编辑</i>
            </div>
        </div>

        <div class="profile-content">
            <div class="avatar-section">
                <div class="avatar-container">
                    <template v-if="user.avatar">
                        <img :src="'http://localhost:8000/static'+user.avatar" alt="用户头像">
                    </template>
                    <template v-else>
                        <div class="avatar-placeholder">
                            <i class="fas fa-user"></i>
                        </div>
                    </template>
                </div>

                <div class="avatar-actions">
                    <button class="btn btn-primary" @click="changeAvatar">
                        <i class="fas fa-camera"></i> 更换头像
                    </button>
                    <button class="btn btn-secondary" @click="downloadProfile">
                        <i class="fas fa-download"></i> 下载资料
                    </button>
                </div>
            </div>

            <div class="info-section">
                <div class="info-card">
                    <h2><i class="fas fa-user-circle"></i> 基本信息</h2>

                    <div class="info-item">
                        <div class="info-icon">
                            <i class="fas fa-hashtag"></i>
                        </div>
                        <div class="info-content">
                            <div class="info-label">用户ID</div>
                            <div class="info-value">{{ user.id }} <span class="badge badge-blue">已验证</span></div>
                        </div>
                    </div>

                    <div class="info-item">
                        <div class="info-icon">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <div class="info-content">
                            <div class="info-label">手机号码</div>
                            <div class="info-value">{{ formatPhone(user.phone) }} <span
                                    class="badge badge-green">已绑定</span></div>
                        </div>
                    </div>

                    <div class="info-item">
                        <div class="info-icon">
                            <i class="fas fa-user-tag"></i>
                        </div>
                        <div class="info-content">
                            <div class="info-label">昵称</div>
                            <div class="info-value">
                                {{ user.nick_name }}
                                <span class="badge badge-purple">默认昵称</span>
                            </div>
                        </div>
                    </div>

                    <div class="info-item">
                        <div class="info-icon">
                            <i class="fas fa-venus-mars"></i>
                        </div>
                        <div class="info-content">
                            <div class="info-label">性别</div>
                            <div class="info-value"
                                :class="{ 'gender-male': user.gender === 1, 'gender-female': user.gender === 2 }">
                                <template v-if="user.gender === 1">男</template>
                                <template v-else-if="user.gender === 2">女</template>
                                <template v-else>未设置</template>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="info-card">
                    <h2><i class="fas fa-file-alt"></i> 个人简介</h2>
                    <div class="introduction">
                        {{ user.introduction }}
                    </div>
                </div>

                <div class="stats-section">
                    <div class="stat-card stat-1" @click="showActivities">
                        <div class="stat-icon">
                            <i class="fas fa-calendar-check"></i>
                        </div>
                        <div class="stat-content">
                            <h3>128 天</h3>
                            <p>加入时间</p>
                        </div>
                    </div>

                    <div class="stat-card stat-2" @click="showLevel">
                        <div class="stat-icon">
                            <i class="fas fa-star"></i>
                        </div>
                        <div class="stat-content">
                            <h3>黄金会员</h3>
                            <p>用户等级</p>
                        </div>
                    </div>

                    <div class="stat-card stat-3" @click="showAchievements">
                        <div class="stat-icon">
                            <i class="fas fa-trophy"></i>
                        </div>
                        <div class="stat-content">
                            <h3>24 项</h3>
                            <p>获得成就</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            © 2023 个人资料中心 | 数据最后更新: {{ currentDate }}
        </div>
    </div>

    <div v-if="showToast" class="action-toast">
        {{ toastMessage }}
    </div>
</template>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    color: #333;
}

.container {
    width: 100%;
    max-width: 1000px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    overflow: hidden;
    animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.profile-header {
    background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
    padding: 35px 40px;
    color: white;
    text-align: center;
    position: relative;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.profile-header h1 {
    font-size: 32px;
    margin-bottom: 8px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.profile-header p {
    font-size: 18px;
    opacity: 0.92;
    max-width: 600px;
    margin: 0 auto;
}

.profile-content {
    display: flex;
    padding: 40px;
    position: relative;
}

@media (max-width: 768px) {
    .profile-content {
        flex-direction: column;
        align-items: center;
    }
}

.avatar-section {
    flex: 0 0 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-right: 40px;
    border-right: 1px solid #eee;
}

@media (max-width: 768px) {
    .avatar-section {
        border-right: none;
        border-bottom: 1px solid #eee;
        padding-right: 0;
        padding-bottom: 30px;
        margin-bottom: 30px;
        width: 100%;
    }
}

.avatar-container {
    position: relative;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 15px 40px rgba(67, 97, 238, 0.3);
    border: 5px solid white;
    background: linear-gradient(135deg, #e0e7ff 0%, #d0d8fd 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.avatar-container:hover {
    transform: scale(1.05);
    box-shadow: 0 20px 50px rgba(67, 97, 238, 0.4);
}

.avatar-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.avatar-placeholder {
    font-size: 90px;
    color: #4361ee;
    opacity: 0.7;
}

.avatar-actions {
    margin-top: 28px;
    display: flex;
    gap: 15px;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
}

.btn {
    padding: 12px 25px;
    border-radius: 50px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 15px;
    border: none;
    outline: none;
}

.btn-primary {
    background: #4361ee;
    color: white;
    box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
}

.btn-primary:hover {
    background: #3a0ca3;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(67, 97, 238, 0.4);
}

.btn-secondary {
    background: white;
    color: #4361ee;
    border: 2px solid #4361ee;
}

.btn-secondary:hover {
    background: #f0f2ff;
    transform: translateY(-3px);
}

.info-section {
    flex: 1;
    padding-left: 40px;
}

@media (max-width: 768px) {
    .info-section {
        padding-left: 0;
        width: 100%;
    }
}

.info-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    padding: 30px;
    margin-bottom: 30px;
    transition: transform 0.3s ease;
}

.info-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
}

.info-card h2 {
    color: #2c3e50;
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 2px solid #f0f3f5;
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 24px;
}

.info-item {
    display: flex;
    margin-bottom: 20px;
    padding: 15px 18px;
    border-radius: 12px;
    transition: all 0.3s;
}

.info-item:hover {
    background-color: #f8f9ff;
    transform: translateX(8px);
}

.info-icon {
    width: 50px;
    height: 50px;
    border-radius: 14px;
    background: #eef2ff;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 22px;
    color: #4361ee;
    flex-shrink: 0;
    margin-right: 22px;
    transition: all 0.3s;
}

.info-item:hover .info-icon {
    background: #4361ee;
    color: white;
    transform: scale(1.1);
}

.info-content {
    flex: 1;
}

.info-label {
    font-size: 14px;
    color: #6c757d;
    margin-bottom: 7px;
    font-weight: 500;
}

.info-value {
    font-size: 19px;
    font-weight: 600;
    color: #2c3e50;
}

.gender-male {
    color: #4361ee;
    position: relative;
    padding-left: 24px;
}

.gender-male::before {
    content: "♂";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
}

.gender-female {
    color: #f72585;
    position: relative;
    padding-left: 24px;
}

.gender-female::before {
    content: "♀";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
}

.introduction {
    background: linear-gradient(to right, #f8f9ff, #f0f2ff);
    padding: 25px;
    border-radius: 14px;
    font-size: 16px;
    line-height: 1.8;
    color: #4a5568;
    border-left: 4px solid #4361ee;
    box-shadow: inset 0 4px 12px rgba(0, 0, 0, 0.03);
}

.stats-section {
    display: flex;
    gap: 20px;
    margin-top: 30px;
}

@media (max-width: 576px) {
    .stats-section {
        flex-direction: column;
    }
}

.stat-card {
    flex: 1;
    background: white;
    border-radius: 15px;
    padding: 22px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
    display: flex;
    align-items: center;
    gap: 18px;
    transition: all 0.4s ease;
    cursor: pointer;
}

.stat-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.stat-icon {
    width: 60px;
    height: 60px;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 26px;
}

.stat-1 .stat-icon {
    background: rgba(67, 97, 238, 0.12);
    color: #4361ee;
}

.stat-2 .stat-icon {
    background: rgba(72, 207, 173, 0.12);
    color: #48cfad;
}

.stat-3 .stat-icon {
    background: rgba(155, 89, 182, 0.12);
    color: #9b59b6;
}

.stat-card:hover .stat-icon {
    transform: rotate(10deg);
}

.stat-content h3 {
    font-size: 24px;
    color: #2c3e50;
    margin-bottom: 5px;
}

.stat-content p {
    font-size: 14px;
    color: #718096;
}

.footer {
    text-align: center;
    padding: 25px;
    color: #718096;
    font-size: 14px;
    background: #f8f9ff;
    border-top: 1px solid #eef2ff;
}

.edit-icon {
    position: absolute;
    top: 25px;
    right: 25px;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.4s ease;
    backdrop-filter: blur(4px);
}

.edit-icon:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: rotate(15deg) scale(1.1);
}

.badge {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: bold;
    margin-left: 10px;
}

.badge-blue {
    background: #eef2ff;
    color: #4361ee;
}

.badge-purple {
    background: #f3e8fd;
    color: #7209b7;
}

.badge-green {
    background: #e6f7ee;
    color: #2ecc71;
}

.action-toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    padding: 15px 30px;
    background: #4361ee;
    color: white;
    border-radius: 50px;
    font-weight: 600;
    box-shadow: 0 10px 30px rgba(67, 97, 238, 0.3);
    z-index: 100;
    animation: slideUp 0.5s ease forwards;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translate(-50%, 20px);
    }

    to {
        opacity: 1;
        transform: translate(-50%, 0);
    }
}
</style>