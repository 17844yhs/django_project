import { ref } from 'vue';
import api from '@/apis';
export const useTimer = () => {
    // 验证码图片
    const captchaImage = ref('')
    const fetchCaptcha = async () => {
        try {
            const res = await api.get_captcha(); // 注意 responseType

            // 核心转换代码
            const blob = new Blob([res], { type: 'image/png' });
            captchaImage.value = URL.createObjectURL(blob);
            // 图片加载成功后打印 captchaImage
            // console.log(captchaImage.value);
        } catch (error) {
            console.error('获取验证码失败:', error);
        }
    };
    const codeText = ref('获取验证码');
    const timesave = ref(60); // 初始倒计时 60 秒
    let timeid = null;

    const startTimer =async (e) => {
        // 如果已有倒计时在运行，则不再启动新的倒计时
        if (timeid) return;
        // 获取图片
        await fetchCaptcha()
        // 显示初始的倒计时文本
        codeText.value = `${timesave.value}s可获取`;
        // 使用 setInterval 启动倒计时，每秒更新一次
        timeid = setInterval(() => {
            timesave.value--; // 每秒减少一次时间
            codeText.value = `${timesave.value}s可获取`; // 更新显示的倒计时文本

            // 当倒计时为 0 时，停止倒计时并更新按钮文本
            if (timesave.value <= 0) {
                clearInterval(timeid); // 停止倒计时
                timeid = null; // 重置 timeid，允许重新启动倒计时
                codeText.value = '获取验证码'; // 恢复按钮文本
                timesave.value = 60
            }
        }, 1000); // 每 1000 毫秒执行一次，即每秒执行一次
    };    
    return { codeText, startTimer,captchaImage};
};
