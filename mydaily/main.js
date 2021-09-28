//导入Vue框架
import Vue from 'vue';
//导入app.vue组件
import App from './app.vue';
import './style.css';

new Vue({
    el:"#app",
    render: function(h) {
        return h(App)
    }   
});