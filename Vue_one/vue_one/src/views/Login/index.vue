<script setup>
import api from '@/apis';
import { useRouter } from 'vue-router';
import { ref, reactive } from 'vue';
import { useTimer } from '@/composables/timeout';
import { userStore } from '@/stores/userStore';
const router = useRouter()
// 获取用户pinia
const store = userStore()
// 登录表单
const loginform = reactive({
  phone: '',
  pwd: '',
  code: ''
})
// 登录
const LoginHandler = async (e) => {
  e.preventDefault()
  const res = await api.login(loginform)
  sessionStorage.setItem('token',res.token)   
  console.log(res);
  
  if (res.status == 200) {
    await store.getuserinfo(res.user_id)   
    router.push({ name: 'home' })
  }
  else{
    alert('登录失败')
  }
}

const { codeText, startTimer,captchaImage } = useTimer()

// 获取验证码
const CodeHandle = async (e) => {
  e.preventDefault()
  await startTimer()
}

// 利用ref的倒计时
// const code = ref('null')
// const codeText = '获取验证码'
// let timeleft = ref(60)
// let timer = null
// const CodeHandle = (e) =>{
//   if(timer){
//     return
//   }
//   code.value.innerHTML = `${timeleft.value}s可获取`
//   timer = setInterval(()=>{
//     timeleft.value--;
//     code.value.innerHTML = `${timeleft.value}s可获取`
//     if(timeleft.value<=0){
//       clearInterval(timer);
//       timer =null
//       code.value.innerHTML = codeText
//     }
//   },1000)
// }
</script>

<template>
  <div class="login-container">
    <div class="floating-bubbles">
      <!-- 动态气泡背景 -->
    </div>

    <div class="container" id="form-container">
      <h2 id="form-title">登录</h2>
      <form id="form">
        <div class="form-group">
          <label for="phone">手机号</label>
          <input v-model="loginform.phone" type="phone" id="phone" required placeholder="请输入您的手机号" />
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input v-model="loginform.pwd" type="password" id="password" required placeholder="请输入您的密码" />
        </div>
        <div class="one"><input v-model="loginform.code" type="text" placeholder="请输入验证码"><a href="" @click="CodeHandle"><span ref="code">{{
          codeText }}</span></a>
        </div>
        <!-- 模板中显示 -->
        <div><img :src="captchaImage" alt="验证码" v-if="captchaImage" /></div>
        <button type="submit" id="submit-btn" @click.prevent="LoginHandler">登录</button>
      </form>
      <div class="toggle-link" id="toggle-link" @click="router.push('/register')">没有账号？注册</div>
    </div>
  </div>
</template>
<style scoped>
.one {
  display: flex;
}

.one input {
  width: 50%;
}

.one a {
  margin: auto;
}

.login-container {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  overflow: hidden;
}

@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.container {
  background: rgba(255, 255, 255, 0.9);
  padding: 40px;
  width: 380px;
  border-radius: 12px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  transition: all 0.4s ease;
  backdrop-filter: blur(5px);
  z-index: 2;
}

.container:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
  font-weight: 600;
  font-size: 28px;
}

label {
  display: block;
  margin: 15px 0 8px;
  font-size: 14px;
  color: #555;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.3s;
  background: rgba(255, 255, 255, 0.8);
}

input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
}

button {
  margin-top: 25px;
  width: 100%;
  padding: 12px;
  background: linear-gradient(to right, #667eea, #764ba2);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: all 0.3s;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

.toggle-link {
  margin-top: 20px;
  text-align: center;
  font-size: 14px;
  color: #667eea;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s;
}

.toggle-link:hover {
  color: #764ba2;
  text-decoration: underline;
}

.form-group {
  position: relative;
  margin-bottom: 20px;
  opacity: 1;
  transform: translateY(0);
  transition: all 0.4s ease;
}

.floating-bubbles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  overflow: hidden;
}

.bubble {
  position: absolute;
  bottom: -100px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  animation: rise 10s infinite ease-in;
}

@keyframes rise {
  0% {
    bottom: -100px;
    transform: translateX(0);
  }

  50% {
    transform: translateX(100px);
  }

  100% {
    bottom: 1080px;
    transform: translateX(-200px);
  }
}
</style>