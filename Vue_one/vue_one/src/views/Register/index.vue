<script setup>
import { useRouter } from 'vue-router';
import api from '@/apis';
import { reactive } from 'vue';
const RegisterForm = reactive({
  phone:'',
  pwd:'',
  nick_name:'',
})
const router = useRouter()
const RegisterHandle = async(e)=>{
  const res =await api.register(RegisterForm)
  if(res.status==200){
    router.push('/login')
  }  
  else{
    alert(res.msg)
  }
}
</script>

<template>
  <div class="login-page">
    <!-- 粒子背景 -->
    <div class="particles" id="particles"></div>
    
    <div class="form-wrapper">
      <div class="form-container">
        <h2>注册账号</h2>
        <form>
          <div class="input-group">
            <i class="fas fa-user"></i>
            <label for="username">用户名</label>
            <input v-model="RegisterForm.nick_name" type="text" id="username" name="username" placeholder="请输入用户名" required />
          </div>
          
          <div class="input-group">
            <i class="fas fa-phone"></i>
            <label for="phone">手机号</label>
            <input v-model="RegisterForm.phone" type="tel" id="phone" name="phone" placeholder="请输入手机号" required />
          </div>
          
          <div class="input-group">
            <i class="fas fa-lock"></i>
            <label for="password">密码</label>
            <input v-model="RegisterForm.pwd" type="password" id="password" name="password" placeholder="请输入密码" required />
          </div>
          
          <div class="input-group">
            <i class="fas fa-check-circle"></i>
            <label for="confirm-password">确认密码</label>
            <input type="password" id="confirm-password" name="confirm-password" placeholder="请再次输入密码" required />
          </div>
          
          <button type="submit" @click.prevent="RegisterHandle">
            <i class="fas fa-user-plus"></i> 立即注册
          </button>
        </form>
        <div class="toggle-link">
          <a href="#" @click="router.push('/login')"><i class="fas fa-sign-in-alt"></i> 已有账号？登录</a>
        </div>
      </div>
    </div>
  </div>
</template>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

.login-page {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: url('https://images.unsplash.com/photo-1635070041078-e363dbe005cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80') no-repeat center center fixed;
  background-size: cover;
  font-family: 'Poppins', sans-serif;
}

.login-page::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  z-index: 1;
}

.form-wrapper {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.form-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
  animation: fadeIn 0.8s ease-out;
  transform-style: preserve-3d;
  transition: all 0.5s ease;
  width: 100%;
  max-width: 500px;
}

.form-container:hover {
  transform: translateY(-10px) rotateX(5deg);
  box-shadow: 0 35px 60px rgba(0, 0, 0, 0.3);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h2 {
  color: #fff;
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  font-weight: 600;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.input-group {
  position: relative;
  margin-bottom: 25px;
}

.input-group i {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255, 255, 255, 0.7);
  font-size: 18px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 15px 15px 15px 45px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  color: #fff;
  font-size: 15px;
  transition: all 0.3s ease;
}

input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
}

button {
  width: 100%;
  padding: 15px;
  background: linear-gradient(45deg, #ff4d7d, #ff6b6b);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 20px;
  transition: all 0.4s ease;
  box-shadow: 0 5px 15px rgba(255, 77, 125, 0.4);
  position: relative;
  overflow: hidden;
}

button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(255, 77, 125, 0.6);
}

button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: 0.5s;
}

button:hover::before {
  left: 100%;
}

.toggle-link {
  text-align: center;
  margin-top: 25px;
}

.toggle-link a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-size: 14px;
  transition: all 0.3s ease;
  position: relative;
}

.toggle-link a:hover {
  color: #fff;
}

.toggle-link a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: #fff;
  transition: width 0.3s ease;
}

.toggle-link a:hover::after {
  width: 100%;
}

/* 粒子背景效果 */
.particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.particle {
  position: absolute;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  pointer-events: none;
  animation: float linear infinite;
}

@keyframes float {
  0% {
    transform: translateY(0) translateX(0);
  }
  50% {
    transform: translateY(-100px) translateX(50px);
  }
  100% {
    transform: translateY(0) translateX(0);
  }
}

/* 响应式设计 */
@media (max-width: 576px) {
  .form-container {
    padding: 30px 20px;
  }
  
  h2 {
    font-size: 24px;
  }
  
  input {
    padding: 12px 12px 12px 40px;
  }
}
</style>