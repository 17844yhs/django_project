<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-container">
        <div class="modal-header">
          <h3>退出登录</h3>
        </div>
        
        <div class="modal-body">
          <p>确定要退出当前账号吗？</p>
        </div>
        
        <div class="modal-footer">
          <button class="btn-cancel" @click="close">取消</button>
          <button class="btn-confirm" @click="confirmLogout">确定退出</button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, defineEmits, defineProps } from 'vue'
// 声明组件接收的 props（父组件传递进来的属性）
const props = defineProps({
  show: {
    type: Boolean,
    required: true
  }
})
// 声明组件会向父组件触发的自定义事件
const emit = defineEmits(['close', 'confirm'])

// emit('close') 会触发父组件监听的 @close 事件
// emit('confirm') 会触发父组件监听的 @confirm 事件
const close = () => {
  emit('close')
}

const confirmLogout = () => {
  emit('confirm')
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 400px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.modal-header h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.modal-body {
  padding: 20px;
  color: #666;
}

.modal-footer {
  padding: 15px 20px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.btn-cancel {
  padding: 8px 16px;
  background-color: #f5f5f5;
  color: #666;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-cancel:hover {
  background-color: #e0e0e0;
}

.btn-confirm {
  padding: 8px 16px;
  background-color: #ff6700;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-confirm:hover {
  background-color: #e65c00;
}

/* 过渡动画 */
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  transform: scale(0.9);
}
</style>